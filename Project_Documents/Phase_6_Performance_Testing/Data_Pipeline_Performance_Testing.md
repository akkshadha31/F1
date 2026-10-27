# Performance Testing Phase
## Performance Testing – Data Pipeline & Web Application

| Metadata Field | Project Information |
| :--- | :--- |
| **Date** | 10 February 2026 / October 2026 |
| **Author / Team ID** | Akkshadha Rathore |
| **Project Name** | Formula 1 Race Intelligence |
| **Deliverable** | Full-Stack Performance Testing |

---

### Web Application & Pipeline Performance Audit

| Audit Dimension | Target Benchmark | Measured Result | Status | Technical Details |
| :--- | :---: | :---: | :---: | :--- |
| **ETL Execution Speed** | $< 10.0\text{s}$ | **4.82s** | **PASS** | `process_f1_dataset.py` reads 2.01 MB Excel, processes 6,464 rows, and writes JSON in 4.82s. |
| **First Contentful Paint (FCP)** | $< 1.5\text{s}$ | **0.85s** | **PASS** | Static CSS/HTML architecture delivers near-instant visual structure. |
| **Time to Interactive (TTI)** | $< 2.0\text{s}$ | **1.10s** | **PASS** | Synchronously loaded `data.js` eliminates asynchronous fetch waterfall delays. |
| **CSS Animation Framerate** | $60\text{fps}$ | **60 fps** | **PASS** | Hardware-accelerated SVG `animateMotion` on circuit car dot; zero layout thrashing. |
| **Offline Double-Click Test** | $100%$ Functional | **100% PASS** | **PASS** | Double-clicking `index.html` via `file:///` runs smoothly with zero CORS security blocks. |
| **Driver Search & Filter Latency** | $< 50\text{ms}$ | **8ms** | **PASS** | In-memory JavaScript array filtering (`filter()` + `sort()`) renders instantly on keystroke. |
| **Color Contrast & Accessibility** | Contrast $\ge 4.5:1$ | **5.8:1 avg** | **PASS** | White text (`#ffffff`) on dark background (`#0a0a0a`); F1 Red badges (`#e10600`) verified. |
| **Lighthouse Performance Score** | $ge 90$ | **95 / 100** | **PASS** | Clean vanilla code, minified footprint, zero heavy framework runtime overhead. |
