# Project Demonstration Phase
## Demonstration of Proposed Features

| Metadata Field | Project Information |
| :--- | :--- |
| **Date** | October 2026 |
| **Author / Presenter** | **Akkshadha Rathore** |
| **Project Name** | Formula 1 Race Intelligence |
| **Deliverable** | Feature Demonstration Script & Validation |

---

### Step-by-Step Feature Walkthrough

| Feature Module | Demonstration Action | Expected Visual & Functional Response | Validation Check |
| :--- | :--- | :--- | :---: |
| **1. F1 Start Sequence Preloader** | Refresh page or access `index.html`. | 5 red lights illuminate sequentially with 320ms intervals; status changes to *"FORMATION LAP COMPLETE"*; brief suspense pause; all 5 turn off simultaneously with *"LIGHTS OUT AND AWAY WE GO!"* before fading into hero. | **PASS** |
| **2. Hero Telemetry & Count-Up** | Scroll into Hero section. | Live pulsing red beacon glows; stats strip numbers count up smoothly from 0 to target values (`75+`, `1K+`, `20`, `10`); split-tone Moscow skyline blends seamlessly. | **PASS** |
| **3. Animated Vector Circuit** | Scroll to Project Overview (`#project`). | Dark circuit card renders dashed red racing line; glowing red car dot moves smoothly along path; S1, S2, S3 dots and green DRS bar display crisp contrast. | **PASS** |
| **4. Live Marquee Ticker** | Inspect Live Data bar in Dimensions (`#insights`). | Ticker smoothly scrolls empirical facts (Verstappen 4,640 pts, Monaco 1:12.492, Ferrari 2.18s pit stop); pauses on mouse hover. | **PASS** |
| **5. Tableau Dashboard Frame** | Click `[VIEW DASHBOARD]` or navigate to `#dashboard`. | macOS window frame displays 8-panel high-res dashboard preview with zero cropping; KPI summary strip shows 10 Teams, 17 Seasons, 6,464 Outcomes, 29 Circuits; `[Open full screen ↗]` triggers native fullscreen. | **PASS** |
| **6. Interactive Story Chapters** | Navigate to `#story` and click chips 1 through 7. | Clicking chips (e.g., Chip 6: Tyre Compound Usage) dynamically updates the caption below to display exact compound metrics (Soft 31.52%, Medium 30.78%, Hard 30.36%). | **PASS** |
| **7. Inline Chart.js Charts** | Inspect Key Findings (`#insights-data`). | 4 interactive charts animate into view; hovering shows dark-themed tooltips with precise points and percentage values. | **PASS** |
| **8. Driver Search & Season Filter** | Type "Lewis" in search box; change season to "2024". | Grid instantly filters to Lewis Hamilton; stats update to show 2024 season metrics (233 pts, 3 wins, 7 podiums); progress bars reflect 2024 conversion rates. | **PASS** |
| **9. Lightbox Artifact Gallery** | Click any card in Telemetry Gallery (`#gallery`). | Modal opens with enlarged high-res capture; arrow keys (<kbd>←</kbd> / <kbd>→</kbd>) cycle images; <kbd>Esc</kbd> closes modal. | **PASS** |
| **10. Terminal Form & Toast** | Submit valid contact details in Terminal (`#contact`). | Button enters loading state (*"TRANSMITTING..."*); green toast alert appears with confirmation message; form automatically resets. | **PASS** |
