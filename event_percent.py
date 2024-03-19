webhook_url = "ur webkook here"
interval = 1 # if any error is showing set this to 2
userid = "" # change it to ur userid

import pip
try:
    import time
    import requests

except ModuleNotFoundError:
    invalidModuleInput = input("A module was not found. Do you want to try to install all the modules? (y/n): ")
    if invalidModuleInput.lower() == "y":
        pip.main(['install', "requests"])
        pip.main(['install', "requests"])
        ask = input("Installed all the modules. Please restart the script to try again. Installation finished.")
        exit()
    else:
        ask = input("Installation finished.")
        exit()




def getUserName(userid):

    responseData = requests.get(f"https://users.roblox.com/v1/users/{userid}")

    assert responseData.status_code == 200

    username = responseData.json()['name']

    return username

current_percent = None
while True:
    try:
        resp = requests.get(f"https://badges.roblox.com/v1/users/{userid}/badges/awarded-dates?badgeIds=494124218541104,+1627409032487035,+383372909061448,+2270812053326845,+2365638641421958,+2524484866295916,+4135484921332210,+274949934966548,+4365003461198636,+661345209724224,+1319345198887520,+2405390101523433,+1297845549260160,+4471605369851248,+1294433313993410,+4458952072692430,+2204025041316467,+1365388696519737,+3604048216530746,+1006778307344708,+3462052376214650,+343455186930821,+134094038834616,+3548895558816086,+1040006371199126,+4161247087578467,+3890165791787164,+2583617475301475,+4348432740950988,+1248156187701730,+984962670920392,+2550078020756721,+1944624489758435,+1554247241410455,+2659970340026923,+2291772724254521,+1058787539781134,+2199979154597259,+2467952231976036,+2279144525349903,+403853366352411,+3038128691832836,+3287120475581904,+2530119448030987,+752494343136655,+1491637208006345,+2759322967534820,+2074373309825993,+91625828906504,+3323495840863977,+1988856830053956,+3610545440246446,+3644597344186631,+4170073808242991,+3907198305582616,+3310494142087904,+1444633010134285,+3746510072228231,+3491459325032795,+3189151177666639,+222984738107196,+1052929021736324,+977080744089986,+3454897142623403,+3973768407427753,+2844222768557843,+3343479586894918,+134181817607278,+3889590126352151,+1968121496024382,+1195935784919838,+3183430629084179,+2126304292,+2858067043515256,+363014879883870,+326973416221376,+3712682348791593,+2820172087409351,+1058253836632411,+2676085241436003,+1832660142626803,+1619180517680517,+1450333031867445,+1700770216759129,+1649143115111218,+697214652468022,+2799462321324393,+2919630202517155,+3600048773691028,+1929474479015752,+4417973491171074,+3165988561890156,+286340036168649,+2131510390543294,+546555632944216,+3942882097917743,+4304154751188194,+2212320827432860,+3382555369617502")
        #somehow the following requests is all badges (i got it from roblox.com/the-hunt)
        data = resp.json()
        badge_ids = [item["badgeId"] for item in data["data"] if "badgeId" in item]
        count_badge_ids = len(badge_ids) # this counts how much u have

        if count_badge_ids != current_percent:
            current_percent = count_badge_ids
            name = getUserName(userid)
            requests.post(webhook_url, json={"content": f"{name} completed {current_percent + 1}% ({current_percent + 1} badges) of the hunt!"}) # for some reason its 1 less than the actual value
            time.sleep(interval)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        time.sleep(60)