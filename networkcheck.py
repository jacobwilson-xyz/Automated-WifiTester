import credentials
import speedtest
import datetime
import schedule
import requests
import json
import time

print("Initialising ...")

def sendWebhookNotification(ping, downloadSpeed, uploadSpeed, currentTime, elapsedTime, serverName, serverLocation, hostname, networkSSID, physicalLocation):
    payload = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "body": [
                        {
                            "type": "TextBlock",
                            "size": "Large",
                            "weight": "Bolder",
                            "text": f"⚡ Speedtest Data - {hostname} via {networkSSID}"
                        },
                        {
                            "type": "TextBlock",
                            "size": "Medium",
                            "weight": "Bolder",
                            "text": f"💓 **Ping:** {ping}"
                        },
                        {
                            "type": "TextBlock",
                            "text": f"⬇️ **Download:** {downloadSpeed}"
                        },
                        {
                            "type": "TextBlock",
                            "text": f"⬆️ **Upload:** {uploadSpeed}"
                        },
                        {
                            "type": "TextBlock",
                            "text": f"🕒 **Time:** {currentTime}"
                        },
                        {
                            "type": "TextBlock",
                            "text": f"⏱️ **Elapsed:** {elapsedTime}s"
                        },
                        {
                            "type": "TextBlock",
                            "text": f"🖥️ **Host:** {serverName}"
                        },
                        {
                            "type": "TextBlock",
                            "text": f"🌍 **Country:** {serverLocation}"
                        },
                        {
                            "type": "TextBlock",
                            "text": f"🏢 **Physical Location:** {physicalLocation}"
                        }
                    ]
                }
            }
        ]
    }

    requests.post(credentials.webhookurl, data=json.dumps(payload))
    print("Request Sent.")


def runTest():
    startTime = time.time()
    test = speedtest.Speedtest()
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

    print(f"Ping: {pingResult}\nDownload: {downloadResult}\nUpload: {uploadResult}\nCurrent Time: {currentTime}\nElapsed TIme: {round(elapsedTime, 2)}\nHost: {bestServer['host']}\nCountry:{bestServer['country']}\nDevice:{credentials.deviename}\nLocal Network: {credentials.ssid}")
    sendWebhookNotification(pingResult, downloadResult, uploadResult, currentTime, round(elapsedTime, 2), bestServer['host'], bestServer['country'], credentials.devicename, credentials.ssid, credentials.location)


schedule.every().day.at("09:00").do(runTest)
print("[LIVE] Schedule Everyday at 09:00")
schedule.every().day.at("13:00").do(runTest)
print("[LIVE] Schedule Everyday at 13:00")
schedule.every().day.at("17:00").do(runTest)
print("[LIVE] Schedule Everyday at 17:00")

if credentials.testmode == True:
    print("Test Mode Enabled... Testing..")
    runTest()
    print("Test Complete... Continuing as normal")

print("Running...")
while True:
    schedule.run_pending()
    time.sleep(60)
 