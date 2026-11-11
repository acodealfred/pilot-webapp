import "./style.css";

type Health = { status: string };

async function fetchHealth(): Promise<string> {
  try {
    const response = await fetch("/api/health");
    if (!response.ok) return "unavailable";
    const body = (await response.json()) as Health;
    return body.status;
  } catch {
    return "unavailable";
  }
}

function renderHome(root: HTMLElement, status: string): void {
  root.innerHTML = `
    <h1 data-testid="page-title">Spear818 Pilot</h1>
    <p>A small web app used to test the agentic SDLC pipeline.</p>
    <p>Service status: <strong data-testid="health-status">${status}</strong></p>
  `;
}

async function fetchVersion(): Promise<string | null> {
  try {
    const response = await fetch("/api/version");
    if (!response.ok) return null;
    const body = (await response.json()) as { version: string };
    return body.version;
  } catch {
    return null;
  }
}

function renderAbout(root: HTMLElement, version: string | null): void {
  const text = version
    ? `Version: <strong data-testid="app-version">${version}</strong>`
    : "Version unavailable";
  root.innerHTML = `
    <h1 data-testid="page-title">About</h1>
    <p>${text}</p>
  `;
}

async function main(): Promise<void> {
  const root = document.getElementById("app");
  if (!root) return;
  if (location.pathname.replace(/\/+$/, "") === "/about") {
    renderAbout(root, await fetchVersion());
    return;
  }
  renderHome(root, "checking…");
  renderHome(root, await fetchHealth());
}

void main();
