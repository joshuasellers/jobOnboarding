# Demo toolkit

Minimal three-service stack: Spring Boot API, Python simulator, Vite + React frontend.

## Run

```bash
docker compose up --build
```

- Frontend: http://localhost:5173  
- API: http://localhost:8080/tracks  

The simulator posts random tracks to the API every second; the UI polls `/tracks` once per second.

## Layout

- `api/` — Spring Boot 3.2, Java 17  
- `simulator/` — Python 3.10 + `requests`  
- `frontend/` — React 18 + Vite 5  
