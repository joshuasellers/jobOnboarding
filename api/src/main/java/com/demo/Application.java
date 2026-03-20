package com.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@SpringBootApplication
@RestController
@CrossOrigin
public class Application {

    private List<Map<String, Object>> tracks = new ArrayList<>();

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @GetMapping("/tracks")
    public List<Map<String, Object>> getTracks() {
        return tracks;
    }

    @PostMapping("/tracks")
    public void addTrack(@RequestBody Map<String, Object> track) {
        track.put("id", UUID.randomUUID().toString());
        track.put("timestamp", System.currentTimeMillis());
        tracks.add(track);
    }
}
