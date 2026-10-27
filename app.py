"""
Formula 1 Race Intelligence Dashboard - Flask Application Engine
================================================================
Author / Lead Developer: Akkshadha Rathore
Tableau Profile         : Akkshadha rathore
Published Workbook      : F1 Race Intelligence Dashboard_2
Championship Story      : Formula 1 Race Intelligence: From Global Overview to Championship Success

This module serves the interactive Formula 1 Race Intelligence web application,
providing dynamic rendering of the dark telemetry interface, embedded Tableau
visualizations, and RESTful telemetry data endpoints.
"""

import os
import json
from flask import Flask, render_template, jsonify, send_from_directory, request

# Base directory paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Initialize Flask application
app = Flask(
    __name__,
    template_folder=TEMPLATES_DIR if os.path.exists(TEMPLATES_DIR) else BASE_DIR,
    static_folder=STATIC_DIR if os.path.exists(STATIC_DIR) else BASE_DIR,
    static_url_path='/static'
)

# ==============================================================================
# CONFIGURATION SETTINGS & TABLEAU WORKBOOK URLS
# ==============================================================================
CONFIG = {
    "AUTHOR_NAME": "Akkshadha Rathore",
    "AUTHOR_HANDLE": "Akkshadha rathore",
    "WORKBOOK_NAME": "F1 Race Intelligence Dashboard_2",
    "DASHBOARD_SHEET": "FORMULA 1 RACE INTELLIGENCE DASHBOARD",
    "STORY_SHEET": "Formula 1 Race Intelligence: From Global Overview to Championship Success",
    
    # Primary Interactive Tableau URLs
    "TABLEAU_DASHBOARD_URL": "https://prod-in-a.online.tableau.com/#/site/en25cs3090015-97b3bc9161/views/F1RaceIntelligenceDashboard_2/FORMULA1RACEINTELLIGENCEDASHBOARD?:iid=2",
    "TABLEAU_STORY_URL": "https://prod-in-a.online.tableau.com/#/site/en25cs3090015-97b3bc9161/views/F1RACEStory/Formula1RaceIntelligenceFromGlobalOverviewtoChampionshipSuccess?:iid=1",
    
    # 4 Core KPI Ground Truth
    "KPIS": {
        "competing_teams": 10,
        "seasons_in_play": 17,
        "race_outcomes_logged": 6464,
        "circuits_showcased": 29
    },
    
    # Analytical Dimensions
    "DIMENSIONS": [
        {
            "id": "circuits",
            "title": "Circuit Analysis",
            "icon": "fa-solid fa-map-location-dot",
            "desc": "Geographic and telemetry track profiling across 29 host circuits worldwide, contrasting high-downforce street layouts with high-speed power circuits.",
            "stat": "→ 29 HOST CIRCUITS MAPPED"
        },
        {
            "id": "lap_time",
            "title": "Lap Time Breakdown",
            "icon": "fa-solid fa-stopwatch-20",
            "desc": "Microsecond-precision telemetry breaking down Sector 1, Sector 2, and Sector 3 splits, apex cornering speeds, and qualifying delta margins.",
            "stat": "→ MILLISECOND DELTA TELEMETRY"
        },
        {
            "id": "tyre_strategy",
            "title": "Tyre Strategy",
            "icon": "fa-solid fa-circle-notch",
            "desc": "Compound degradation curves and allocation share across 4 Pirelli compounds: Soft (31.52%), Medium (30.78%), Hard (30.36%), and Inter (7.34%).",
            "stat": "→ 4 PIRELLI COMPOUNDS IN PLAY"
        },
        {
            "id": "driver_h2h",
            "title": "Driver Head-to-Head",
            "icon": "fa-solid fa-user-ninja",
            "desc": "Dynamic Top-N parameter ranking allowing real-time comparison of qualifying pace deltas, podium counts, and point progression across the modern grid.",
            "stat": "→ TOP N DYNAMIC FILTERING"
        },
        {
            "id": "points_progression",
            "title": "Points Progression",
            "icon": "fa-solid fa-arrow-trend-up",
            "desc": "Championship point curves tracking Red Bull Racing (8,006 pts) and Mercedes-AMG (7,790 pts) across 17 competitive seasons (2010–2026).",
            "stat": "→ 17 SEASONS (2010–2026)"
        },
        {
            "id": "reliability",
            "title": "Weather & Safety Cars",
            "icon": "fa-solid fa-triangle-exclamation",
            "desc": "DNF attrition diagnostics categorizing power unit, collision, transmission, and brake failures, benchmarking modern 91.4% grid completion.",
            "stat": "→ DNF REASON & ATTRITION DIAGNOSTICS"
        }
    ],
    
    # 9 Tableau Story Scenes
    "STORY_SCENES": [
        {"id": 1, "title": "KPI Summary Cards", "summary": "Core telemetry foundation indexing 10 Competing Teams, 17 Seasons, 6,464 Outcomes, and 29 Circuits."},
        {"id": 2, "title": "Global Driver Distribution", "summary": "Dark Mapbox geographic projection mapping driver nationalities and racing volumes across 29 Grand Prix nations."},
        {"id": 3, "title": "Country-wise Race Participation", "summary": "Participation volume treemap led by Bahrain (2,168 outcomes), United States (400), Monaco (328), Spain (328), and Brazil (308)."},
        {"id": 4, "title": "Team Championship Performance", "summary": "Vertical bar chart tracking constructor championship hauls across hybrid engine regulations."},
        {"id": 5, "title": "Driver Reliability Analysis", "summary": "Stacked bar chart colored by DNF Reason (Engine, Collision, Transmission, Suspension, Brakes) detailing attrition."},
        {"id": 6, "title": "Driver Performance Leaderboard", "summary": "Dynamic Top-N vertical bar chart driven by Top N Parameter (Hamilton, Verstappen, Leclerc, Norris, Alonso)."},
        {"id": 7, "title": "Podium Achievements", "summary": "Packed bubble visualization sized by SUM(Podiums) contrasting driver and constructor top-3 cluster density."},
        {"id": 8, "title": "Tyre Compound Usage", "summary": "Pirelli compound distribution pie chart showing Soft (31.52%), Medium (30.78%), Hard (30.36%), and Inter (7.34%)."},
        {"id": 9, "title": "Team Performance Ranking", "summary": "Horizontal bar chart ranking all 10 constructors sorted descending by total accumulated points."}
    ]
}


