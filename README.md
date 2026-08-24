# 📺 DialogTv Automated EPG Guide & Setup

මෙම Repository එක මඟින් DialogTv EPG data auto-fetch වී, සෑම channel එකකටම දින අනුව (Date-wise) වෙන වෙනම XML files සහ සියලුම channels අඩංගු `Epg.xml` file එක auto generate වේ. GitHub Actions මඟින් සෑම විනාඩි 15 කට වරක්ම update වේ.

---

## 🔒 1. Source Link එක Hide කර GitHub Secrets වලට Add කරන්නේ කෙසේද?

ඔබගේ EPG Source API link එක කිසිදු කෙනෙකුට code එක හරහා හෝ commits හරහා **නොපෙනෙන පරිදි සම්පූර්ණයෙන්ම Hide කිරීමට**:

1. ඔබගේ **GitHub Repository** එකට යන්න.
2. උඩ ඇති **Settings** tab එක click කරන්න.
3. වම් පැත්තේ menu එකෙන් **Secrets and variables** ➡️ **Actions** click කරන්න.
4. **New repository secret** (කොළ පාට button එක) click කරන්න.
5. **Name** එකට: `EPG_SOURCE_URL` යොදන්න.
6. **Secret** එකට: ඔබගේ EPG Source Link එක paste කරන්න.
7. **Add secret** button එක click කරන්න.

> **සැළකිය යුතුයි**: මෙසේ Add කළ පසු GitHub Actions මඟින් background එකෙන් පමණක් secure එකක් ලෙස මෙය කියවන අතර, කිසිදු කෙනෙකුට ඔබගේ source link එක දැකගත නොහැක!

---

## 🚀 2. Files GitHub එකට Upload කරන්නේ කෙසේද?

Terminal / Command Prompt එකේ පහත commands run කරන්න:

```bash
# 1. Git initialize කරන්න
git init

# 2. Files add කර commit කරන්න
git add .
git commit -m "Initial commit of DialogTv EPG"

# 3. Main branch එකට මාරු වන්න
git branch -M main

# 4. ඔබගේ Repo link එක add කරන්න
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>.git

# 5. Push කරන්න
git push -u origin main
```

---

## ⚙️ 3. Workflow Permissions Enable කිරීම (වැදගත්)

GitHub Actions එකට auto-update files save (commit & push) කිරීමට permission ලබා දිය යුතුය:

1. Repo එකේ **Settings** ➡️ **Actions** ➡️ **General** වෙත යන්න.
2. පහළට scroll කර **Workflow permissions** යටතේ **Read and write permissions** select කරන්න.
3. **Save** click කරන්න.

---

## 🔗 4. IPTV Players (TiviMate / OTT Navigator) සඳහා Direct Links

### 📡 සියලුම Channels එකවර බැලීමට (Full EPG):
```text
https://raw.githubusercontent.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>/main/DialogTv/Channels/Epg.xml
```

*Compressed XML (.gz format - වේගයෙන් load වේ):*
```text
https://raw.githubusercontent.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>/main/DialogTv/Channels/Epg.xml.gz
```

---

### 📺 තනි තනි Channels වලට (Date අනුව):
```text
https://raw.githubusercontent.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>/main/DialogTv/Channels/<YYYY-MM-DD>/<CHANNEL_ID>.xml
```
*උදාහරණ:*
- Channel 1: `https://raw.githubusercontent.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>/main/DialogTv/Channels/2026-08-24/1.xml`
- Channel 10: `https://raw.githubusercontent.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>/main/DialogTv/Channels/2026-08-24/10.xml`
- Channel 100: `https://raw.githubusercontent.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>/main/DialogTv/Channels/2026-08-24/100.xml`

---

## 📁 Repository Structure

```text
├── .github/
│   └── workflows/
│       └── update_epg.yml     # Auto Update Action (Every 15 min)
├── DialogTv/
│   └── Channels/
│       ├── Epg.xml            # Full EPG (All Channels)
│       ├── Epg.xml.gz         # Gzip EPG
│       ├── README.md          # Channels Index
│       └── <YYYY-MM-DD>/      # Daily folder (1.xml, 2.xml, ...)
├── .gitignore                 # Protects local environment
├── README.md                  # Detailed Sinhala Guide
└── update_epg.py              # Standalone EPG Processor
```
