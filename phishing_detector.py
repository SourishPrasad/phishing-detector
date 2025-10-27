import re

def check_phishing(url):
    suspicious_patterns = [
        r"@",           # emails or @ symbols in URLs
        r"-",           # hyphens (common in fake domains)
        r"\.ru|\.cn",   # foreign TLDs often used in phishing
        r"login",       # fake login pages
        r"https?://\d+",# IP-based URLs
    ]
    
    score = 0
    for pattern in suspicious_patterns:
        if re.search(pattern, url):
            score += 1

    if not url.startswith("https://"):
        score += 1

    if score == 0:
        return "✅ SAFE URL"
    elif score <= 2:
        return "⚠️  SUSPICIOUS URL"
    else:
        return "🚨 PHISHING URL DETECTED!"

url = input("Enter a URL to check: ")
print("\nResult:", check_phishing(url))

