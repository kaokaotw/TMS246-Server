
response = sm.sendAskYesNo("Do you wish to leave the battlefield")

if response:
    sm.warpInstanceOut(940020000)