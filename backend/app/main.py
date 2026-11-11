"""Pilot web app backend.

Serves a small JSON API under /api and the built front end from frontend/dist.
"""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

FRONTEND_DIST = Path(__file__).resolve().parents[2] / "frontend" / "dist"

APP_VERSION = "0.1.0"

app = FastAPI(title="Spear818 Pilot Web App")


@app.get("/api/health")
def health() -> dict[str, str]:
    """Liveness check used by CI, Docker and the home page."""
    return {"status": "ok"}


@app.get("/api/version")
def version() -> dict[str, str]:
    """Report the app version shown on the About page."""
    return {"version": APP_VERSION}


if FRONTEND_DIST.exists():
    app.mount("/assets", StaticFiles(directory=FRONTEND_DIST / "assets"), name="assets")

    @app.get("/{path:path}", include_in_schema=False)
    def spa(path: str) -> FileResponse:
        """Serve the single-page front end for any non-API path."""
        candidate = FRONTEND_DIST / path
        if path and candidate.is_file() and FRONTEND_DIST in candidate.resolve().parents:
            return FileResponse(candidate)
        return FileResponse(FRONTEND_DIST / "index.html")
