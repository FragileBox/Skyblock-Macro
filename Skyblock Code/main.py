import os
import requests
import json
from mojang import MojangAPI
import time
import pandas as pd

playerName = ""
UUID = MojangAPI.get_uuid(playerName)

KEY = "38b5786e-3110-4704-94c3-0cfc03199da8"

req_loc = f"https://api.hypixel.net/status?key={KEY}&uuid={UUID}"
req_col = f"https://api.hypixel.net/skyblock/profiles?key={KEY}&uuid={UUID}"

def getInfo(call):
    r = requests.get(call)
    return r.json()

def openFile():
    try:
        os.startfile("Private_Island_Macros.ahk")
    except:
        print("oops, file not found")

def closeFile():
    try:
        os.system("TASKKILL /F /IM AutoHotkeyU64.exe")
    except:
        print("oops, file not found")

Crop = "COBBLESTONE"
def execute():
    openFile()
    try:
        while True:
            try:
                col = getInfo(req_col)["profiles"][0]["members"][UUID]["collection"]
                loc = getInfo(req_loc)
                
                before_col = col[Crop]
                print("before", before_col)
                time.sleep(30)
                new_col = col[Crop]
                
                if loc.get("session").get("mode") != "dynamic":
                    break
                print("after", new_col,"\n")
                if before_col == new_col:
                    break
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
    closeFile()

execute()
