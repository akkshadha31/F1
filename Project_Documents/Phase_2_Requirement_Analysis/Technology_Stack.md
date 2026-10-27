# Requirement Analysis Phase
## Technology Stack (Architecture & Stack)

| Metadata Field | Project Information |
| :--- | :--- |
| **Date** | 31 January 2026 / October 2026 |
| **Author / Team ID** | Akkshadha Rathore |
| **Project Name** | Formula 1 Race Intelligence |
| **Maximum Marks** | 2 Marks |

---

### Defined Technology Stack

| S.No | Component | Description | Technology Selected | Justification / Architectural Purpose |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Programming & Scripting** | Languages used to parse, transform, clean, and visualize data. | Python 3.13, JavaScript (ES6+), HTML5, CSS3 | Python provides robust data manipulation via OpenPyXL and Pillow; ES6+ powers responsive client interactivity; HTML5/CSS3 deliver hardware-accelerated broadcast graphics. |
| **2** | **Database & Data Store** | Engine used to organize, query, and serve structured telemetry. | Snowflake Data Warehouse / Local JSON Store (`data.js`) | Snowflake provides scalable cloud-based SQL modeling with RAW, STAGING, and CURATED layers; `data.js` embeds cleaned datasets locally for offline zero-CORS double-click execution. |
| **3** | **Data Ingestion & ETL** | Tools used to extract and load data from source workbooks. | Python ETL Pipeline (`process_f1_dataset.py`) / Snowflake Stages | Automates extraction of 6,464 race records and 3,814 telemetry laps, filters placeholder strings, and outputs clean normalized JSON schemas. |
| **4** | **Data Transformation & Logic** | Business calculations, aggregations, and KPI formulas. | Python / Snowflake SQL / Tableau Desktop | Calculates career points, win/podium conversion percentages, Pirelli tire compound share ratios, and pit stop consistency statistics. |
| **5** | **Data Visualization** | Engines used to create interactive charts, graphs, and stories. | Tableau Public & Chart.js 4.4 | Tableau Public hosts the full 8-panel dashboard and narrative story; Chart.js provides animated, high-speed inline bar, doughnut, and stacked charts directly in the browser. |
| **6** | **Front-End User Interface** | Client interface through which users explore telemetry. | Custom F1 Web Interface (HTML5, CSS3, Font Awesome 6, Google Orbitron) | Recreates the reference broadcast design with F1 start-light preloader, animated SVG circuit, live ticker marquee, driver filter controls, and lightbox gallery. |
| **7** | **Version Control & Hosting** | Source code management and deployment environment. | Git, GitHub, Local Python HTTP Server (Port 3000) | Ensures reproducible version tracking and provides a lightweight background daemon server for instant browser previewing. |
