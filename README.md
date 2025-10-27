cd ~/phishing-detector

cat > README.md <<'EOF'
# Phishing Detector

A simple Python tool that detects potential phishing URLs.

## Example Run

```bash
$ python phishing_detector.py
Enter a URL to check: http://paypal-login.ru
Result: 🚨 PHISHING URL DETECTED!
