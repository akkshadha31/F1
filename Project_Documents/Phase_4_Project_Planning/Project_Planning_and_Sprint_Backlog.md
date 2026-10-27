# Project Planning Phase
## Project Planning Template (Product Backlog, Sprint Planning, Velocity & Burndown)

| Metadata Field | Project Information |
| :--- | :--- |
| **Date** | 18 October 2026 / October 2026 |
| **Author / Team ID** | Akkshadha Rathore |
| **Project Name** | Formula 1 Race Intelligence |
| **Maximum Marks** | 8 Marks |

---

### Product Backlog & Sprint Schedule (4 Marks)

| Sprint | Functional Requirement (Epic) | User Story Number | User Story / Task Description | Story Points | Priority | Owner / Assignee |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| **Sprint-1** | Environment & ETL Ingestion | **USN-01** | Develop Python ETL parser (`process_f1_dataset.py`) to ingest 5 sheets (6,464 race results, 3,814 laps, 29 circuits). | 5 | High | Akkshadha Rathore |
| **Sprint-1** | Data Cleaning & Normalization | **USN-02** | Remove placeholder records (`Driver_2`, `Team_2`), correct encoding artifacts, and compute JSON aggregates. | 3 | High | Akkshadha Rathore |
| **Sprint-1** | Design System & Framework Setup | **USN-03** | Construct strict F1 Black & Red CSS design system (`#0a0a0a`, `#e10600`, Orbitron typography, glow borders). | 5 | High | Akkshadha Rathore |
| **Sprint-1** | Start Sequence & Hero Terminal | **USN-04** | Build F1 5-light start sequence preloader ("Lights Out"), count-up stats strip, and split-tone hero layout. | 5 | High | Akkshadha Rathore |
| **Sprint-1** | Animated Circuit Engine | **USN-05** | Implement hardware-accelerated animated SVG race circuit with traveling car dot, S1–S3 markers, and DRS bar. | 4 | Medium | Akkshadha Rathore |
| **Sprint-2** | Tableau Dashboard Construction | **USN-06** | Model and build 8 core analytical panels in Tableau Public (Leaderboard, Reliability, Map, Tyres, Teams, Podiums). | 6 | High | Akkshadha Rathore |
| **Sprint-2** | Tableau Story Chaptering | **USN-07** | Design 7-point interactive narrative story in Tableau Public and implement browser window frame container. | 5 | High | Akkshadha Rathore |
| **Sprint-2** | Interactive Inline Visualizations | **USN-08** | Implement 4 dynamic Chart.js charts (Leaderboard, Constructor points, Tyre compound share, DNF failure causes). | 5 | High | Akkshadha Rathore |
| **Sprint-3** | Driver Grid Search & Filtering | **USN-09** | Build live driver grid with real-time text search, multi-season dropdown (2010–2026), and sorting algorithms. | 5 | High | Akkshadha Rathore |
| **Sprint-3** | Lightbox Artifact Gallery | **USN-10** | Create masonry artifact gallery with zoom lightbox, keyboard navigation (<kbd>←</kbd> / <kbd>→</kbd> / <kbd>Esc</kbd>), and captions. | 3 | Medium | Akkshadha Rathore |
| **Sprint-3** | Terminal Form Validation & Toast | **USN-11** | Build client-side validated contact terminal with animated transmitting state and green/red toast alerts. | 3 | Medium | Akkshadha Rathore |
| **Sprint-4** | Zero-CORS Offline Optimization | **USN-12** | Compile synchronous `data.js` data store ensuring 100% offline double-click readiness without local server. | 4 | High | Akkshadha Rathore |
| **Sprint-4** | End-to-End Testing & Verification | **USN-13** | Run responsive testing across desktop, tablet, and mobile; verify color contrast ratio $ge 4.5:1$ and Lighthouse $ge 90$. | 4 | High | Akkshadha Rathore |
| **Sprint-4** | Project Documentation & Delivery | **USN-14** | Author complete project documentation, reports, presentation scripts, and README guides. | 3 | High | Akkshadha Rathore |

---

### Project Tracker, Velocity & Burndown (4 Marks)

| Sprint | Total Story Points | Duration | Sprint Start Date | Planned End Date | Points Completed | Actual Release Date | Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Sprint-1** | 22 | 6 Days | 24 Oct 2026 | 29 Oct 2026 | 22 | 29 Oct 2026 | Completed |
| **Sprint-2** | 16 | 6 Days | 31 Oct 2026 | 05 Nov 2026 | 16 | 05 Nov 2026 | Completed |
| **Sprint-3** | 11 | 6 Days | 07 Nov 2026 | 12 Nov 2026 | 11 | 12 Nov 2026 | Completed |
| **Sprint-4** | 11 | 6 Days | 14 Nov 2026 | 19 Nov 2026 | 11 | 19 Nov 2026 | Completed |

#### Velocity Metrics
* **Total Project Story Points:** $60	ext{ Points}$
* **Total Sprints:** $4	ext{ Sprints}$
* **Average Velocity:** $15.0	ext{ Story Points / Sprint}$ (or $2.5	ext{ Points / Day}$)
* **Sprint Completion Rate:** $100%$ on planned milestone timelines.

#### Burndown Tracking
* Day 0: 60 Story Points Remaining
* Day 6 (End of Sprint 1): 38 Story Points Remaining (-22 pts)
* Day 12 (End of Sprint 2): 22 Story Points Remaining (-16 pts)
* Day 18 (End of Sprint 3): 11 Story Points Remaining (-11 pts)
* Day 24 (End of Sprint 4): 0 Story Points Remaining (-11 pts, Complete Delivery)
