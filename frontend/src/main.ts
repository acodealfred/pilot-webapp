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

type FeatureRequest = { title: string; description: string; category: string };

function escapeHtml(text: string): string {
  const el = document.createElement("div");
  el.textContent = text;
  return el.innerHTML;
}

async function renderFeatureRequests(root: HTMLElement): Promise<void> {
  root.innerHTML = `
    <h1 data-testid="page-title">Feature requests</h1>
    <form id="request-form" novalidate>
      <p><label>Title <input data-testid="request-title" name="title" /></label></p>
      <p><label>Description <textarea data-testid="request-description" name="description"></textarea></label></p>
      <p><label>Category
        <select data-testid="request-category" name="category">
          <option value="UI">UI</option>
          <option value="Performance">Performance</option>
          <option value="Other" selected>Other</option>
        </select></label></p>
      <p data-testid="request-error" role="alert" hidden></p>
      <button type="submit" data-testid="request-submit">Submit</button>
    </form>
    <ul data-testid="request-list"></ul>
  `;
  const form = root.querySelector<HTMLFormElement>("#request-form")!;
  const error = root.querySelector<HTMLElement>('[data-testid="request-error"]')!;
  const list = root.querySelector<HTMLElement>('[data-testid="request-list"]')!;

  async function refresh(): Promise<void> {
    try {
      const response = await fetch("/api/feature-requests");
      if (!response.ok) return;
      const items = (await response.json()) as FeatureRequest[];
      list.innerHTML = items
        .map((i) => {
          const description = i.description ? `<br>${escapeHtml(i.description)}` : "";
          return `<li data-testid="request-item"><strong>${escapeHtml(i.title)}</strong> (${escapeHtml(i.category)})${description}</li>`;
        })
        .join("");
    } catch {
      // keep the current list
    }
  }

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const data = new FormData(form);
    error.hidden = true;
    try {
      const response = await fetch("/api/feature-requests", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: data.get("title"),
          description: data.get("description"),
          category: data.get("category"),
        }),
      });
      if (!response.ok) {
        const body = (await response.json().catch(() => ({}))) as { detail?: unknown };
        error.textContent = typeof body.detail === "string" ? body.detail : "The request is not valid";
        error.hidden = false;
        return;
      }
      form.reset();
      await refresh();
    } catch {
      error.textContent = "Could not submit the request";
      error.hidden = false;
    }
  });

  await refresh();
}

async function main(): Promise<void> {
  const root = document.getElementById("app");
  if (!root) return;
  const path = location.pathname.replace(/\/+$/, "");
  if (path === "/feature-requests") {
    await renderFeatureRequests(root);
    return;
  }
  if (path === "/about") {
    renderAbout(root, await fetchVersion());
    return;
  }
  renderHome(root, "checking…");
  renderHome(root, await fetchHealth());
}

void main();