def get_tableau_embed_url(url):
    """
    Intelligently formats a Tableau interactive URL into an iframe-compatible embed URL.
    Handles Tableau Cloud/Server (/#/site/ -> /t/) and Tableau Public URL structures.
    """
    if not url:
        return ""
    clean_url = url.split("?")[0].rstrip("/")
    if "/#/site/" in clean_url:
        clean_url = clean_url.replace("/#/site/", "/t/")
    return f"{clean_url}?:embed=yes&:showVizHome=no&:toolbar=yes&:tabs=no&:showAppBanner=false"


def load_json_file(filename):
    """Safely load JSON data from data directory or return empty dict."""
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            app.logger.error(f"Error loading {filename}: {e}")
    return {}


# Pre-load telemetry data
CIRCUITS_DATA = load_json_file('circuits.json')
DRIVERS_DATA = load_json_file('drivers.json')
INTELLIGENCE_DATA = load_json_file('f1_intelligence.json')
INSIGHTS_DATA = load_json_file('insights.json')


# ==============================================================================
# WEB ROUTES
# ==============================================================================

@app.route('/')
def index():
    """Render the primary Formula 1 Race Intelligence Dashboard."""
    dashboard_embed = get_tableau_embed_url(CONFIG["TABLEAU_DASHBOARD_URL"])
    story_embed = get_tableau_embed_url(CONFIG["TABLEAU_STORY_URL"])
    
    return render_template(
        'index.html',
        author_name=CONFIG["AUTHOR_NAME"],
        author_handle=CONFIG["AUTHOR_HANDLE"],
        workbook_name=CONFIG["WORKBOOK_NAME"],
        tableau_dashboard_url=CONFIG["TABLEAU_DASHBOARD_URL"],
        tableau_story_url=CONFIG["TABLEAU_STORY_URL"],
        tableau_dashboard_embed_url=dashboard_embed,
        tableau_story_embed_url=story_embed,
        kpis=CONFIG["KPIS"],
        dimensions=CONFIG["DIMENSIONS"],
        story_scenes=CONFIG["STORY_SCENES"]
    )


