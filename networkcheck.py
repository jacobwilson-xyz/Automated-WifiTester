import webhookSender
import config
import subprocess
import speedtest
import datetime
import schedule
import socket
import base64
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

testComplete = False

def runNetworkCheck():
    startTime = time.time()

    if config.systemPlatform == "Linux":
        ipOUT = ""
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

        if config.displayDeviceIP:
            ipRAW = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
            ipOUT = ipRAW.stdout
            if config.encodeDeviceIP:
                ipEncoded = ipOUT.encode('utf-8')
                ipEncoded = base64.b64encode(ipEncoded)
                ipOUT = ipEncoded.decode('utf-8')
                print("IP Address Encoded...")
        else:
            ipOUT = "Hidden"


    if config.systemPlatform == "Windows":
        ipOUT = ""
        if config.displayDeviceIP:
            ipRAW = socket.gethostbyname_ex(socket.gethostname())[-1]
            if config.encodeDeviceIP:
                ipRAW = [base64.b64encode(s.encode('utf-8')).decode('utf-8') for s in ipRAW]
                print("IP Address Encoded...")

            for ips in ipRAW:
                ipOUT = ipOUT + f"{ips} "
            
        else:
            ipOUT = "Hidden"
    
    print(f"Running on {ipOUT}")

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
        if config.testMode is True and testComplete is False:
            webhookSender.sendTestWebhookLinux(pingResult, downloadResult, uploadResult, currentTime, round(elapsedTime, 2), bestServer['host'], bestServer['country'], config.deviceName, wlanSSID, config.location, wlanFreq, wlanRate, wlanQualityPercent, wlanSignalStrength, ipOUT)
        else:
            webhookSender.sendWebhookNotificationLinux(pingResult, downloadResult, uploadResult, currentTime, round(elapsedTime, 2), bestServer['host'], bestServer['country'], config.deviceName, wlanSSID, config.location, wlanFreq, wlanRate, wlanQualityPercent, wlanSignalStrength)
    else:
        if config.testMode is True and testComplete is False:
            webhookSender.sendTestWebhook(pingResult, downloadResult, uploadResult, currentTime, round(elapsedTime, 2), bestServer['host'], bestServer['country'], config.deviceName, config.ssid, config.location, ipOUT)
        else:
            webhookSender.sendWebhookNotification(pingResult, downloadResult, uploadResult, currentTime, round(elapsedTime, 2), bestServer['host'], bestServer['country'], config.deviceName, config.ssid, config.location)
    print("Complete. Returning to Schedule")
    return


schedule.every().day.at("09:00").do(runNetworkCheck)
print("[LIVE] Schedule Everyday at 09:00")
schedule.every().day.at("13:00").do(runNetworkCheck)
print("[LIVE] Schedule Everyday at 13:00")
schedule.every().day.at("17:00").do(runNetworkCheck)
print("[LIVE] Schedule Everyday at 17:00")

if config.testMode == True:
    print("Test Mode Enabled... Testing..")
    runNetworkCheck()
    print("Test Complete... Continuing as normal")

print("Running...")
while True:
    schedule.run_pending()
    time.sleep(60)
 
