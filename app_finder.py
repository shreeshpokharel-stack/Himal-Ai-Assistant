import os


def find_app(app_name):

    common_apps = {
        "spotify": [
            os.path.expandvars(
                r"%APPDATA%\Spotify\Spotify.exe"
            ),
            os.path.expandvars(
                r"%LOCALAPPDATA%\Microsoft\WindowsApps\Spotify.exe"
            )
        ],

        "whatsapp": [
            os.path.expandvars(
                r"%LOCALAPPDATA%\WhatsApp\WhatsApp.exe"
            ),
            os.path.expandvars(
                r"%LOCALAPPDATA%\Microsoft\WindowsApps\WhatsApp.exe"
            )
        ]
    }

    if app_name in common_apps:

        for path in common_apps[app_name]:

            if os.path.exists(path):
                return path

    return None