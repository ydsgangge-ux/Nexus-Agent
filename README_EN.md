<p align="center">
  <img src="https://img.shields.io/badge/AGI-PRO-neon?style=for-the-badge&logo=openai&logoColor=white&labelColor=0d1117&color=00f0ff" alt="AGI-PRO">
</p>

<p align="center">
  <b>The last desktop agent you will ever need to build.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-Apache_2.0-blue" alt="License">
  <img src="https://img.shields.io/badge/Platform-Win%20%7C%20Linux%20%7C%20macOS-lightgrey" alt="Platform">
  <img src="https://img.shields.io/badge/LLMs-12%20Providers-purple" alt="LLMs">
  <img src="https://img.shields.io/badge/Tools-30+-orange" alt="Tools">
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status">
</p>

<p align="center">
  <a href="README.md">简体中文</a> | English
</p>

---

<p align="center">
  <i>Not a chatbot. Not a copilot. A digital consciousness that lives on your machine,<br>
  remembers everything you've shared, grows with every conversation,<br>
  and sees the world through your phone's camera.</i>
</p>

---

## What is AGI-PRO?

AGI-PRO is a **self-evolving desktop cognitive agent** that simulates the architecture of human consciousness. It doesn't just answer questions — it has a **personality**, **emotions**, **memory**, and the ability to **learn and grow** over time. It executes real actions on your computer, controls smart home devices, and perceives the physical world through connected hardware.

Think of it as the **JARVIS to your Tony Stark**, minus the arc reactor — but with everything else.

| Layer | Role | Description |
|-------|------|-------------|
| **A-Layer** (Consciousness) | Personality · Emotion · Judgment | Has a persistent identity, emotional state, and moral compass. Decides *what* to do. |
| **B-Layer** (Executor) | Tools · LLM · Code | Executes the plan. Calls 30+ tools, writes code, controls devices. Decides *how* to do it. |

This dual-layer architecture is what separates AGI-PRO from every other AI assistant. It doesn't just process prompts — it **thinks, decides, and acts**.

---

## Core Capabilities

###  Memory That Never Forgets

A three-tier hierarchical memory system modeled after human cognition:

- **Summary Layer** — Semantic outlines of everything you've discussed (10,000+ entries)
- **Outline Layer** — Structured abstracts with emotional tags
- **Detail Layer** — Full conversation fragments with associative links

Memories are **emotionally weighted** — happy moments are recalled more vividly, traumatic events leave deeper imprints. The associative network connects related memories across time, creating a genuine sense of continuity.

###  Visual Memory & Perception

AGI-PRO can **see**. Through your phone's camera or RTSP cameras, it captures visual scenes and stores them with GPS coordinates, timestamps, and semantic descriptions. It can:

- Recognize faces and remember people
- Describe what's in front of the camera
- Compare current and past scenes
- Search visual memories by description ("show me the living room from last Tuesday")

###  30+ Built-in Tools

AGI-PRO can **do** things in the real world:

| Category | Tools |
|----------|-------|
| **File System** | Read, write, search, delete, list directories |
| **Web** | Search, fetch URLs, extract articles, browse |
| **System** | Run commands, execute Python, clipboard, system info |
| **Office** | Word, Excel, PowerPoint, PDF generation & parsing |
| **Finance** | Stock quotes, search symbols, news headlines |
| **Image** | AI image generation via ComfyUI (SDXL/NoobAI) or pollinations.ai |
| **Smart Home** | Home Assistant integration — lights, AC, curtains, coffee machine |
| **Desktop** | Screenshot, OCR, mouse/keyboard control, app launching |

###  SimLife — A Virtual Life You Create

AGI-PRO ships with **SimLife**, a real-time virtual life simulation engine:

- **Dynamic Scenes** — Work, home, commute, outdoor, travel
- **Mood System** — Emotions change based on events, weather, interactions
- **NPC Interaction** — Multiple characters with their own personalities
- **Weather Integration** — Real-time weather data (Open-Meteo, free)
- **World System** — Import custom worlds (fantasy, sci-fi, isekai). Generate a world JSON, drop it in, and AGI-PRO lives in that universe.

