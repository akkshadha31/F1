# Project Development Phase (Tableau)
## Business Question and Visualization Report

| Metadata Field | Project Information |
| :--- | :--- |
| **Date** | 24 September 2026 / October 2026 |
| **Author / Team ID** | Akkshadha Rathore |
| **Project Name** | Formula 1 Race Intelligence |
| **Maximum Marks** | 5 Marks |

---

### Executive Visualization Framework
Transforming 6,464 historical and modern race outcomes, 3,814 telemetry laps, and 311 championship records into actionable business intelligence. Below are the **8 core business questions** driving the Tableau visualizations:

#### BQ-1: Global Driver Distribution Across Grand Prix Nations
* **Business Question:** What is the geographical footprint of Grand Prix racing volume and driver origin density across global host nations?
* **Visualization:** Filled Chloropleth World Map with overlay country count badges.
* **Telemetry Finding:** USA (400 race entries), Spain (328), Monaco (328), Canada (308), Brazil (308), Singapore (288), Mexico (160), Japan (140), Netherlands (140), Saudi Arabia (140), Azerbaijan (140), and China (40).
* **Reference Artifact:** `assets/dashboard-preview.png` (Top-Left Panel) & `assets/story-preview.png`.

#### BQ-2: Driver Reliability & DNF Root-Cause Analysis
* **Business Question:** How do mechanical failures versus collision incidents distribute across competitive drivers, and who demonstrates superior vehicle preservation?
* **Visualization:** Stacked Column Bar Chart categorized by failure modes (Mechanical, Collision, Engine, Gearbox, Electrical).
* **Telemetry Finding:** Carlos Sainz and Charles Leclerc absorbed high early-career mechanical attrition on high-speed circuits, whereas Lewis Hamilton maintained the highest vehicle completion rate ($> 94%$).
* **Reference Artifact:** `assets/dashboard-preview.png` (Top-Right Panel).

#### BQ-3: Hybrid-Era Driver Performance Leaderboard
* **Business Question:** Who are the dominant drivers in the modern hybrid regulation era when aggregating total performance points and win conversions?
* **Visualization:** Vertical Bar Chart ranked by total championship points index.
* **Telemetry Finding:** Lewis Hamilton leads with 31,147 points, closely rivaled by Max Verstappen at 31,126 points, followed by Charles Leclerc (27,673), Lando Norris (26,408), Yuki Tsunoda (14,438), Esteban Ocon (14,205), Carlos Sainz (11,004), and Fernando Alonso (1,353).
* **Reference Artifact:** `assets/dashboard-preview.png` (Mid-Left Panel).

#### BQ-4: Team Performance Ranking (Constructor Points)
* **Business Question:** Which constructor teams have established supreme engineering dominance in accumulated championship points?
* **Visualization:** Horizontal Bar Chart with constructor color branding.
* **Telemetry Finding:** Red Bull Racing leads the grid with 8,006 total points, followed closely by Mercedes AMG (7,790 pts), Ferrari (5,778 pts), McLaren (4,270 pts), Alpine (1,947 pts), Aston Martin (1,181 pts), Williams (1,057 pts), RB (923 pts), Haas (591 pts), and Kick Sauber (363 pts).
* **Reference Artifact:** `assets/dashboard-preview.png` (Mid-Right Panel).

#### BQ-5: Team Championship Performance Analysis
* **Business Question:** How do team points distribute across annual championship standings cycles?
* **Visualization:** Vertical Column Bar Chart of official championship standings totals.
* **Telemetry Finding:** Red Bull and Mercedes account for over 52% of all constructor points awarded since 2014, with Ferrari mounting sustained resurgence cycles.
* **Reference Artifact:** `assets/dashboard-preview.png` (Bottom-Left Panel).

#### BQ-6: Pirelli Tyre Compound Usage Distribution
* **Business Question:** What is the proportional usage of Pirelli tire compounds across telemetry-recorded racing laps?
* **Visualization:** Donut / Pie Chart showing percentage share and lap volume.
* **Telemetry Finding:** Soft compound represents 31.52% (1,202 laps), Medium represents 30.78% (1,174 laps), Hard represents 30.36% (1,158 laps), and Intermediate wet represents 7.34% (280 laps).
* **Reference Artifact:** `assets/dashboard-preview.png` (Bottom-Center-Left Panel).

#### BQ-7: Country-Wise Grand Prix Participation Volume
* **Business Question:** Which host nations and circuits represent the primary empirical volume in championship history?
* **Visualization:** Treemap Chart with size-weighted country blocks.
* **Telemetry Finding:** Bahrain International Circuit represents the highest telemetry concentration with 2,168 logged outcomes, followed by European and American Grand Prix hubs.
* **Reference Artifact:** `assets/dashboard-preview.png` (Bottom-Center-Right Panel).

#### BQ-8: Podium Achievements by Driver and Constructor
* **Business Question:** How do top-3 podium finishes cluster across driver-team partnerships?
* **Visualization:** Packed Bubble Chart with bubble volume scaled by podium finish frequency.
* **Telemetry Finding:** Dense, dominant clusters centered around Lewis Hamilton / Mercedes and Max Verstappen / Red Bull Racing, with widespread secondary clusters for Ferrari and McLaren.
* **Reference Artifact:** `assets/dashboard-preview.png` (Bottom-Right Panel).
