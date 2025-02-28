#!/bin/bash
echo "CLI Browser Search wird installiert..."
git clone https://github.com/shease-dev/cli-browser-search.git /tmp/cli-browser-search
sudo cp /tmp/cli-browser-search/search.py /usr/local/bin/search
sudo chmod +x /usr/local/bin/search
rm -rf /tmp/cli-browser-search
echo "Installation abgeschlossen ✅! Starte mit 'search' im Terminal."
