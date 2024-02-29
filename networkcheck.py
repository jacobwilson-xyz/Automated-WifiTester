import credentials
import speedtest
import datetime
import schedule
import requests
import socket
import json
import time


def sendWebhookNotification(ping, downloadSpeed, uploadSpeed, currentTime, elapsedTime, serverName, serverLocation, hostname, currentNetwork):
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
                            "text": f"⚡ Speedtest Data - {hostname} via {currentNetwork}"
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
                        }
                    ]
                }
            }
        ]
    }

    requests.post(credentials.webhookurl, data=json.dumps(payload))


def runTest():
    startTime = time.time()
    test = speedtest.Speedtest()
    servers = [19019]
    test.get_servers(servers)
    bestServer = test.get_best_server()

    downloadResultRAW = test.download()
    uploadResultRAW = test.upload()
    pingResultRAW = test.results.ping

    downloadResult = str(f"{downloadResultRAW / 1024 / 1024:.2f}Mbit/s")
    uploadResult = str(f"{uploadResultRAW / 1024 / 1024:.2f}Mbit/s")
    pingResult = str(f"{pingResultRAW}ms")
    localHostname = socket.gethostname()
    endTime = time.time()
    elapsedTime = endTime - startTime
    currentTime = datetime.datetime.now()

    sendWebhookNotification(pingResult, downloadResult, uploadResult, currentTime, round(elapsedTime, 2), bestServer['host'], bestServer['country'], localHostname, currentNetwork)


schedule.every().day.at("09:00").do(runTest)
schedule.every().day.at("13:00").do(runTest)
schedule.every().day.at("17:00").do(runTest)

while True:
    schedule.run_pending()
    time.sleep(60)
 