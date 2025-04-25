# TechnoNauts Impactathon'25 Project by Team Innovate Y

# 🎙️ PaperCast - Turning Research into Human-Like Podcasts

> **Listen to Learn. Anywhere, Anytime.**  
> 📡 Live Demo: [https://papercast.streamlit.app/](https://papercast.streamlit.app/)

---

## 🧠 What is PaperCast?

**PaperCast** is an intelligent platform that transforms dense and complex research papers into engaging, human-like podcast episodes. Designed for students, researchers, and curious minds on-the-go, PaperCast makes learning from academic papers easier, faster, and more accessible than ever before.


---

## 🧩 System Architecture

```mermaid
flowchart TD

subgraph User Interaction
    A1[Content Creator Uploads Research Paper]
    A2[User Accesses Web Interface]
    A3[User Listens to Podcast / Downloads Episodes]
end

subgraph Backend
    B1[Extract Text from PDF]
    B2[Summarize with Gemini Flash]
    B3[Generate Script in Podcast Format]
    B4[Tag Script with Voices ]
    B5[Convert to Audio using ElevenLabs]
    B6[Save MP3 & Voice Script]
end

subgraph Storage
    C1[Store MP3 Files]
    C2[Store Tagged Voice Scripts]
end

subgraph Frontend UI
    D1[Dark-themed Podcast UI]
    D2[Play Audio Episode]
    D3[Download Episodes ]
end

A1 --> B1
B1 --> B2
B2 --> B3
B3 --> B4
B4 --> B5
B5 --> B6
B6 --> C1
B6 --> C2

A2 --> D1
D1 --> D2
D1 --> D3
C1 --> D2
C1 --> D3

A3 --> D2
```
---

## 🌟 Features

- 📝 **Automatic Text Extraction** from uploaded PDF research papers.
- 🤖 **Smart Summarization** using Google Gemini LLM with research-optimized prompts.
- 🗣️ **Voice Generation** via ElevenLabs for natural, lifelike podcast narration.
- 🎧 **Dark, Minimal Podcast Web UI** built using React & Tailwind CSS.
- ☁️ **Streamlit Backend** for quick interactions and hosting.
- 📦 **Supabase Integration** for audio storage and access.
- 📱 **Mobile-friendly Design** mimicking real podcast apps.

---

## 🧰 Tech Stack

| Tool         | Purpose                                  |
|--------------|-------------------------------------------|
| `Python`     | Core processing, LLM integration          |
| `Streamlit`  | Lightweight backend interface             |
| `Google Gemini` | Research paper summarization            |
| `ElevenLabs` | AI voice synthesis for podcast-style audio|
| `Supabase`   | Storage of `.wav` audio and thumbnails    |
| `Mermaid.js` | For diagrams and architecture flowcharts  |

---

## 🎨 UI Highlights

- Discover & Trending Pages with smooth audio playback
- Interactive audio player with playlist view
- Responsive podcast card layout inspired by Spotify & YouTube
- Sidebar Navigation with seamless transitions
