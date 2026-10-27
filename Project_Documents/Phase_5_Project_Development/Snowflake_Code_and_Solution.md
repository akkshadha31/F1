# Project Development Phase (Snowflake)
## Snowflake Project – Data Engineering & SQL Solution

| Metadata Field | Project Information |
| :--- | :--- |
| **Date** | 24 September 2026 / October 2026 |
| **Author / Team ID** | Akkshadha Rathore |
| **Project Name** | Formula 1 Race Intelligence |
| **Maximum Marks** | 5 Marks |

---

### Solution Summary Table

| Field | Engineering Specification / Solution Details |
| :--- | :--- |
| **Project Repository** | Local Git Repository `c:\Users\DELL\Pictures\F1` / GitHub Enterprise |
| **Data Source(s)** | `F1 Racing Project Dataset.xlsx` (5 sheets: circuits, standings, laps, qualifying, race results) |
| **Database Name** | `F1_INTELLIGENCE_DB` |
| **Virtual Warehouse** | `COMPUTE_WH` (Size: X-Small / Small, Auto-suspend 60s) |
| **Schemas Created** | `RAW` (Ingested CSVs), `STAGING` (Cleaned views), `CURATED` (Dimensional marts) |
| **Tables & Views** | `DIM_CIRCUITS`, `DIM_DRIVERS`, `DIM_CONSTRUCTORS`, `FACT_RACE_RESULTS`, `FACT_LAP_INTELLIGENCE`, `MART_DRIVER_LEADERBOARD`, `MART_CONSTRUCTOR_STANDINGS` |
| **Key SQL Transformations** | Window functions (`ROW_NUMBER`, `RANK`), `SUM()` point rollups, DNF root-cause categorization, tire wear stint lengths. |
| **KPIs Delivered** | Competing Teams (10), Seasons in Play (17), Outcomes Logged (6,464), Circuits (29), Win Conversion %, Podium Conversion %, Avg Pit Stop Time. |
| **Key Insights** | Red Bull Racing constructor leadership (8,006 pts); Hamilton/Verstappen leaderboard parity; Soft compound 31.52% share; Bahrain volume peak (2,168 outcomes). |

---

### Snowflake Quality Checklist

| S.No | Engineering Criteria | Status | Comments & Verification |
| :---: | :--- | :---: | :--- |
| 1 | Required data is successfully loaded and accessible in Snowflake | **Yes** | 6,464 race records and 3,814 lap records loaded into `RAW` stage. |
| 2 | Data is cleaned, transformed, and prepared appropriately | **Yes** | Encodings corrected, placeholders purged, DNF reasons standardized. |
| 3 | Required tables, views, and data relationships correctly implemented | **Yes** | Star schema implemented with foreign keys linking facts to dimensional tables. |
| 4 | Required SQL logic, calculations, and KPIs correctly implemented | **Yes** | Accurate points summation matches Tableau dashboard and local `data.js`. |
| 5 | Data and solution outputs validated against project requirements | **Yes** | Verified against reference screenshots and official F1 championship records. |
| 6 | Solution is properly organized, documented, and functional | **Yes** | Clean SQL scripts, reproducible pipeline, and offline-compatible data objects. |
