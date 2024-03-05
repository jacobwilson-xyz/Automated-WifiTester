import webhookSender
import config
import subprocess
import speedtest
import datetime
import schedule
import time
import sys

print("Initialising ...")


def systemCompatitbilityCheck():
    if config.systemPlatform in ['Windows', 'Linux']:
        print(f"{config.systemPlatform} OS Identified, continuing")
        return
    else:
        print(f"Unsupported Operating System: {config.systemPlatform} Exiting...")
        sys.exit()
        

print("Checking system ...")  
systemCompatitbilityCheck()
def runTest():
    startTime = time.time()

    if config.systemPlatform == "Linux":
        iwRAW = subprocess.run('iwconfig', capture_output=True, text=True)
        iwOut = iwRAW.stdout

        wlan = iwOut.split(config.wlan, 1)[1]

        wlanSSID = wlan.split("ESSID:", 1)[1].split("Mode", 1)[0].split("\"")[1].split("\"\n")[0]
        wlanFreq = wlan.split("Frequency:", 1)[1].split("GHz", 1)[0] + "GHz"
        wlanRate = wlan.split("Bit Rate=", 1)[1].split("Mb/s", 1)[0] + "Mb/s"
        wlanQuality = wlan.split("Link Quality=", 1)[1].split("Signal level", 1)[0].split(" ", 1)[0]
        wlanQualityFirst = wlanQuality.split("/")[0]
        wlanQualitySecond = wlanQuality.split("/")[1]
        wlanQualityPercent = round(int(wlanQualityFirst) / int(wlanQualitySecond) * 100, 1)
        wlanSignalStrength = wlan.split("Signal level=", 1)[1].split(" dBm")[0] + "dBm"


    test = speedtest.Speedtest(secure=True)
    test.get_servers()
    bestServer = test.get_best_server()

    downloadResultRAW = test.download()
    uploadResultRAW = test.upload()
    pingResultRAW = test.results.ping

    downloadResult = str(f"{downloadResultRAW / 1024 / 1024:.2f}Mbit/s")
    uploadResult = str(f"{uploadResultRAW / 1024 / 1024:.2f}Mbit/s")
    pingResult = str(f"{pingResultRAW}ms")
    endTime = time.time()
    elapsedTime = endTime - startTime
    currentTime = datetime.datetime.now()

    print(f"Ping: {pingResult}\nDownload: {downloadResult}\nUpload: {uploadResult}\nCurrent Time: {currentTime}\nElapsed Time: {round(elapsedTime, 2)}\nHost: {bestServer['host']}\nCountry:{bestServer['country']}\nDevice:{config.deviceName}\nLocal Network: {config.ssid}")
    if config.systemPlatform == "Linux":
        webhookSender.sendWebhookNotificationLinux(pingResult, downloadResult, uploadResult, currentTime, round(elapsedTime, 2), bestServer['host'], bestServer['country'], config.deviceName, wlanSSID, config.location, wlanFreq, wlanRate, wlanQualityPercent, wlanSignalStrength)
    else:
        webhookSender.sendWebhookNotification(pingResult, downloadResult, uploadResult, currentTime, round(elapsedTime, 2), bestServer['host'], bestServer['country'], config.deviceName, config.ssid, config.location)
    print("Complete. Returning to Schedule")
    return


schedule.every().day.at("09:00").do(runTest)
print("[LIVE] Schedule Everyday at 09:00")
schedule.every().day.at("13:00").do(runTest)
print("[LIVE] Schedule Everyday at 13:00")
schedule.every().day.at("17:00").do(runTest)
print("[LIVE] Schedule Everyday at 17:00")

if config.testMode == True:
    print("Test Mode Enabled... Testing..")
    runTest()
    print("Test Complete... Continuing as normal")

print("Running...")
while True:
    schedule.run_pending()
    time.sleep(60)
 
