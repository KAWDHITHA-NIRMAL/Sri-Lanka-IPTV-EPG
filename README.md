<div align="center">

# 📡 Sri Lanka IPTV EPG Hub (XMLTV)

[![GitHub Repo](https://img.shields.io/badge/GitHub-Sri--Lanka--IPTV--EPG-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KAWDHITHA-NIRMAL/Sri-Lanka-IPTV-EPG)
[![Auto Sync](https://img.shields.io/badge/Sync%20Interval-Every%2015%20Mins-6366f1?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/KAWDHITHA-NIRMAL/Sri-Lanka-IPTV-EPG/actions)
[![Format](https://img.shields.io/badge/Format-XMLTV%20%7C%20GZ-ec4899?style=for-the-badge&logo=xml&logoColor=white)](https://github.com/KAWDHITHA-NIRMAL/Sri-Lanka-IPTV-EPG)
[![License](https://img.shields.io/badge/License-MIT-3b82f6?style=for-the-badge&logo=open-source-initiative&logoColor=white)](LICENSE)
[![Developer](https://img.shields.io/badge/Developer-Kawdhitha%20Nirmal-f59e0b?style=for-the-badge&logo=codeforces&logoColor=white)](https://github.com/KAWDHITHA-NIRMAL)
[![Team](https://img.shields.io/badge/Team-Cyber%20Yakku™-06b6d4?style=for-the-badge&logo=shield&logoColor=white)](https://github.com/KAWDHITHA-NIRMAL)

<p align="center">
  <b>A high-performance, automated Electronic Program Guide (EPG / XMLTV) engine for Sri Lankan TV Channels.</b><br>
  Fetches live TV guides, splits channels into dedicated daily date folders, provides unified full XML feeds, and synchronizes seamlessly every 15 minutes via GitHub Actions.
</p>

</div>

---

## 🌟 Key Highlights

- ⚡ **15-Minute Automated Synchronization**: Continuously runs via GitHub Actions (`cron: '*/15 * * * *'`) to ensure your guide data is always fresh and accurate.
- 🗂️ **Date-Partitioned Channel Feeds**: Automatically generates individual channel XMLTV files sorted by date (`DialogTv/Channels/<YYYY-MM-DD>/<channel_id>.xml`).
- 📦 **All-in-One Global Feed**: Delivers all 135+ channels combined in a single `DialogTv/Channels/Epg.xml` file.
- 🗜️ **Ultra-Fast Gzip Compression**: Provides `Epg.xml.gz` reducing file transfer sizes by over **95%** (5.5 MB ➔ ~240 KB) for instantaneous loading on mobile and TV devices.
- 🔒 **Zero-Leak Secret Protection**: Source API endpoints remain 100% hidden and secure through GitHub Repository Secrets (`EPG_SOURCE_URL`).
- 🚀 **Zero External Dependencies**: Pure Python standard library engine with built-in HTTP handling, XML parsing, and gzip compression.

---

## 📁 Repository Directory Structure

```text
├── .github/
│   └── workflows/
│       └── epg.yml                   # ⚡ 15-Minute GitHub Actions Auto-Sync Engine
├── DialogTv/
│   └── Channels/
│       ├── Epg.xml                   # 🌟 Combined Full EPG (All Channels)
│       ├── Epg.xml.gz                # 🗜️ Compressed Full EPG (Super Fast)
│       ├── README.md                 # 📋 Live Channel Catalog & Stats
│       └── 2026-08-24/               # 📅 Daily Date Directory (YYYY-MM-DD)
│           ├── 1.xml                 # 📺 Channel 1 XMLTV Guide
│           ├── 2.xml                 # 📺 Channel 2 XMLTV Guide
│           ├── 100.xml               # 📺 Channel 100 XMLTV Guide
│           └── ...                   # 📺 135+ Individual Channel Feeds
├── .gitignore                        # 🛡️ Ignores environment & cache files
├── epg.py                            # 🐍 Core EPG Parser & Channel Splitter
├── LICENSE                           # 📜 MIT Open Source License
└── README.md                         # 📖 Complete Project Documentation
```

---

## 🔗 Live EPG URL Endpoints

Direct URLs ready to use in your IPTV players, OTT apps, and media centers:

### 1️⃣ Full Combined EPG (All Channels)

| Format | Live Direct URL Endpoint | Description |
| :--- | :--- | :--- |
| **Gzip Compressed (Recommended)** | `https://raw.githubusercontent.com/KAWDHITHA-NIRMAL/Sri-Lanka-IPTV-EPG/main/DialogTv/Channels/Epg.xml.gz` | Fast loading, low bandwidth (~240 KB) |
| **Standard XMLTV** | `https://raw.githubusercontent.com/KAWDHITHA-NIRMAL/Sri-Lanka-IPTV-EPG/main/DialogTv/Channels/Epg.xml` | Full uncompressed XMLTV feed |
| **Global CDN (jsDelivr)** | `https://cdn.jsdelivr.net/gh/KAWDHITHA-NIRMAL/Sri-Lanka-IPTV-EPG@main/DialogTv/Channels/Epg.xml` | Edge-cached global delivery |

---

### 2️⃣ Channel-by-Channel Feeds (Date-Wise)

Target specific channels on specific days to save bandwidth and device memory:

```text
https://raw.githubusercontent.com/KAWDHITHA-NIRMAL/Sri-Lanka-IPTV-EPG/main/DialogTv/Channels/<YYYY-MM-DD>/<CHANNEL_ID>.xml
```

#### 📌 Concrete Examples:
- **Channel 1 (Date: 2026-08-24):**
  ```text
  https://raw.githubusercontent.com/KAWDHITHA-NIRMAL/Sri-Lanka-IPTV-EPG/main/DialogTv/Channels/2026-08-24/1.xml
  ```
- **Channel 10 (Date: 2026-08-24):**
  ```text
  https://raw.githubusercontent.com/KAWDHITHA-NIRMAL/Sri-Lanka-IPTV-EPG/main/DialogTv/Channels/2026-08-24/10.xml
  ```
- **Channel 100 (Date: 2026-08-24):**
  ```text
  https://raw.githubusercontent.com/KAWDHITHA-NIRMAL/Sri-Lanka-IPTV-EPG/main/DialogTv/Channels/2026-08-24/100.xml
  ```

---

## 📱 Supported Players & Platforms

This standard XMLTV feed is fully compatible with all major IPTV, OTT, and PVR players:

| Player / Platform | Supported Formats | Recommended URL |
| :--- | :---: | :--- |
| 📺 **TiviMate IPTV Player** | `.xml`, `.xml.gz` | `Epg.xml.gz` (Instant load) |
| 📱 **OTT Navigator IPTV** | `.xml`, `.xml.gz` | `Epg.xml.gz` |
| 💻 **IPTV Smarters Pro** | `.xml` | `Epg.xml` |
| 🍿 **Kodi (PVR IPTV Simple Client)** | `.xml`, `.xml.gz` | `Epg.xml.gz` |
| 🎧 **VLC Media Player** | `.xml` | `Epg.xml` |
| ⚡ **Perfect Player** | `.xml`, `.xml.gz` | `Epg.xml.gz` |

---

## 📜 License

This project is licensed under the **MIT License**.

```text
MIT License

Copyright (c) 2026 ‌‌‌‌✘ 𝗞𝗔𝗪𝗗𝗛𝗜𝗧𝗛𝗔 𝗡𝗜𝗥𝗠𝗔𝗟 •| Cyber Yakku™

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

See the full [LICENSE](LICENSE) file for more details.

---

## 👨‍💻 Developer & Credits

<div align="center">

| Project Lead & Developer | Organization / Team |
| :---: | :---: |
| **Kawdhitha Nirmal** | **Cyber Yakku™** |
| [![GitHub](https://img.shields.io/badge/GitHub-KAWDHITHA--NIRMAL-181717?style=flat-square&logo=github)](https://github.com/KAWDHITHA-NIRMAL) | [![Cyber Yakku](https://img.shields.io/badge/Cyber%20Yakku-Official%20Team-red?style=flat-square&logo=shield)](https://github.com/KAWDHITHA-NIRMAL) |

</div>

<br>

> **Disclaimer**: This tool is designed for organizing and splitting Electronic Program Guide (EPG) metadata for personal research and integration. All channel names, program details, and logos belong to their respective copyright holders.

<p align="center">
  <b>Built with ❤️ by Kawdhitha Nirmal &bull; Powered by Cyber Yakku™</b>
</p>
