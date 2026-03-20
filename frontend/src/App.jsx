import { useEffect, useState } from "react";

export default function App() {
  const [tracks, setTracks] = useState([]);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("http://localhost:8080/tracks")
        .then(res => res.json())
        .then(setTracks);
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h1>Live Tracks</h1>
      <ul>
        {tracks.map(t => (
          <li key={t.id}>
            {t.latitude.toFixed(2)}, {t.longitude.toFixed(2)} - {t.speed.toFixed(1)}
          </li>
        ))}
      </ul>
    </div>
  );
}
