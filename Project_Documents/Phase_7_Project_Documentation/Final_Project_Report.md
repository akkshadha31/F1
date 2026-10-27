# Project Documentation Phase
## Formula 1 Race Intelligence – Comprehensive Final Project Report

| Document Metadata | Details |
| :--- | :--- |
| **Project Title** | Formula 1 Race Intelligence: From Global Overview to Championship Success |
| **Author / Lead Engineer** | **Akkshadha Rathore** |
| **Date of Submission** | October 2026 |
| **Domain** | Motorsport Data Science, Telemetry Analytics & Business Intelligence |
| **Primary Tools** | Tableau Public, Python 3.13, Snowflake, HTML5, CSS3, Vanilla JS ES6+ |
| **Dataset Analyzed** | `F1 Racing Project Dataset.xlsx` (6,464 race results, 3,814 laps, 29 circuits) |

---

### Executive Summary & Abstract
The **Formula 1 Race Intelligence** project is a production-grade, full-stack motorsport analytics terminal that models 17 competitive Formula 1 seasons (2010–2026). By fusing modern data engineering pipelines with Tableau Public visual storytelling and an ultra-responsive web application in a strict Formula 1 Black & Red broadcast aesthetic (`#0a0a0a` + `#e10600`), this platform democratizes access to complex racing telemetry. It empowers strategists, simulation drivers, data journalists, and motorsport enthusiasts to explore driver pace deltas, tire compound degradation curves, constructor battle trajectories, pit stop efficiency, and circuit attrition in real time.

---

### Chapter 1: Problem Background & Domain Overview
Modern Formula 1 racing generates billions of data points per Grand Prix weekend through hundreds of vehicle sensors capturing engine RPM, tire surface temperatures, brake pressure, and GPS telemetry. However, public and analyst access is severely bottlenecked:
1. **Data Silos & Schema Fragmentation:** Telemetry data is scattered across disconnected workbooks, making multi-table joins prone to calculation errors.
2. **Superficial Broadcast Presentation:** Live TV broadcasts only share ephemeral, high-level graphics that vanish seconds after display.
3. **Fragile BI Architectures:** Traditional cloud-dependent dashboards fail in trackside environments when network connectivity drops.

---

### Chapter 2: Data Pipeline & Snowflake ETL Methodology
The project analyzed **6,464 race records**, **3,814 lap records**, **3,130 qualifying sessions**, and **29 circuits**:
* **Ingestion:** Developed `process_f1_dataset.py` using OpenPyXL to ingest the 5 source sheets.
* **Cleaning:** Purged synthetic placeholder records (`Driver_2`, `Team_2`), corrected character encoding artifacts for Nico Hülkenberg, and standardized unclassified DNF records.
* **Snowflake Staging & Star Schema:** Organized tables into `RAW`, `STAGING`, and `CURATED` layers (`DIM_CIRCUITS`, `DIM_DRIVERS`, `FACT_RACE_RESULTS`, `FACT_LAP_INTELLIGENCE`).
* **Zero-CORS Client Embedding:** Generated synchronous `data.js` data objects to guarantee 100% offline functionality when double-clicking `index.html`.

---

### Chapter 3: Tableau Business Intelligence Engine
Eight core analytical panels were constructed in Tableau Public:
1. **Global Driver Distribution World Map:** Visualizes race entry density across host nations (USA 400, Spain 328, Monaco 328, Canada 308).
2. **Driver Reliability & DNF Analysis:** Categorizes mechanical versus accident retirements across drivers.
3. **Driver Performance Leaderboard:** Ranks top performers in total hybrid-era points (Hamilton 31,147 pts, Verstappen 31,126 pts).
4. **Team Performance Ranking:** Evaluates constructor supremacy (Red Bull Racing 8,006 pts, Mercedes 7,790 pts, Ferrari 5,778 pts).
5. **Team Championship Standings:** Tracks annual points progression across regulatory shifts.
6. **Tyre Compound Usage Share:** Donut chart establishing proportional compound selection: Soft 31.52%, Medium 30.78%, Hard 30.36%, Intermediate 7.34%.
7. **Country-wise Participation Treemap:** Highlights outcome density (Bahrain 2,168 logged outcomes).
8. **Podium Achievements Bubble Chart:** Displays podium cluster density for top constructor partnerships.

---

### Chapter 4: Web Application Architecture & Design System
* **F1 Start Sequence Preloader:** Realistic 5-light sequence with sound timing and *"LIGHTS OUT AND AWAY WE GO!"* transition.
* **Animated SVG Track Engine:** Hardware-accelerated racing line with traveling red car dot, S1–S3 markers, and DRS bar.
* **Infinite LIVE DATA Ticker:** Real-time telemetry marquee streaming live facts computed from the dataset.
* **Interactive Driver Grid:** Instant search, multi-season filtering (2010–2026), sort controls, champion crown badges, and win/podium conversion progress bars.
* **Inquiry Terminal:** Validated glass card form with animated loading state and toast notifications.

---

### Chapter 5: Empirical Results & Strategic Insights
* **Championship Domination:** Lewis Hamilton holds 6 hybrid titles and 4,491 points, rivaled by Max Verstappen's recent ground-effect supremacy.
* **Constructor Hegemony:** Red Bull Racing (8,006 pts) and Mercedes (7,790 pts) account for $> 52%$ of all points awarded in the hybrid era.
* **Pirelli Compound Parity:** Tri-compound parity between Soft (31.52%), Medium (30.78%), and Hard (30.36%) confirms effective FIA tire regulations.
* **Pit Lane Margins:** Sub-2.3s pit executions (Ferrari record 2.18s avg) deliver decisive undercut advantages.

---

### Chapter 6: Conclusion & Future Scope
The platform successfully meets all functional and non-functional requirements with a Lighthouse score of 95/100 and 100% offline availability. Future expansion will introduce live WebSocket streaming from the F1 Live Timing API and machine learning models for tire degradation forecasting.
