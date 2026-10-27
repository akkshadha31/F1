# Performance Testing Phase
## Performance Testing – Tableau Dashboard & Story

| Metadata Field | Project Information |
| :--- | :--- |
| **Date** | 10 February 2026 / October 2026 |
| **Author / Team ID** | Akkshadha Rathore |
| **Project Name** | Formula 1 Race Intelligence |
| **Deliverable** | Model Performance Testing |

---

### Tableau Performance Testing Matrix

| S.No | Test Parameter | Evaluation Metric / Values | Test Result & Observations |
| :---: | :--- | :--- | :---: |
| **1** | **Data Rendered** | 6,464 Race Results rows, 3,814 Lap Intelligence records, 311 Championship Standings, 29 Circuits. | **PASS** (100% data integrity verified with zero missing rows) |
| **2** | **Data Preprocessing** | Placeholder records (`Driver_2`, `Team_2`) purged; encoding normalized for Hülkenberg; DNF classifications standardized. | **PASS** (Clean dataset loaded into Tableau extract) |
| **3** | **Utilization of Filters** | Multi-dimensional filters: `DNF Reason` (All/Specific), `Year of Race Date` (2010–2026), and `Top N Parameter` (10). | **PASS** (Instant cross-filtering across all 8 dashboard panels $< 150\text{ms}$) |
| **4** | **Calculation Fields Used** | Calculated Fields: Points Summation, Win Conversion %, Podium Conversion %, Tyre Share %, Avg Pit Stop Time, Finish Rate %. | **PASS** (Formulas verified against manual SQL benchmarks) |
| **5** | **Dashboard Design** | **Total Visualizations: 8 Panels**<br>(World Map, Reliability Stacked Bar, Driver Leaderboard, Team Rankings, Championship Standings, Tyre Donut, Country Treemap, Podium Bubble Chart). | **PASS** (High-resolution, zero-crop layout matching reference design) |
| **6** | **Story Design** | **Total Visualizations / Chapters: 7 Story Points**<br>(Global Distribution, Country Participation, Team Championship, Reliability, Podiums, Tyre Share, Team Rankings). | **PASS** (Smooth interactive story transitions with narrative captions) |
| **7** | **Frame Responsiveness** | Aspect ratio preservation, browser window macOS dots, fullscreen trigger, zero horizontal overflow. | **PASS** (Tested across 1080p, 1440p, 4K, and tablet viewports) |
