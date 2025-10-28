import streamlit as st
from urllib.parse import urlparse
import re

# paste the same scoring logic from your improved script
RISKY_TLDS = {".ru", ".cn", ".tk", ".pw", ".ml", ".cf", ".gq"}
WHITELIST = {"github.com", "google.com", "youtube.com", "wikipedia.org"}

def is_ip_hostname(host: str) -> bool:
    if not host: return False
    host_clean = host.strip("[]")
    return bool(re.match(r"^\d{1,3}(\.\d{1,3}){3}$", host_clean))

def get_tld(host: str) -> str:
    if not host or "." not in host: return ""
    parts = host.lower().rsplit(".", 1)
    return "." + parts[-1]

def score_url(url: str):
    reasons=[]
    score=0.0
    u=url.strip()
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", u):
        u="http://"+u
    parsed=urlparse(u)
    scheme=parsed.scheme.lower()
    host=(parsed.hostname or "").lower()
    path=(parsed.path or "").lower()
    netloc=(parsed.netloc or "").lower()
    if host in WHITELIST:
        return 0.0, ["whitelisted domain"]
    if is_ip_hostname(host):
        score+=3.0; reasons.append("ip-address used in URL (+3)")
    if "@" in netloc or "@" in url:
        score+=3.0; reasons.append("'@' in URL (+3)")
    tld=get_tld(host)
    if tld in RISKY_TLDS:
        score+=1.8; reasons.append(f"risky TLD {tld} (+1.8)")
    suspicious_keywords=["login","signin","secure","update","verify","account","bank"]
    for kw in suspicious_keywords:
        if kw in host or kw in path:
            score+=1.3; reasons.append(f"keyword '{kw}' found (+1.3)"); break
    if "-" in host.split(":")[0]:
        score+=0.6; reasons.append("hyphen in domain (+0.6)")
    if host.count(".")>=3:
        score+=0.6; reasons.append("many subdomains/dots (+0.6)")
    if len(url)>100:
        score+=0.8; reasons.append("very long URL (+0.8)")
    if scheme!="https":
        score+=0.5; reasons.append("not using HTTPS (+0.5)")
    if parsed.port and parsed.port not in (80,443):
        score+=0.9; reasons.append(f"unusual port {parsed.port} (+0.9)")
    return score,reasons

def classify(score):
    if score>=3.0: return "🚨 PHISHING URL DETECTED!"
    elif score>=1.5: return "⚠️ SUSPICIOUS URL"
    else: return "✅ SAFE URL"

st.title("Phishing Detector — Demo")
st.write("Type a URL and get a quick rule-based assessment (runs on the server).")
url = st.text_input("Enter URL (example: example.com or https://example.com)","")
if st.button("Check URL"):
    if not url.strip():
        st.warning("Enter a URL first.")
    else:
        score, reasons = score_url(url)
        label = classify(score)
        st.subheader(label)
        st.write(f"Score: {score:.1f}")
        if reasons:
            st.write("Triggers:")
            for r in reasons:
                st.write("- " + r)
        else:
            st.write("No suspicious signals detected.")
