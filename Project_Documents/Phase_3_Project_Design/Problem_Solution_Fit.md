# Project Design Phase
## Problem – Solution Fit Template

| Metadata Field | Project Information |
| :--- | :--- |
| **Date** | 19 September 2026 / October 2026 |
| **Author / Team ID** | Akkshadha Rathore |
| **Project Name** | Formula 1 Race Intelligence |
| **Maximum Marks** | 2 Marks |

---

### Problem – Solution Fit Analysis
Confirming that every identified customer problem is directly solved by an implemented platform capability:

| Customer Problem & Friction Point | Behavioral Pattern & Root Cause | Implemented Solution Feature | Measurable Outcome & Fit Validation |
| :--- | :--- | :--- | :--- |
| **1. Disjointed Telemetry Data:** Analysts must merge 5 Excel sheets manually to correlate lap pace with tire degradation. | Analysts work across fragmented spreadsheets, causing calculation errors and delayed race strategy decisions. | **Unified Python ETL & Curated Data Pipeline:** Harmonizes 6,464 race records, 3,814 lap records, and 29 circuits into a single schema. | Data retrieval latency reduced from 45 minutes to $< 100\text{ms}$; zero calculation errors across metrics. |
| **2. Lack of Visual Tire Analytics:** Teams cannot easily visualize how tire compounds degrade across stints. | Raw tables list tire compounds as text without visual proportion or degradation trend indicators. | **Pirelli Compound Matrix & Doughnut Visual:** Displays exact compound utilization (Soft 31.52%, Medium 30.78%, Hard 30.36%, Inter 7.34%). | Immediate visual clarity on compound crossover thresholds and optimal qualifying/race stint allocations. |
| **3. Superficial Broadcast Graphics:** Fans and journalists only see high-level TV banners without career historical depth. | Broadcast graphics are transient and offer no historical teammate filtering or multi-season trend exploration. | **Multi-Season Driver Telemetry Grid & Search:** Filterable cards with season dropdowns (2010–2026), search, and win/podium rate bars. | Self-guided exploration for all 19 drivers; instant comparison between Hamilton (31,147 pts) and Verstappen (31,126 pts). |
| **4. Inflexible BI Deployment:** Cloud-only dashboards break during offline briefings or when firewalls block embeds. | Telemetry analysts often present in trackside hospitality suites with unstable internet connectivity. | **Dual-Engine Architecture:** Tableau Public cloud embed paired with 100% offline-ready `data.js` and local double-click execution. | 100% platform availability online and offline; zero dependency on external network servers. |
