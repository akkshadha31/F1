# Project Design Phase
## Solution Architecture

| Metadata Field | Project Information |
| :--- | :--- |
| **Date** | 19 September 2026 / October 2026 |
| **Author / Team ID** | Akkshadha Rathore |
| **Project Name** | Formula 1 Race Intelligence |
| **Maximum Marks** | 4 Marks |

---

### High-Level Architecture Overview
The **Formula 1 Race Intelligence** platform employs a decoupled, high-performance data architecture separating raw ingestion, analytical data warehousing, visualization modeling, and client presentation.

```mermaid
flowchart TD
    subgraph Data_Layer["1. Data Ingestion & Storage Layer"]
        XLSX["F1 Racing Project Dataset.xlsx (5 Sheets)"] --> ETL["Python ETL Pipeline (process_f1_dataset.py)"]
        ETL --> SF_RAW["Snowflake RAW / Staging Tables"]
        ETL --> JSON_Store["data.js / data/*.json Store"]
    end

    subgraph Analytics_Layer["2. Business Intelligence & Modeling Layer"]
        SF_RAW --> SF_MART["Snowflake CURATED / Analytics Mart"]
        SF_MART --> Tableau_Desktop["Tableau Desktop Modeling"]
        Tableau_Desktop --> Tableau_Public["Tableau Public Server (Dashboard & Story)"]
    end

    subgraph Presentation_Layer["3. Front-End Web Application Layer"]
        JSON_Store --> Web_App["Formula 1 Web Engine (index.html, script.js)"]
        Tableau_Public --> Web_App
        Web_App --> UI_Hero["Hero Experience & F1 Start Lights"]
        Web_App --> UI_SVG["Animated SVG Circuit & Telemetry Tags"]
        Web_App --> UI_Ticker["Infinite LIVE DATA Marquee Ticker"]
        Web_App --> UI_Dashboard["Embedded Tableau Dashboard Frame"]
        Web_App --> UI_Story["Embedded Tableau Story Frame + Navigator"]
        Web_App --> UI_Charts["Chart.js Telemetry Visualizations (4 Charts)"]
        Web_App --> UI_Drivers["Driver Grid & Search / Season Filter Engine"]
        Web_App --> UI_Contact["Contact Terminal with Validation & Toast"]
    end
```

---

### Component Description Table

| Component Name | Description / Role in Architecture | Technology Used |
| :--- | :--- | :--- |
| **Source Workbook** | Primary historical repository comprising 6,464 race outcomes, 3,814 telemetry laps, 3,130 qualifying records, 311 standings, and 29 circuits. | Microsoft Excel (.xlsx) |
| **ETL Pipeline** | Automated Python pipeline that reads openpyxl workbooks, cleans encoding anomalies, filters synthetic placeholders, and outputs normalized JSON. | Python 3.13, OpenPyXL |
| **Data Warehouse** | Multi-tier cloud data warehouse structuring RAW ingestion tables, normalized STAGING views, and CURATED reporting marts. | Snowflake Cloud DW / SQL |
| **Offline Data Store** | Synchronously loaded JavaScript data object providing zero-CORS offline execution when double-clicking `index.html`. | Vanilla JavaScript (`data.js`) |
| **Tableau BI Engine** | Cloud-hosted multi-panel dashboard and narrative story points delivering deep-dive visual analytics. | Tableau Public Embed API / iFrame |
| **Inline Visual Engine** | Client-side canvas charting rendering high-speed bar, doughnut, and stacked failure charts. | Chart.js 4.4 |
| **Vector Animation Engine** | Hardware-accelerated SVG circuit mapping with traveling red car dot, S1–S3 sector marks, and DRS straight bar. | Pure SVG & CSS Keyframes |
| **Web Presentation Engine** | Semantic HTML5 single-page application styled in strict F1 Black & Red broadcast theme (`#0a0a0a` + `#e10600`). | HTML5, CSS3, Vanilla JS ES6+ |
