# 🏎️ FORMULA 1 RACE INTELLIGENCE DASHBOARD
### Enterprise Motorsport Telemetry & Championship Analytics Engine
**Author & Lead Architect:** **Akkshadha Rathore**  
**Tableau Profile:** `Akkshadha rathore`  
**Published Workbook:** `F1 Race Intelligence Dashboard_2`  
**Dashboard Sheet:** `FORMULA 1 RACE INTELLIGENCE DASHBOARD`  
**Story Sheet:** `Formula 1 Race Intelligence: From Global Overview to Championship Success` (9 scenes)  

[![Tableau Live](https://img.shields.io/badge/Tableau-Live_Dashboard-E97627?style=for-the-badge&logo=tableau&logoColor=white)](https://prod-in-a.online.tableau.com/#/site/en25cs3090015-97b3bc9161/views/F1RaceIntelligenceDashboard_2/FORMULA1RACEINTELLIGENCEDASHBOARD?:iid=2)
[![Tableau Story](https://img.shields.io/badge/Tableau_Story-9--Scene_Narrative-22C55E?style=for-the-badge&logo=tableau&logoColor=white)](https://prod-in-a.online.tableau.com/#/site/en25cs3090015-97b3bc9161/views/F1RACEStory/Formula1RaceIntelligenceFromGlobalOverviewtoChampionshipSuccess?:iid=1)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Web_Service-000000?style=for-the-badge&logo=flask&logoColor=white)](https://palletsprojects.com/p/flask/)
[![Theme](https://img.shields.io/badge/Theme-F1_Dark_Obsidian_%26_Crimson-E10600?style=for-the-badge)](#)

---

## 📌 Project Overview

The **Formula 1 Race Intelligence Dashboard** is an enterprise-grade motorsport telemetry and data storytelling platform engineered by **Akkshadha Rathore**. It translates **17 championship seasons (2010–2026)**, **6,464 race outcomes**, and **~13,750 connected data records** into interactive visual intelligence.

Combining **Tableau**'s multi-table logical modeling with an asynchronous **Python Flask** service layer and a broadcast-inspired dark user interface (`#0a0a0f` Obsidian + `#e10600` F1 Crimson), this platform provides team strategists, sports journalists, and racing enthusiasts with instant access to championship trajectories, tyre wear degradation curves, and reliability diagnostics.

---

## 📊 Live Interactive Tableau Workbooks

* 🏁 **Interactive Telemetry Dashboard:**  
  [FORMULA 1 RACE INTELLIGENCE DASHBOARD](https://prod-in-a.online.tableau.com/#/site/en25cs3090015-97b3bc9161/views/F1RaceIntelligenceDashboard_2/FORMULA1RACEINTELLIGENCEDASHBOARD?:iid=2)
* 📖 **9-Scene Championship Narrative Story:**  
  [Formula 1 Race Intelligence: From Global Overview to Championship Success](https://prod-in-a.online.tableau.com/#/site/en25cs3090015-97b3bc9161/views/F1RACEStory/Formula1RaceIntelligenceFromGlobalOverviewtoChampionshipSuccess?:iid=1)

> **💡 Single-Source URL Swapping:**  
> All Tableau embed targets are centralized inside `app.py` under the `CONFIG` dictionary (`TABLEAU_DASHBOARD_URL` and `TABLEAU_STORY_URL`). Updating either variable automatically updates the Jinja2 template, the REST API endpoints, the responsive `<iframe>` containers, and external navigation links across the platform.

---

## 🎯 4 Core Operational KPIs

```
+------------------------------------------------------------------------------------+
| 🏁 Competing Teams: 10              | 📅 Seasons in Play: 17 (2010–2026)           |
+-------------------------------------+----------------------------------------------+
| 🏎️ Race Outcomes Logged: 6,464      | 🌍 Circuits Showcased: 29                    |
+------------------------------------------------------------------------------------+
```

---

## 🔬 5 Core Telemetry Pillars

1. **Global Race Overview:** Multi-season geographic footprint across 29 world circuits, mapping race volumes, track profiles, and continental racing clusters led by Bahrain (2,168 outcomes), the United States (400), Monaco (328), and Spain (328).
2. **Driver Performance Metrics:** Qualifying pace deltas, race pace progression, dynamic Top-N parameter scoring (default: 10), and podium conversion ratios.
3. **Constructor Championship Battle:** Multi-season constructor trajectory highlighting Red Bull Racing (8,006 pts) and Mercedes-AMG (7,790 pts) across hybrid regulations.
4. **Pit Stop & Tyre Strategy Analysis:** Pirelli compound distribution across 4 specifications (Soft 31.52%, Medium 30.78%, Hard 30.36%, Intermediate 7.34%) and stint degradation modeling.
5. **Reliability & DNF Diagnostics:** Failure cause classification (Engine, Collision, Transmission, Suspension, Brakes) and attrition dynamics illustrating modern 91.4% grid completion.

---

## 📈 9 Unique Tableau Visualizations

The published workbook contains 9 distinct, purpose-built visualizations:
1. **KPI Summary Cards:** High-level operational metrics (10 Teams, 17 Seasons, 6,464 Outcomes, 29 Circuits).
2. **Global Driver Distribution Across Grand Prix Nations:** Dark Mapbox geographic projection mapping driver nationalities and racing volumes across 29 host nations.
3. **Driver Reliability Analysis:** Stacked horizontal bar chart colored by `Dnf Reason` (Engine, Collision, Transmission, Suspension, Brakes, Overheating).
4. **Driver Performance Leaderboard:** Dynamic vertical bar chart controlled by the `Top N Parameter` (default: 10), led by Hamilton, Verstappen, Leclerc, and Norris.
5. **Team Performance Ranking:** Horizontal bar chart sorted descending by accumulated constructor points.
6. **Team Championship Performance Analysis:** Vertical grouped bar chart illustrating cyclical constructor dominance across hybrid eras.
7. **Tyre Compound Usage Distribution:** Circular proportion chart detailing Soft (31.52%), Medium (30.78%), Hard (30.36%), and Inter (7.34%) share.
8. **Country-wise Race Participation:** Volume treemap led by Bahrain (2,168), USA (400), Monaco (328), Spain (328), and Brazil (308).
9. **Podium Achievements by Driver and Team:** Packed bubble chart sized by `SUM(Podiums)` comparing top-3 density across constructors.

---

## ⚙️ Interactive Global Controls

* **`Dnf Reason` Filter:** Categorical filter isolating specific attrition causes (Mechanical vs. Accident).
* **`YEAR(Race Date)` Filter:** Continuous timeline slider spanning 17 seasons (2010–2026).
* **`Top N Parameter`:** Integer parameter (range: 5–20, default: 10) dynamically filtering the driver leaderboard.

---

## 🚀 Quickstart & Installation

### Option 1: Flask Production Mode (Recommended)

```bash
# 1. Navigate to project root
cd D:\akk_f1\F1

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Launch Flask server
python app.py
```
Open **`http://127.0.0.1:5000`** in your browser.

### Option 2: Standalone Static Evaluation

Double-click **`index.html`** or open directly in any modern browser without Python dependencies.

---

## 🔌 REST API Endpoints

The Flask application exposes JSON endpoints for telemetry consumption:

| Endpoint | Method | Description |
| :--- | :---: | :--- |
| `/api/health` | `GET` | Health probe verifying application status and author metadata. |
| `/api/config` | `GET` | Active Tableau embed URLs, KPIs, and workbook configuration. |
| `/api/telemetry` | `GET` | Aggregated telemetry summary and dimension indicators. |
| `/api/circuits` | `GET` | All 29 Formula 1 host circuits with metadata. |
| `/api/drivers` | `GET` | Active and historical driver telemetry profiles. |

---

## 📁 Repository Structure

```
.
├── app.py                     # Flask backend application engine & URL configuration
├── templates/
│   └── index.html             # Jinja2 template with dynamic Tableau embedding
├── static/
│   ├── css/style.css          # Dark telemetry stylesheet (Obsidian #0a0a0f & F1 Crimson #e10600)
│   ├── js/script.js           # Interactive controller & dynamic embed formatting
│   ├── js/data.js             # Client-side fallback telemetry dataset
│   ├── assets/                # Visual previews, circuit references, skyline
│   └── data/                  # Telemetry JSON datasets
├── F1 Racing Project Dataset.xlsx # Raw master dataset (5 sheets, ~13.7K rows)
├── index.html                 # Offline standalone distribution
├── PROJECT_DOCUMENTATION.md   # Comprehensive academic project documentation
├── requirements.txt           # Python package requirements
├── run.bat                    # One-click Windows launch script
└── README.md                  # Master repository documentation
```

---

## 📜 Academic Attribution & Notice

Designed and engineered by **Akkshadha Rathore** (`Akkshadha rathore` on Tableau).  
*Notice: This project is an independent academic data visualization deliverable. Formula 1, F1, FIA, and associated trademarks belong to Formula One Licensing B.V. and respective copyright holders.*
