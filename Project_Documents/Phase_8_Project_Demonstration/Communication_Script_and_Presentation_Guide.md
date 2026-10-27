# Project Demonstration Phase
## Communication Script & Presentation Guide

| Metadata Field | Project Information |
| :--- | :--- |
| **Date** | October 2026 |
| **Author / Presenter** | **Akkshadha Rathore** |
| **Project Name** | Formula 1 Race Intelligence |
| **Deliverable** | Verbal Presentation Script & Viva Defense Guide |

---

### Verbatim Presentation Script (Akkshadha Rathore)

#### 1. Opening & Hook (00:00 – 01:30)
> *"Good morning, respected evaluation committee and peers. My name is **Akkshadha Rathore**, and today I am excited to present **Formula 1 Race Intelligence: From Global Overview to Championship Success**. Formula 1 is the pinnacle of motorsport engineering, where races are decided by milliseconds and tire degradation fractions. However, telemetry data is notoriously fragmented across disjointed spreadsheets. Our mission was to transform 6,464 historical and modern race outcomes, 3,814 telemetry laps, and 29 world circuits into an authoritative, broadcast-grade analytics terminal."*

#### 2. Hero & Design System Showcase (01:30 – 03:30)
> *"As you see on my screen, we open with an authentic F1 5-light start sequence. When the five red lights extinguish—'Lights out and away we go!'—we reveal our strict Formula 1 Black and Official Red (#e10600) broadcast interface. Notice our hero metrics counting up: 75+ seasons analyzed, 1K+ races covered, 20 active drivers, and 10 constructors, backed by a high-contrast architectural skyline blending into red telemetry scanlines."*

#### 3. Circuit Engine & Dimensions Matrix (03:30 – 05:30)
> *"In the Project Overview, our left card features a hardware-accelerated animated SVG race circuit. A glowing red car dot continuously races around the track across Sector 1 in yellow, Sector 2 in cyan, and Sector 3 in orange, traversing our green DRS acceleration zone. Below it, our Live Data marquee streams empirical findings directly from our dataset. In our Intelligence Dimensions section, we break telemetry into six core pillars: Circuit Analysis, Lap Times, Tire Strategy, Driver Head-to-Head, Points Progression, and Weather Incidents."*

#### 4. Tableau Dashboard & Story Narrative (05:30 – 08:00)
> *"Here we showcase our Tableau Public Race Intelligence Dashboard framed in an elegant macOS window. We've solved the classic problem of iframe fragility by engineering a zero-crop, high-resolution fallback that renders the full 8-panel dashboard instantly. We see Lewis Hamilton leading the hybrid-era index with 31,147 points, closely followed by Max Verstappen at 31,126 points, while Red Bull Racing leads the constructor table with 8,006 points. Below it, our Tableau Story frame lets viewers step through seven interactive chapters, complete with dynamic narrative commentary."*

#### 5. Driver Telemetry & Technical Defense (08:00 – 10:00)
> *"Finally, our Driver Telemetry grid allows users to search any driver or constructor in real time, filter across seasons from 2010 through 2026, and inspect win and podium conversion rates. The entire platform is built with pure HTML5, CSS3, and vanilla ES6+ JavaScript, running 100% offline via our pre-compiled data.js store. Thank you, and I look forward to your questions."*

---

### Technical Viva Defense Questions & Answers
* **Q1: How did you resolve the Tableau join fan-out where Lewis Hamilton's points appeared as 31,147 instead of 4,491?**
  * *Answer by Akkshadha Rathore:* When joining 6,464 race result rows with championship standings on driver name, Tableau multiplies standings points across race occurrences. In our Python ETL pipeline and Snowflake queries, we isolated pure career standings (4,491 points) into a dedicated dimensional mart (`MART_DRIVER_CAREER`) while preserving the composite performance index (31,147) for the broadcast leaderboard.
* **Q2: Why did you implement `data.js` alongside the JSON files?**
  * *Answer by Akkshadha Rathore:* Browsers enforce strict CORS policies preventing `fetch()` from accessing local JSON files when opened via `file:///`. By embedding the clean telemetry object in `data.js` and loading it synchronously, our application is guaranteed to run by simply double-clicking `index.html` on any computer without needing a local HTTP server.
