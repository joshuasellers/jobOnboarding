# Technical sales engineering ramp plan

This plan is tailored to **this repository**: a single demo stack under the repo root (`api/`, `simulator/`, `frontend/`, [`docker-compose.yml`](../docker-compose.yml)). Use markdown checkboxes (`[ ]` / `[x]`) to track progress. Pair each week with the questions in [`KNOWLEDGE_CHECKS.md`](KNOWLEDGE_CHECKS.md).

**Companion docs:** [README.md](../README.md) for quick start; [CONCEPTS_AND_TOOLS.md](CONCEPTS_AND_TOOLS.md) for full explanations (Docker, networking, HTTP, CORS, each stack).

---

## Goal

Build the ability to ship **convincing technical demos** using:

- Java (Spring Boot) — [`api/`](../api/)
- Python (simulation, scripting) — [`simulator/`](../simulator/)
- React (UI) — [`frontend/`](../frontend/)
- Docker (reproducible runs) — Compose + Dockerfiles

By the end of this ramp you should be able to:

- [ ] Spin up a variant of this stack in **1–3 hours** of focused work
- [ ] Reuse this repo as your **personal demo toolkit** (copy, rename, tweak)
- [ ] Support **live presentations** with `docker compose up` and a clear narrative

---

## Mindset: SDE vs demo engineering

| SDE thinking | Demo engineering thinking |
|--------------|---------------------------|
| Scalable, perfect systems | Fast, convincing demos |
| Clean architecture | Working prototype |
| Production-ready | Demo-ready |
| Depth | Breadth + speed |

A demo that works once and tells a clear story beats a perfect system nobody sees.

---

## Universal demo pattern (core mental model)

Today this repo implements the **first hop** of the pattern end-to-end:

```text
Python simulator  →  Java API (REST)  →  React UI (polling)
        ↑                    ↑                    ↑
   simulator/            api/               frontend/
```

**You already have:** fake data, ingest API, browser visualization, one-command Docker run.

**Later extensions** (not in the repo yet; practice items below):

```text
…  →  WebSocket or SSE  →  React (push updates)
…  →  Kafka (optional)  →  consumer  →  API  →  UI
…  →  Map (Leaflet/Mapbox) + alerts + scenarios
```

**Default command for the full stack:**

```bash
docker compose up --build
```

- Frontend: http://localhost:5173  
- API: http://localhost:8080/tracks  

---

## What this repo contains (your “toolkit” baseline)

| Path | Role |
|------|------|
| [`api/`](../api/) | Spring Boot REST, `GET/POST /tracks`, Gradle + Dockerfile |
| [`simulator/`](../simulator/) | Python loop posting JSON to the API |
| [`frontend/`](../frontend/) | Vite + React, polls `/tracks` |
| [`docker-compose.yml`](../docker-compose.yml) | Wires three services on one network |

There are no separate sub-repos (`java-api-template/`, etc.) in this project—**this layout is the template**. For a new customer story, duplicate the repo or branch and customize.

---

## Week 0 — Before or during your first days

**Goal:** Own the baseline stack: run it locally and from Docker, and trace one request.

### Environment and first run

- [x] Read [README.md](../README.md) once, then skim [CONCEPTS_AND_TOOLS.md](CONCEPTS_AND_TOOLS.md) (you can return to sections as you go).
- [x] Run the full stack: `docker compose up --build` from the repo root.
- [x] Confirm simulator logs show posts; browser shows a growing list; `GET /tracks` returns JSON.
- [ ] Run the API **without** Docker (optional but valuable): from [`api/`](../api/), `./gradlew bootRun` (requires Java 17). Point [`simulator.py`](../simulator/simulator.py) at `http://localhost:8080` temporarily *or* run only the UI against localhost (see README for hostname rules).

### Trace the data path

- [ ] Identify where the simulator sets the HTTP **host** (`api` vs `localhost`) and why.
- [ ] Identify where the browser calls **`localhost:8080`** and why.
- [ ] List the three containers and which **ports** are published to your machine.

### Hands-on modifications (build “full-stack reflexes”)

Do these in order; check each when done.

- [ ] **Change the data model:** add a field (e.g. `altitude`) in [`simulator/simulator.py`](../simulator/simulator.py), accept and return it from [`api/src/main/java/com/demo/Application.java`](../api/src/main/java/com/demo/Application.java), display it in [`frontend/src/App.jsx`](../frontend/src/App.jsx).
- [ ] **Add a simple alert in the UI:** e.g. highlight list items when `speed` exceeds a threshold (visual “threat” demo).
- [ ] **Add a chart (optional Week 0 stretch):** e.g. `recharts` in the frontend for speed or track count over time (you may need to derive series from current poll data).

### Narrative practice

- [ ] Write (out loud or on paper) a **30-second** explanation: simulated sensor data → API → dashboard. Use terms: REST, JSON, polling, Docker Compose.

