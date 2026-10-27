# Requirement Analysis Phase
## Solution Requirements (Functional & Non-Functional)

| Metadata Field | Project Information |
| :--- | :--- |
| **Date** | 31 January 2026 / October 2026 |
| **Author / Team ID** | Akkshadha Rathore |
| **Project Name** | Formula 1 Race Intelligence |
| **Maximum Marks** | 4 Marks |

---

### Functional Requirements (FR)

| FR No. | Functional Epic | Sub-Requirement / Specification | Priority |
| :---: | :--- | :--- | :---: |
| **FR-1** | Data Access & Integration | Ingest, parse, and harmonize all 5 sheets from `F1 Racing Project Dataset.xlsx` (`circuits`, `championship_standings`, `lap_intelligence`, `qualifying_results`, `race_results`) encompassing 6,464 race outcome rows. | High |
| **FR-2** | Data Processing & Cleansing | Clean encoding artifacts (e.g., Hülkenberg), filter placeholder entries (`Driver_2`, `Team_2`), resolve join fan-outs, and normalize team branding across regulation cycles. | High |
| **FR-3** | Telemetry & KPI Calculations | Calculate macro KPIs (10 Teams, 17 Seasons, 6,464 Outcomes, 29 Circuits), career points totals, win conversion rates, podium conversion rates, and average pit stop speeds. | High |
| **FR-4** | Interactive Visualizations | Render 4 dynamic Chart.js visualizations (Driver Leaderboard, Team Rankings, Tire Compound Share, DNF Reliability) with responsive scaling and custom tooltips. | High |
| **FR-5** | Tableau Public Integration | Provide official embed containers for Tableau Public Dashboard and Story views, accompanied by full-resolution fallback previews and fullscreen modal expanders. | High |
| **FR-6** | User Search, Filter & Sort | Support real-time driver search, multi-season filtering (2010–2026 or Career), and multi-attribute sorting (points, wins, podiums, poles, least DNFs). | High |
| **FR-7** | Interactive Story Navigator | Equip Tableau Story section with 7 clickable chapter chips (1 to 7) that dynamically update narrative commentary and context. | Medium |
| **FR-8** | Terminal Inquiry & Toast | Deliver client-side validated contact form with real-time feedback and animated green/red toast notification upon submission. | Medium |

---

### Non-Functional Requirements (NFR)

| NFR No. | Requirement Category | Detailed Technical Specification |
| :---: | :--- | :--- |
| **NFR-1** | **Usability & UX** | Strict Formula 1 Black & Red broadcast aesthetic (`--bg: #0a0a0a`, `--red: #e10600`, `--card: #151515`), glowing borders, Orbitron typography, and minimum contrast ratio $\ge 4.5:1$. |
| **NFR-2** | **Performance & Speed** | First Contentful Paint (FCP) $< 1.2\text{s}$, smooth 60fps animations, lazy-loaded visual assets, and Lighthouse performance rating $\ge 90$. |
| **NFR-3** | **Reliability & Offline Execution** | 100% offline runnable by simply double-clicking `index.html` via pre-compiled `data.js` object, avoiding cross-origin `file://` CORS restrictions. |
| **NFR-4** | **Responsiveness & Cross-Platform** | Fully responsive layout spanning ultra-wide desktops ($1920\text{px}+$), standard laptops, tablets, and mobile smartphones with slide-out hamburger navigation. |
| **NFR-5** | **Security & Client Integrity** | Client-side input sanitization on all form fields, secure CDN asset delivery via HTTPS, and no exposure of backend credentials. |
| **NFR-6** | **Maintainability & Extensibility** | Modular codebase with separated concerns (`index.html`, `style.css`, `script.js`, `data.js`, `data/`), extensive code comments, and configurable Tableau URL constants. |
