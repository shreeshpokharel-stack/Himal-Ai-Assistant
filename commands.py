import os
import webbrowser
import subprocess


def execute_command(command):

    command = command.lower().strip()

    if command.startswith("open "):

        target = command.replace("open ", "").strip()

        aliases = {
            "nodepad": "notepad",
            "note pad": "notepad",
            "whats app": "whatsapp",
            "spotfy": "spotify"
        }

        target = aliases.get(target, target)

        # Notepad
        if target == "notepad":
            subprocess.Popen("notepad.exe")
            return "Opening Notepad..."

        # Calculator
        if target == "calculator":
            subprocess.Popen("calc.exe")
            return "Opening Calculator..."

        # Paint
        if target == "paint":
            subprocess.Popen("mspaint.exe")
            return "Opening Paint..."

        # CMD
        if target == "cmd":
            subprocess.Popen("cmd.exe")
            return "Opening CMD..."

        # Chrome
        if target == "chrome":

            chrome_paths = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            ]

            for path in chrome_paths:
                if os.path.exists(path):
                    subprocess.Popen(path)
                    return "Opening Chrome..."

            return "Chrome not found."

        # Spotify
        if target == "spotify":
            os.system("start spotify:")
            return "Opening Spotify..."

        # WhatsApp
        if target == "whatsapp":
            os.system("start whatsapp:")
            return "Opening WhatsApp..."

        # Fallback search
        webbrowser.open(
            f"https://www.google.com/search?q={target}"
        )

        return f"Searching Google for {target}"

    elif command == "youtube":
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif command == "google":
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif command == "shutdown":
        os.system("shutdown /s /t 1")
        return "Shutting down..."

    elif command == "restart":
        os.system("shutdown /r /t 1")
        return "Restarting..."

    return "Command not recognized."