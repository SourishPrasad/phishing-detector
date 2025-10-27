cd ~/phishing-detector

cat > README.md <<'EOF'
# Phishing Detector

A simple Python tool that detects potential phishing URLs.

## Example Run

```bash
$ python phishing_detector.py
Enter a URL to check: http://user-login.ru
Result: 🚨 PHISHING URL DETECTED!
```
EOF
```bash
git add README.md
git commit -m "Format README: add example run and link"
git push
