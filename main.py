from datetime import datetime as dt
import webbrowser as wb
import sys

time = '' # The exect time you want to join the meeting, for example: 08:15:00 (8:15 AM)
url = '' # The URL of the meeting you want to join

connected = False

while not connected:
    crt = dt.now().strftime('%H:%M:%S')

    if crt == time:
        connected = True
        wb.open(url)
        sys.exit(0)