**Knowledge check:** Complete [Section A](KNOWLEDGE_CHECKS.md#a-baseline-stack-and-docker) in [`KNOWLEDGE_CHECKS.md`](KNOWLEDGE_CHECKS.md).

---

## Week 1 — Onboarding week

**Goal:** Treat the React app as a **dashboard**: layout, refresh behavior, and small UX wins.

### Dashboard skills

- [ ] Refactor [`App.jsx`](../frontend/src/App.jsx) into smaller components (e.g. header + track list + stats line).
- [ ] Add loading or error state around `fetch` (even a simple string is enough).
- [ ] Adjust poll interval; notice tradeoff between freshness and load.

### Java API practice

- [ ] Add a read-only endpoint (e.g. `GET /tracks/count` or `GET /health`) and call it from the UI or `curl`.
- [ ] Experiment with clearing or capping the in-memory list (demo “reset” behavior).

### Python practice

- [ ] Parameterize simulator (env vars or constants): interval, speed range, URL—so you can demo different “scenarios” without code rewrites.

**Knowledge check:** [Section B](KNOWLEDGE_CHECKS.md#b-rest-json-and-react-data-flow).

---

## Week 2 — Real-time direction + Docker confidence

**Goal:** Understand what **changes** when you move from polling to push; solidify Docker for sales demos.

### Streaming (implementation checklist — you add this)

Not in the repo yet; use these as build tasks when you are ready.

- [ ] Add a **WebSocket** or **SSE** endpoint on the Spring Boot side.
- [ ] Push new tracks (or deltas) to the browser when the API receives a `POST`.
- [ ] Update React to subscribe instead of (or in addition to) polling every second.

### Docker demo readiness

- [ ] Rebuild images from scratch (`docker compose build --no-cache`) and confirm still works.
- [ ] Document on a sticky note your **exact** demo URL order (what you open first in a customer call).
- [ ] Practice recovery: if a container exits, which logs do you check?

**Knowledge check:** [Section C](KNOWLEDGE_CHECKS.md#c-real-time-and-docker-for-demos).

---

## Week 3 — Defense-style / geospatial story

**Goal:** Map + rules + narrative (“command and control” lite).

### Map and alerts (implementation checklist)

- [ ] Add a map library (e.g. **react-leaflet**) and plot lat/lon from each track.
- [ ] Implement **one business rule** in UI or API: e.g. speed threshold, simple “zone” check, or stale track detection.
- [ ] Optional: short **track history** (last N points per id)—may require API changes.

### Scenario thinking

- [ ] Write a one-page “script” for: drone swarm, zone violation, or anomaly—using only fake data.

**Knowledge check:** [Section D](KNOWLEDGE_CHECKS.md#d-maps-alerts-and-demo-storytelling).

---

## Week 4 (optional) — Integration demos

**Goal:** Show **external** data entering the same pattern.

- [ ] Add a Spring component that calls an **external HTTP API** (weather, ADS-B, or a mock third-party).
- [ ] Normalize the payload into your existing `tracks` shape (or a parallel view model).
- [ ] Surface it in React with clear labeling (“external feed” vs “simulated”).

**Knowledge check:** [Section E](KNOWLEDGE_CHECKS.md#e-integration-and-interoperability).

---

## Core demo scenarios to practice (map to this repo)

Use the same stack; change **story** and **fields**:

| Scenario | Flow |
|----------|------|
| Moving-object / drone style | simulator → API → list or map + threshold alerts |
| Sensor dashboard | simulator → API → charts + table |
| Data fusion | multiple Python scripts or one script with multiple logical sensors → merge in API → UI |
| External integration | third-party API → Java adapter → React |

- [ ] Practice scenario 1 end-to-end with a verbal script.
- [ ] Practice scenario 2 with at least one chart.
- [ ] Sketch (on paper) how you would add scenario 3 without building it yet.
- [ ] Sketch external integration for scenario 4.

---

## Skills checklist (ongoing)

### Backend (Java)

- [ ] Spring Boot basics
- [ ] REST design (`GET` / `POST`, status codes)
- [ ] JSON binding (`Map` vs DTOs)
- [ ] WebSockets or SSE (when you add streaming)

### Python

- [ ] Generate fake structured data
- [ ] HTTP client (`requests`, correct URL per environment)
- [ ] Small scripts and env-based config

### React

- [ ] `useState`, `useEffect`, cleanup (intervals)
- [ ] `fetch` and error handling
- [ ] Lists, keys, conditional UI
- [ ] Charts and maps (as you level up)

### Docker

- [ ] Read a Dockerfile; know `COPY`, `CMD`, `EXPOSE` vs `ports:` in Compose
- [ ] Compose services, networks, `depends_on` limits
- [ ] Host vs container DNS (`api` vs `localhost`)

---

## Daily practice (15–30 minutes)

During onboarding, pick **one** per day:

- [ ] Add or change an API field and thread it through simulator + UI
- [ ] Change UI copy or layout for a specific customer vertical
- [ ] Break something on purpose and fix it (build resilience for live demos)
- [ ] Rehearse one minute of explanation while the stack runs

Prioritize **speed and clarity** over perfect architecture.

---

## What success looks like

After roughly three to four weeks of deliberate practice:

- [ ] You can describe this repo’s architecture in under a minute without reading slides.
- [ ] You can modify simulator + API + UI in one sitting for a new fake scenario.
- [ ] You can run `docker compose up --build` calmly before a call and verify health in under two minutes.
- [ ] You know which parts are **demo-honest** (in-memory, no auth) vs what you would say for production.

---

## Principles (keep visible)

1. **Fake data is normal** — real feeds are rare early; simulate well.
2. **Make it visual** — if they cannot see it, it is harder to remember.
3. **Make it easy to run** — one command wins meetings.
4. **Polish beats complexity** — clear UI + live motion beats opaque depth.

---

## Default stack when you are unsure

Spring Boot API + Python simulator + React dashboard + Docker Compose. Add WebSockets/SSE and a map when the story needs “live” or geospatial punch.

---

## Final takeaway

You are assembling **proof**, **visuals**, and **confidence** for customers—not only code. This repo is the concrete baseline; the checklists above are how you stretch it into a career skill.
