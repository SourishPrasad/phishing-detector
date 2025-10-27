cd ~/phishing-detector

cat >> README.md <<'EOF'
## Example run

$ python phishing_detector.py
Enter a URL to check: http://paypal-login.ru
Result: 🚨 PHISHING URL DETECTED!
EOF
git add README.md
git commit -m "Add example run to README"
git push
