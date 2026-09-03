#!/bin/bash
set -e
echo "=== Deploying Temanulis ==="
cd /home/ubuntu/temanulis
git pull origin main

# sync to web root
sudo cp -u index.html /var/www/temanulis/index.html
if [ -f "content-bank (11).html" ]; then
  sudo cp -u "content-bank (11).html" "/var/www/temanulis/content-bank (11).html"
fi
sudo chown -R ubuntu:www-data /var/www/temanulis
sudo chmod -R 775 /var/www/temanulis

echo "=== Testing Deployment ==="
STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://faridadamn.my.id/temanulis/)
if [ "$STATUS" -eq 200 ]; then
  echo "Temanulis successfully deployed and live at https://faridadamn.my.id/temanulis/ (HTTP 200)"
else
  echo "Warning: HTTP status is $STATUS"
fi
