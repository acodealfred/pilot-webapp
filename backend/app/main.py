"""Pilot web app backend.

Serves a small JSON API under /api and the built front end from frontend/dist.
"""

from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

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


class FeatureRequestIn(BaseModel):
    title: str
    description: str = ""
    category: Literal["UI", "Performance", "Other"]


# Kept in memory only: lost on restart, shared by all users. Oldest first.
feature_requests: list[dict[str, str]] = []


@app.post("/api/feature-requests", status_code=201)
def create_feature_request(body: FeatureRequestIn) -> dict[str, str]:
    """Store a new feature request."""
    title = body.title.strip()
    if not title:
        raise HTTPException(status_code=422, detail="Title is required")
    item = {
        "title": title,
        "description": body.description.strip(),
        "category": body.category,
    }
    feature_requests.append(item)
    return item


@app.get("/api/feature-requests")
def list_feature_requests() -> list[dict[str, str]]:
    """List feature requests, newest first."""
    return list(reversed(feature_requests))


if FRONTEND_DIST.exists():
    app.mount("/assets", StaticFiles(directory=FRONTEND_DIST / "assets"), name="assets")

    @app.get("/{path:path}", include_in_schema=False)
    def spa(path: str) -> FileResponse:
        """Serve the single-page front end for any non-API path."""
        candidate = FRONTEND_DIST / path
        if path and candidate.is_file() and FRONTEND_DIST in candidate.resolve().parents:
            return FileResponse(candidate)
        return FileResponse(FRONTEND_DIST / "index.html")
