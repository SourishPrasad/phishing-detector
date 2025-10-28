# 🛡️ Phishing Detector (Rule-Based)

A lightweight **phishing URL detection tool** built using Python.  
Designed for quick detection of suspicious links using a rule-based weighted scoring system.

---

## ⚙️ Features
- ✅ Works entirely **offline** — no privacy risk.
- ⚡ Instant detection — no need for external APIs.
- 🧠 **Weighted scoring system** to reduce false positives.
- 🔍 Highlights which rules triggered detection.
- 📱 Works perfectly on **Termux (Android)** or any Python 3 environment.

---

## 🧩 Example Run
```bash
$ python phishing_detector.py
Enter a URL to check: http://paypal-login.ru
Result: 🚨 PHISHING URL DETECTED!
Score: 6.9
Triggers:
 - keyword 'login' found (+1.3)
 - risky TLD .ru (+1.8)
 - not using HTTPS (+0.5)
 - hyphen in domain (+0.6)
 - many subdomains/dots (+0.6)
