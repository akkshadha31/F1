# Project Development Phase (Tableau)
## Dashboard Design Template

| Metadata Field | Project Information |
| :--- | :--- |
| **Date** | 24 September 2026 / October 2026 |
| **Author / Team ID** | Akkshadha Rathore |
| **Project Name** | Formula 1 Race Intelligence |
| **Maximum Marks** | 5 Marks |

---

### Dashboard Layout & UI Design Principles

The **Formula 1 Race Intelligence Dashboard** adheres to the following core UX principles:
1. **Top Header & KPI Summary Row:**
   * Branded F1 header with checkered flag accents.
   * Four prominent KPI cards: **Competing Teams (10)**, **Seasons in Play (17)**, **Race Outcomes Logged (6,464)**, and **Circuits Showcased (29)**.
   * Interactive filters: `DNF Reason (All)`, `Year of Race Date (All)`, and `Top N Parameter (10)`.
2. **2×4 Analytical Grid:**
   * *Row 1:* Global Driver Distribution Map (Left) & Driver Reliability Analysis (Right).
   * *Row 2:* Driver Performance Leaderboard (Left) & Team Performance Ranking (Right).
   * *Row 3:* Team Championship Standings (Left), Tyre Usage Donut (Center-Left), Country Participation Treemap (Center-Right), Podium Bubble Chart (Right).
3. **Color Palette & Contrast:**
   * Strict dark background (`#0a0a0a` / `#151515`) with high-contrast colored bars matching official team liveries (Red Bull Navy, Mercedes Cyan, Ferrari Scarlet, McLaren Papaya).

---

### Major Dashboard Outcomes & Findings (Bullet Points)
* **Macro Scale & Coverage:** The dashboard models 6,464 total race outcomes logged across 17 competitive seasons and 29 world championship circuits, delivering the most comprehensive telemetry dataset in fan-accessible analytics.
* **Driver Performance Titan Clash:** Lewis Hamilton (31,147 pts) and Max Verstappen (31,126 pts) stand virtually dead-level atop the cumulative hybrid-era index, separated by a razor-thin margin of just 21 points.
* **Constructor Dominance:** Red Bull Racing (8,006 pts) and Mercedes (7,790 pts) dominate constructor standings, having converted 73% of front-row starts into Grand Prix podium finishes.
* **Pirelli Compound Balance:** Soft (31.52%), Medium (30.78%), and Hard (30.36%) compounds demonstrate near-equal race strategy distribution, proving Pirelli's targeted multi-stint strategy regulations.
* **Geographic Volume:** Bahrain International Circuit dominates historical testing and outcome volume with 2,168 sessions, followed by classic European street tracks (Monaco, Spain with 328 sessions each).

---

### Tableau Public Integration Link
* **Tableau Public Dashboard Link:**
  `https://public.tableau.com/views/Formula1RaceIntelligence/Dashboard1`
* **Web Container Implementation:** Encapsulated inside a macOS window frame with red/yellow/green control dots, fullscreen modal trigger, and high-resolution zero-crop fallback (`assets/dashboard-preview.png`).
