# Project Design Phase
## Project Proposal (Proposed Solution) Template

| Metadata Field | Project Information |
| :--- | :--- |
| **Date** | 15 March 2026 / October 2026 |
| **Author / Team ID** | Akkshadha Rathore |
| **Project Title** | Formula 1 Race Intelligence |
| **Maximum Marks** | 3 Marks |

---

### Project Overview
* **Objective:** To build an authoritative, broadcast-quality Formula 1 Race Intelligence platform that transforms complex multi-season championship datasets (6,464 race outcomes, 3,814 telemetry laps) into interactive Tableau dashboards, real-time visual charts, and a high-performance web terminal.
* **Scope:** Encompasses historical and contemporary hybrid regulation cycles (2010–2026), 10 active constructor teams, 19 elite drivers, 29 world championship circuits, and 5 tire compound strategies.

### Problem Statement & Impact
* **Description:** Motorsport telemetry is traditionally siloed across massive, unwieldy tables with complex join relationships, hindering rapid strategic decision-making and preventing fans and analysts from exploring multi-dimensional race dynamics.
* **Impact:** Eliminates data opacity, shortens strategic analysis cycles from hours to seconds, and bridges the gap between raw engineering telemetry and public data storytelling.

### Proposed Solution & Methodology
* **Approach:** A modular four-tier architecture:
  1. *Ingestion & ETL Tier:* Automated Python ETL pipeline (`process_f1_dataset.py`) parsing raw workbooks and normalizing entity models.
  2. *Data Warehouse & Storage Tier:* Cloud-ready Snowflake schemas and offline-ready `data.js` objects.
  3. *Business Intelligence Tier:* Multi-panel Tableau Public dashboard and narrative story points.
  4. *Presentation & Interaction Tier:* Pure HTML5/CSS3/ES6+ web terminal in a strict Formula 1 Black & Red broadcast design system.
* **Key Features:**
  * Animated start-light gantry sequence ("Lights Out").
  * Animated SVG race circuit with real-time traveling car dot, sector markers, and DRS zone.
  * Infinite-scroll live telemetry marquee ticker.
  * Embedded Tableau Dashboard and Story frames with zero-crop fallbacks.
  * 4 interactive Chart.js graphs and 6 dataset-driven insight cards.
  * Live driver card grid with real-time search, season filters (2010–2026), and sorting.
  * Validated contact terminal with toast notifications.

### Resource Requirements

| Resource Type | Specification / Allocation | Justification |
| :--- | :--- | :--- |
| **Hardware** | Modern Quad-Core CPU, 8 GB+ RAM, 500 MB Storage | Supports smooth local data processing, Chart.js canvas rendering, and 60fps CSS animations. |
| **Software & Frameworks** | Node.js v24+, Python 3.13, OpenPyXL, Pillow, Chart.js 4.4, Font Awesome 6 | Lightweight, robust toolchain requiring zero heavy frontend frameworks (React/Angular). |
| **Data Sources** | `F1 Racing Project Dataset.xlsx` (6,464 rows, 42 columns across 5 sheets) | Real-world historical Grand Prix records, qualifying telemetry, and championship standings. |
| **Personnel** | **Akkshadha Rathore** (Project Lead, Telemetry Engineer & Full-Stack Developer) | End-to-end design, data engineering, UI development, and documentation. |