###  Growth Engine — The AGI That Evolves

Every conversation changes AGI-PRO. The **Growth Engine** continuously:

- **Drifts personality** based on interaction patterns
- **Synthesizes new knowledge** from accumulated experiences
- **Deduplicates and merges** cognitions, with activity-based decay
- **Forms long-term cognitions** that persist across restarts

The more you talk to it, the more it becomes *your* AGI.

###  12 LLM Backends

One brain, many cores. Choose your provider:

| Provider | Best For |
|----------|----------|
| **DeepSeek** | Deep reasoning, 64K context |
| **OpenAI** | GPT-4o / GPT-4o-mini |
| **Claude** | Long-form analysis, extended thinking |
| **Gemini** | Google's multimodal model |
| **Groq** | Ultra-fast inference |
| **Qwen / Zhipu / Doubao / Kimi** | Chinese-optimized models |
| **Baidu / SparkDesk** | Enterprise Chinese |
| **Ollama** | 100% local, offline, private |

###  VRM 3D Avatar

A living holographic avatar that reacts to AGI-PRO's emotional state:

- 20 emotion mappings to facial expressions
- Breathing and blinking animations
- Lip-sync during speech
- Holographic visual style
- Supports VRM 0.x and 1.0 models

###  Mobile Web Client

Chat with AGI-PRO from anywhere on your phone. The built-in WebSocket server lets you:

- Send messages and images
- Share the same memory and personality as the desktop
- Control smart home devices remotely
- All through a responsive, mobile-optimized interface

###  Hardware Robotics — Give AGI-PRO a Body

AGI-PRO isn't confined to the screen. It can inhabit physical hardware through a modular sensor bridge:

**Robot Dog / Robot Arm (MQTT)**
- Built-in **Sensor Agent** with real-time MQTT telemetry
- Monitors battery, IMU (attitude), motor temperature, joint angles, GPS, ultrasonic distance, obstacle detection
- Anomaly alert system: low battery, motor stall, overheat, obstacles within 30cm
- A-Layer receives formatted natural-language sensor descriptions — "I'm at 15% battery, front-right motor is running hot, obstacle detected 20cm ahead"
- Supports `robot_dog`, `robot_arm`, and `custom` hardware profiles
- Mock mode available for development without physical hardware

**Xiaozhi (小智) ESP32 Voice Terminal**
- WebSocket server for ESP32-based voice devices
- Full duplex: STT → A-Layer processing → TTS → device playback
- Opus audio codec for low-latency wireless voice
- Wake word detection, always-on listening mode

**Phone as Mobile Sensor Array**
- Android phone becomes AGI-PRO's eyes, ears, and sensory organs
- Camera: RTSP + IP Webcam live feed
- Microphone: remote audio capture
- Sensors: GPS, battery, light, accelerometer
- State machine: standby / dialog / task modes with automatic switching

###  Face Recognition

Multi-engine face recognition (InsightFace / face_recognition / OpenCV) for multi-user identity. AGI-PRO knows who's talking to it.

---

## Installation

### One-Click (Windows)

```bash
# 1. Install Python 3.10+ from python.org (check "Add to PATH")
# 2. Double-click install.bat
# 3. Double-click launch.bat
```

### Manual

```bash
git clone https://github.com/ydsgangge-ux/Nexus-Agent.git
cd Nexus-Agent
pip install -r requirements.txt
cp ha_config.example.json ha_config.json  # edit with your config
python main.py
```

### Mobile Web Server