# ==============================================================================
# REST API ENDPOINTS
# ==============================================================================

@app.route('/api/config', methods=['GET'])
def get_config():
    """Return dashboard configuration and live Tableau URLs."""
    return jsonify({
        "status": "success",
        "author": CONFIG["AUTHOR_NAME"],
        "tableau_profile": CONFIG["AUTHOR_HANDLE"],
        "workbook_name": CONFIG["WORKBOOK_NAME"],
        "tableau_dashboard_url": CONFIG["TABLEAU_DASHBOARD_URL"],
        "tableau_story_url": CONFIG["TABLEAU_STORY_URL"],
        "tableau_dashboard_embed_url": get_tableau_embed_url(CONFIG["TABLEAU_DASHBOARD_URL"]),
        "tableau_story_embed_url": get_tableau_embed_url(CONFIG["TABLEAU_STORY_URL"]),
        "kpis": CONFIG["KPIS"]
    })


@app.route('/api/telemetry', methods=['GET'])
def get_telemetry():
    """Return summary telemetry indicators and aggregated insights."""
    return jsonify({
        "status": "success",
        "kpis": CONFIG["KPIS"],
        "summary": INTELLIGENCE_DATA.get("kpis", CONFIG["KPIS"]),
        "dimensions": CONFIG["DIMENSIONS"],
        "story_scenes": CONFIG["STORY_SCENES"]
    })


@app.route('/api/circuits', methods=['GET'])
def get_circuits():
    """Return all 29 Formula 1 host circuits."""
    return jsonify({
        "status": "success",
        "count": len(CIRCUITS_DATA) if isinstance(CIRCUITS_DATA, list) else 29,
        "data": CIRCUITS_DATA
    })


@app.route('/api/drivers', methods=['GET'])
def get_drivers():
    """Return driver profiles and career telemetry stats."""
    return jsonify({
        "status": "success",
        "data": DRIVERS_DATA
    })


@app.route('/api/health', methods=['GET'])
def health_check():
    """Application health probe."""
    return jsonify({
        "status": "healthy",
        "application": "Formula 1 Race Intelligence Dashboard",
        "author": CONFIG["AUTHOR_NAME"],
        "version": "2.0.0"
    })


# Route for serving static assets from root if not using /static/
@app.route('/<path:filename>')
def serve_root_static(filename):
    """Fallback route to serve static assets when accessed without /static prefix."""
    if os.path.exists(os.path.join(STATIC_DIR, filename)):
        return send_from_directory(STATIC_DIR, filename)
    if os.path.exists(os.path.join(BASE_DIR, filename)):
        return send_from_directory(BASE_DIR, filename)
    return ("File not found", 404)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"================================================================")
    print(f"🏎️ FORMULA 1 RACE INTELLIGENCE DASHBOARD")
    print(f"   Lead Architect : {CONFIG['AUTHOR_NAME']}")
    print(f"   Tableau Profile: {CONFIG['AUTHOR_HANDLE']}")
    print(f"   Listening on   : http://127.0.0.1:{port}")
    print(f"================================================================")
    app.run(host='0.0.0.0', port=port, debug=True)
