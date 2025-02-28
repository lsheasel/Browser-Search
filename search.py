#!/usr/bin/env python3
import webbrowser
import platform
import shutil
import os
import time
import random

FUN_FACTS = [
    "Fun Fact: Google wurde 1998 gegründet!",
    "Fun Fact: Der erste Webbrowser hieß WorldWideWeb!",
    "Fun Fact: DuckDuckGo verfolgt keine Nutzer!",
    "Fun Fact: Das erste YouTube-Video hieß 'Me at the zoo'!",
    "Fun Fact: Bing wurde 2009 von Microsoft veröffentlicht!"
]

def get_available_browsers():
    browsers = {}
    if platform.system() == "Windows":
        browser_paths = {
            "firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
            "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "brave": "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        }
        for name, path in browser_paths.items():
            if os.path.exists(path):
                webbrowser.register(name, None, webbrowser.BackgroundBrowser(path))
                browsers[name] = name
    else:
        browser_list = [
            ("firefox", "firefox"),
            ("chrome", "google-chrome"),
            ("brave", "brave-browser")
        ]
        for name, command in browser_list:
            if shutil.which(command):
                webbrowser.register(name, None, webbrowser.BackgroundBrowser(command))
                browsers[name] = name
    return browsers

def search_google(browser, query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.get(browser).open(url)

def search_duckduckgo(browser, query):
    url = f"https://duckduckgo.com/?q={query}"
    webbrowser.get(browser).open(url)

def search_youtube(browser, query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.get(browser).open(url)

def show_start_screen():
    print("""
    ██████╗ ██████╗  █████╗ ███████╗███████╗███████╗ ██████╗██╗  ██╗
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██║ ██╔╝
    ██║  ██║██████╔╝███████║███████╗███████╗███████╗██║     █████╔╝ 
    ██║  ██║██╔═══╝ ██╔══██║╚════██║╚════██║╚════██║██║     ██╔═██╗ 
    ██████╔╝██║     ██║  ██║███████║███████║███████║╚██████╗██║  ██╗
    ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝
    CLI Browser Search 🔥
    """
    )
    print(random.choice(FUN_FACTS))
    time.sleep(1)
    print("Starte Programm...")
    time.sleep(1)

if __name__ == "__main__":
    show_start_screen()
    available_browsers = get_available_browsers()

    if not available_browsers:
        print("Keine unterstützten Browser gefunden!")
        exit()

    print("Verfügbare Browser:")
    for index, browser in enumerate(available_browsers.keys(), start=1):
        print(f"{index}) {browser.capitalize()}")

    browser_choice = input("Auswahl: ")
    try:
        browser = list(available_browsers.keys())[int(browser_choice) - 1]
    except (IndexError, ValueError):
        print("Ungültige Auswahl!")
        exit()

    print("Suchmaschinen:")
    print("1) Google")
    print("2) DuckDuckGo")
    print("3) YouTube")

    engine_choice = input("Suchmaschine: ")
    search = input("Was möchtest du suchen? ")

    if engine_choice == "1":
        search_google(available_browsers[browser], search)
    elif engine_choice == "2":
        search_duckduckgo(available_browsers[browser], search)
    elif engine_choice == "3":
        search_youtube(available_browsers[browser], search)
    else:
        print("Ungültige Auswahl!")
        exit()

    print("Suche wurde geöffnet ✅")

# Installationsskript für GitHub
with open("install.sh", "w") as f:
    f.write("""#!/bin/bash
    echo "CLI Browser Search wird installiert..."
    sudo cp search.py /usr/local/bin/search
    sudo chmod +x /usr/local/bin/search
    echo "Installation abgeschlossen! Starte mit 'search' im Terminal."
    """)
