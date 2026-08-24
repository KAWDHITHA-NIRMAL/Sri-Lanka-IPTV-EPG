#!/usr/bin/env python3
"""
Automated DialogTv EPG Grabber & Channel Splitter
Generates:
  - DialogTv/Channels/<YYYY-MM-DD>/<channel_id>.xml
  - DialogTv/Channels/Epg.xml
  - DialogTv/Channels/Epg.xml.gz
"""

import os
import re
import sys
import gzip
import shutil
import logging
import urllib.request
from datetime import datetime, timezone
import xml.etree.ElementTree as ET

# Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("DIALOGTV_EPG")

# Base Directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIALOG_BASE_DIR = os.path.join(BASE_DIR, "DialogTv", "Channels")

# Read Secret EPG URL from environment variable
EPG_SOURCE_URL = os.environ.get("EPG_SOURCE_URL", "").strip()


def make_safe_filename(name: str) -> str:
    """Sanitize channel ID for safe cross-platform file paths."""
    safe = re.sub(r'[\\/*?:"<>|]', "_", str(name))
    safe = safe.strip(". _")
    return safe if safe else "channel_unknown"


def download_epg_data(url: str) -> bytes:
    """Download EPG data securely with decompression."""
    if not url:
        logger.error("EPG_SOURCE_URL environment variable is missing! Please configure GitHub Secrets.")
        # Check if local fallback exists
        local_fallback = os.path.join(DIALOG_BASE_DIR, "Epg.xml")
        if os.path.exists(local_fallback):
            logger.warning("Using local Epg.xml as fallback.")
            with open(local_fallback, "rb") as f:
                return f.read()
        raise ValueError("EPG_SOURCE_URL is not set.")

    logger.info("Connecting to secure EPG source...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/xml, text/xml, application/gzip, */*",
        "Accept-Encoding": "gzip, deflate"
    }
    
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
        if data[:2] == b'\x1f\x8b':
            logger.info("Decompressing gzipped stream...")
            data = gzip.decompress(data)
        logger.info(f"Downloaded {len(data):,} bytes.")
        return data


def process_dialogtv_epg(raw_bytes: bytes):
    """Parses XMLTV and saves date-based channel XMLs and combined Epg.xml."""
    today_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    date_folder = os.path.join(DIALOG_BASE_DIR, today_date)
    os.makedirs(date_folder, exist_ok=True)

    try:
        root = ET.fromstring(raw_bytes)
    except ET.ParseError:
        clean_text = raw_bytes.decode("utf-8", errors="replace")
        root = ET.fromstring(clean_text)

    root_attribs = dict(root.attrib)
    root_attribs.setdefault("generator-info-name", "DialogTv-EPG-Automation")

    channels_map = {}
    channel_names_map = {}
    programmes_map = {}

    for chan in root.findall("channel"):
        cid = chan.get("id")
        if not cid:
            continue
        channels_map[cid] = chan
        programmes_map[cid] = []

        disp = chan.find("display-name")
        display_name = disp.text.strip() if (disp is not None and disp.text) else cid
        channel_names_map[cid] = display_name

    for prog in root.findall("programme"):
        cid = prog.get("channel")
        if not cid:
            continue
        if cid not in programmes_map:
            programmes_map[cid] = []
            if cid not in channels_map:
                synth = ET.Element("channel", {"id": cid})
                d = ET.SubElement(synth, "display-name")
                d.text = cid
                channels_map[cid] = synth
                channel_names_map[cid] = cid
        programmes_map[cid].append(prog)

    total_channels = len(channels_map)
    total_programmes = sum(len(p) for p in programmes_map.values())
    logger.info(f"Processing {total_channels} channels and {total_programmes} programmes for {today_date}...")

    # 1. Save Channel by Channel XMLs
    for cid, chan_elem in channels_map.items():
        safe_name = f"{make_safe_filename(cid)}.xml"
        chan_path = os.path.join(date_folder, safe_name)

        c_root = ET.Element("tv", root_attribs)
        c_root.append(chan_elem)
        for p in programmes_map.get(cid, []):
            c_root.append(p)

        tree = ET.ElementTree(c_root)
        ET.indent(tree, space="  ", level=0)
        with open(chan_path, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=True)

    # 2. Save Full Combined EPG
    full_epg_file = os.path.join(DIALOG_BASE_DIR, "Epg.xml")
    full_epg_gz = os.path.join(DIALOG_BASE_DIR, "Epg.xml.gz")

    full_tree = ET.ElementTree(root)
    ET.indent(full_tree, space="  ", level=0)

    with open(full_epg_file, "wb") as f:
        full_tree.write(f, encoding="utf-8", xml_declaration=True)

    with gzip.open(full_epg_gz, "wb") as f_gz:
        with open(full_epg_file, "rb") as f_in:
            shutil.copyfileobj(f_in, f_gz)

    # 3. Generate README index in DialogTv/Channels/
    write_dialogtv_readme(channel_names_map, programmes_map, today_date, total_channels, total_programmes)

    logger.info("✅ Finished processing DialogTv EPG!")
    logger.info(f"  - Date Directory: DialogTv/Channels/{today_date}/")
    logger.info(f"  - Full EPG File:  DialogTv/Channels/Epg.xml")


def write_dialogtv_readme(names_map: dict, progs_map: dict, today_date: str, count: int, progs: int):
    readme_path = os.path.join(DIALOG_BASE_DIR, "README.md")
    now_human = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = [
        "# 📺 DialogTv EPG Feeds",
        "",
        f"> **Last Synced**: `{now_human}`  ",
        f"> **Date**: `{today_date}` | **Channels**: `{count}` | **Programmes**: `{progs}`",
        "",
        "## ⚡ Quick Links",
        "",
        "- **All Channels (Full EPG):** [`Epg.xml`](Epg.xml)",
        "- **All Channels (Compressed Gz):** [`Epg.xml.gz`](Epg.xml.gz)",
        f"- **Channel by Channel Folder ({today_date}):** [`{today_date}/`]({today_date}/)",
        "",
        "## 📡 Channel-by-Channel XML Links",
        "",
        f"| Channel Name | Channel ID | Shows | Direct XML Link ({today_date}) |",
        "| :--- | :--- | :---: | :--- |"
    ]

    for cid in sorted(names_map.keys(), key=lambda x: names_map[x].lower()):
        cname = names_map[cid]
        p_count = len(progs_map.get(cid, []))
        safe_name = f"{make_safe_filename(cid)}.xml"
        link = f"[`{today_date}/{safe_name}`]({today_date}/{safe_name})"
        lines.append(f"| **{cname}** | `{cid}` | {p_count} | {link} |")

    lines.append("")
    lines.append("---")
    lines.append("*Auto-updated every 15 minutes by GitHub Actions.*")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    logger.info("=== Starting DialogTv EPG Sync ===")
    try:
        raw_xml = download_epg_data(EPG_SOURCE_URL)
        process_dialogtv_epg(raw_xml)
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