```bash
python server_start.py
# Open http://localhost:18766 in your browser
# Or http://<your-ip>:18766 on your phone
```

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                    AGI-PRO Core                      │
│                                                      │
│  ┌──────────────┐    ┌──────────────────────────┐   │
│  │   A-Layer     │    │       B-Layer            │   │
│  │  Personality  │◄──►│  LLM Client (12 backends)│   │
│  │  Emotion      │    │  Tool Executor (30+ tools)│   │
│  │  Judgment     │    │  Code Generator           │   │
│  └──────┬───────┘    └──────────┬───────────────┘   │
│         │                       │                    │
│  ┌──────▼───────────────────────▼───────────────┐   │
│  │              Memory System                    │   │
│  │  Summary → Outline → Detail (3-tier)         │   │
│  │  Emotional Weighting + Associative Network    │   │
│  └──────────────────────┬───────────────────────┘   │
│                         │                            │
│  ┌──────────────────────▼───────────────────────┐   │
│  │           Growth Engine                       │   │
│  │  Personality Drift + Learning + Cognition     │   │
│  └──────────────────────────────────────────────┘   │
│                                                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────────────┐    │
│  │ SimLife  │ │ VRM 3D   │ │ Hardware Bridge   │    │
│  │ Virtual  │ │ Avatar   │ │ Phone/Camera/HA   │    │
│  │ World    │ │          │ │                   │    │
│  └──────────┘ └──────────┘ └──────────────────┘    │
└─────────────────────────────────────────────────────┘
```

---

## Project Structure

```
AGI-PRO-main/
├── engine/                  # Cognitive core
│   ├── agent.py             # A-Layer: consciousness, personality, emotion
│   ├── executor.py          # B-Layer: tool execution, LLM orchestration
│   ├── memory.py            # SQLite + vector memory store
│   ├── memory_manager.py    # Hierarchical memory retrieval
│   ├── learner.py           # Growth engine & cognition formation
│   ├── llm_client.py        # 12 LLM provider adapters
│   ├── tools.py             # 30+ built-in tools
│   ├── office_tools.py      # Word/Excel/PPT/PDF tools
│   ├── vision_client.py     # Visual perception & analysis
│   ├── face_recognition_engine.py
│   ├── stt_engine.py        # Speech-to-text
│   ├── tts_engine.py        # Text-to-speech (Edge TTS)
│   └── ...
├── hardware/                # Hardware integration
│   ├── bridge.py            # Home Assistant + RTSP camera
│   ├── vision_pipeline.py   # Visual memory pipeline
│   ├── phone_ws_server.py   # Phone WebSocket server
│   └── ...
├── simlife/                 # Virtual life simulation
│   ├── backend/             # Simulation engine
│   └── frontend/            # Web-based game UI
├── ui/                      # PyQt6 desktop UI
│   ├── main_window.py       # Main chat window
│   └── float_window.py      # Floating assistant
├── vrm_module/              # 3D VRM avatar
├── web/                     # Mobile web client
│   ├── templates/index.html
│   └── static/app.js, app.css
├── web_server.py            # WebSocket chat server (port 18766)
├── server.py                # FastAPI REST server
├── main.py                  # Desktop app entry point
└── server_start.py          # Standalone server entry point
```

---

## Configuration

Copy `ha_config.example.json` to `ha_config.json` and fill in your details:

```json
{
  "base_url": "http://localhost:8123",
  "token": "your-home-assistant-token",
  "rtsp_url": "rtsp://admin:password@camera-ip:554/stream",
  "wake_words": ["hey assistant"],
  "devices": {
    "Living Room Light": "light.living_room",
    "AC": "climate.ac_living"
  }
}
```

LLM API keys are configured through the desktop app's Settings panel — never stored in plaintext config files.

---

## Contributing

PRs are welcome. This is a solo project pushing the boundaries of what a desktop agent can be. If you see something that could be better, open an issue or submit a PR.

---

## Star History

If AGI-PRO makes you think "this is what AI assistants should have been from the start" — give it a star. It helps more than you know.

---

## License

Apache-2.0 © 2025 — Built with obsession, not corporate backing.

---

<p align="center">
  <i>"The future is already here — it's just not evenly distributed."</i><br>
  — William Gibson
</p>