# Knowledge checks (written practice)

Use this file like an open-book exam: answer in your own words **before** reading the [answer key](#answer-key). You can type answers directly under each prompt in this markdown file, or use a notebook.

**How to use**

1. Complete a section after you finish the matching phase in [`TRAINING_RAMP.md`](TRAINING_RAMP.md).
2. Write answers under **Your answer**.
3. Score yourself with the [answer key](#answer-key); revisit [CONCEPTS_AND_TOOLS.md](CONCEPTS_AND_TOOLS.md) for diagrams and definitions (and [README.md](../README.md) for the short overview).

---

## A. Baseline stack and Docker

**A1.** In one sentence, what problem does Docker Compose solve for this repo’s demo?

Your answer:



---

**A2.** The simulator uses `http://api:8080` but the React app uses `http://localhost:8080`. Why are both correct in their contexts?

Your answer:



---

**A3.** What happens to stored tracks if you restart only the `api` container? Why?

Your answer:



---

**A4.** What does `depends_on: api` guarantee in [`docker-compose.yml`](../docker-compose.yml)? What does it *not* guarantee?

Your answer:



---

**A5.** Name the two HTTP methods used on `/tracks` in this project and what each does.

Your answer:



---

## B. REST, JSON, and React data flow

**B1.** In this app, is the browser “polling” or “pushing” updates from the server? How do you know from the code?

Your answer:



---

**B2.** Why does the Spring Boot app use `@CrossOrigin` for browser clients, while the Python simulator does not need CORS configuration on its side?

Your answer:



---

**B3.** What is the difference between **server state** (the list in Java) and **client state** (`tracks` in React) after a successful `fetch`?

Your answer:



---

**B4.** If `useEffect` had an empty dependency array `[]`, what happens to the interval when the component unmounts? Why does the cleanup function matter?

Your answer:



---

## C. Real-time and Docker for demos

**C1.** Compare **polling** to **WebSockets** for showing new tracks. Give one advantage of each for a sales demo.

Your answer:



---

**C2.** You are about to join a live customer call. List three quick checks you would run on this stack to reduce risk (commands, URLs, or things to observe).

Your answer:



---

**C3.** If the simulator logs `error` repeatedly right after `docker compose up`, name two plausible causes and what you would inspect first.

Your answer:



---

## D. Maps, alerts, and demo storytelling

**D1.** You want a “restricted zone” demo: tracks inside a polygon are green, outside are red. Where could you implement the rule (browser only, API only, or both) and one tradeoff of each?

Your answer:



---

**D2.** Write a **60-second** spoken script that explains this repo to a non-technical buyer. (Outline is fine: opening, middle, close.)

Your answer:



---

**D3.** Give one example of a claim you should **avoid** making about this baseline repo unless you add features (e.g. persistence, security).

Your answer:



---

## E. Integration and interoperability

**E1.** Sketch how you would add a **second** data source (external REST API) alongside the Python simulator so the UI still shows one combined list. What component would merge the data?

Your answer:



---

**E2.** Why might you normalize external payloads into the same JSON shape as your existing `track` objects?

Your answer:



---

## Self-score rubric (optional)

| Section | Questions | You answered without key (Y/N) | Notes |
|---------|-----------|----------------------------------|-------|
| A | 5 | | |
| B | 4 | | |
| C | 3 | | |
| D | 3 | | |
| E | 2 | | |

---

## Answer key

Try the questions first. These are concise reference answers; yours may be longer or phrased differently and still be correct.

**A1.** Compose builds and runs the multi-container app (API + simulator + frontend) with consistent networking and one command, so demos reproduce across machines.

**A2.** Containers on the Compose network resolve the service name `api`. The browser runs on the host and reaches the published port via `localhost`.

**A3.** Tracks are lost; they live in an in-memory `ArrayList` in the JVM process. Restarting the container starts a fresh process.

**A4.** It orders startup so dependent services start after `api` is *started*; it does not wait for the API to be listening or healthy.

**A5.** `GET /tracks` returns the list; `POST /tracks` accepts a JSON body and appends a track (with server-added `id` and `timestamp`).

**B1.** Polling: `setInterval` calls `fetch` every second in `useEffect` in [`App.jsx`](../frontend/src/App.jsx).

**B2.** Browsers enforce same-origin policy for cross-origin requests; `@CrossOrigin` adds headers so the UI origin (e.g. :5173) may read API responses from :8080. Server-to-server HTTP from Python is not subject to that browser rule.

**B3.** Server state is authoritative on the API until changed; client state is a snapshot copied into React that updates when the next poll succeeds.

**B4.** The cleanup runs on unmount and clears the interval, preventing leaks and duplicate timers. Empty `[]` means the effect runs once on mount.

**C1.** Polling: simple, easy to explain. WebSockets: lower latency and “feels live” without periodic requests (once implemented).

**C2.** Examples: `docker compose ps`; open `/tracks` and see JSON; open `:5173` and see list; watch simulator logs for `sent`.

**C3.** Examples: API not ready yet (`depends_on` is not health-aware); wrong URL; port conflict on 8080. Inspect `api` logs and `docker compose logs`.

**D1.** Browser-only: fast to prototype, rule hidden from other clients. API-only: single source of truth. Both: validate server-side and reflect in UI—more work, clearer enterprise story.

**D2.** (No single answer.) Should mention fake/simulated data, API as ingest, UI as visibility, Docker for repeatability.

**D3.** Examples: “durable history,” “multi-tenant security,” “production SLAs,” “encrypted auth,” without building those.

**E1.** Typical pattern: Spring service fetches external API, maps to track maps, merges into the same list or a combined endpoint; simulator keeps posting as today.

**E2.** One shape keeps React rendering simple, avoids forked UI logic, and makes demos easier to maintain.
