# Project Development Phase (Snowflake)
## Data Preparation Template (SQL Data Quality & Transformation)

| Metadata Field | Project Information |
| :--- | :--- |
| **Date** | 24 September 2026 / October 2026 |
| **Author / Team ID** | Akkshadha Rathore |
| **Project Name** | Formula 1 Race Intelligence |
| **Maximum Marks** | 5 Marks |

---

### Activity 1: Identifying and Handling Null Values

#### Analysis
In raw telemetry, `fastest_lap_time_s`, `gap_to_leader_s`, and `dnf_reason` contain NULL values for drivers who did not finish or did not record the fastest lap.

```sql
-- Identify NULL counts across critical race telemetry columns
SELECT 
    COUNT(*) AS total_rows,
    COUNT(CASE WHEN driver IS NULL THEN 1 END) AS null_drivers,
    COUNT(CASE WHEN team IS NULL THEN 1 END) AS null_teams,
    COUNT(CASE WHEN finish_position IS NULL THEN 1 END) AS null_finish_pos,
    COUNT(CASE WHEN dnf = TRUE AND dnf_reason IS NULL THEN 1 END) AS unclassified_dnfs
FROM F1_DB.STAGING.STG_RACE_RESULTS;

-- Treatment: Default unclassified DNF reasons to 'Technical/Mechanical'
UPDATE F1_DB.STAGING.STG_RACE_RESULTS
SET dnf_reason = 'Technical Issue'
WHERE dnf = TRUE AND (dnf_reason IS NULL OR TRIM(dnf_reason) = '');
```

---

### Activity 2: Duplicate Record Handling

```sql
-- Check for duplicate race entries per driver and event
WITH RankedRaces AS (
    SELECT 
        race_id, season, round, driver,
        ROW_NUMBER() OVER (PARTITION BY season, round, driver ORDER BY finish_position ASC) AS row_num
    FROM F1_DB.STAGING.STG_RACE_RESULTS
)
SELECT * FROM RankedRaces WHERE row_num > 1;

-- Clean duplicates by retaining primary valid finish outcome
DELETE FROM F1_DB.STAGING.STG_RACE_RESULTS
WHERE (race_id, driver) IN (
    SELECT race_id, driver FROM (
        SELECT race_id, driver,
               ROW_NUMBER() OVER (PARTITION BY season, round, driver ORDER BY finish_position ASC) AS rn
        FROM F1_DB.STAGING.STG_RACE_RESULTS
    ) WHERE rn > 1
);
```

---

### Activity 3: Data Cleaning & Standardization

```sql
-- Standardize driver names (encoding artifacts) and filter placeholder records
UPDATE F1_DB.STAGING.STG_RACE_RESULTS
SET driver = 'Nico Hülkenberg'
WHERE driver ILIKE '%Hlkenberg%' OR driver ILIKE '%Hulkenberg%';

-- Remove synthetic placeholders ('Driver_2', 'Team_2')
DELETE FROM F1_DB.STAGING.STG_RACE_RESULTS
WHERE driver ILIKE 'Driver_%' OR team ILIKE 'Team_%';

-- Standardize Pirelli tyre compound labels
UPDATE F1_DB.STAGING.STG_LAP_INTELLIGENCE
SET tyre_compound = CASE 
    WHEN tyre_compound ILIKE 'soft%' THEN 'Soft'
    WHEN tyre_compound ILIKE 'med%' THEN 'Medium'
    WHEN tyre_compound ILIKE 'hard%' THEN 'Hard'
    WHEN tyre_compound ILIKE 'inter%' THEN 'Intermediate'
    WHEN tyre_compound ILIKE 'wet%' THEN 'Wet'
    ELSE 'Other'
END;
```

---

### Activity 4: Data Transformation & Validation

```sql
-- Create Curated Analytics Mart for Driver Leaderboard
CREATE OR REPLACE TABLE F1_DB.CURATED.MART_DRIVER_LEADERBOARD AS
SELECT 
    driver,
    team,
    COUNT(DISTINCT season) AS seasons_active,
    COUNT(race_id) AS total_races,
    SUM(points) AS total_points,
    COUNT(CASE WHEN finish_position = 1 THEN 1 END) AS total_wins,
    COUNT(CASE WHEN finish_position IN (1, 2, 3) THEN 1 END) AS total_podiums,
    COUNT(CASE WHEN grid_position = 1 THEN 1 END) AS total_poles,
    COUNT(CASE WHEN dnf = TRUE THEN 1 END) AS total_dnfs,
    ROUND((COUNT(CASE WHEN finish_position = 1 THEN 1 END) / COUNT(race_id)) * 100, 2) AS win_conversion_pct,
    ROUND((COUNT(CASE WHEN finish_position IN (1, 2, 3) THEN 1 END) / COUNT(race_id)) * 100, 2) AS podium_conversion_pct
FROM F1_DB.STAGING.STG_RACE_RESULTS
GROUP BY driver, team;

-- Verification Check
SELECT * FROM F1_DB.CURATED.MART_DRIVER_LEADERBOARD ORDER BY total_points DESC LIMIT 10;
```
