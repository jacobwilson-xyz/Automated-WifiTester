import config
import requests
import json

def sendWebhookNotification(ping, downloadSpeed, uploadSpeed, currentTime, elapsedTime, serverName, serverLocation, hostname, networkSSID, physicalLocation):
    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
        "summary": f"⚡ Speedtest Data - {hostname} via {networkSSID}",
        "sections": [{
            "activityTitle": f"⚡ Speedtest Data - {hostname} via {networkSSID}",
            "activitySubtitle": "Open for all info",
            "activityImage": "https://www.newton.ac.uk/wp-content/uploads/2023/12/ini-socmed-green-white-graphic.png",
            "facts": [{
                "name": "💓 Ping",
                "value": f"{ping}"
            }, {
                "name": "⬇️ Download",
                "value": f"{downloadSpeed}"
            }, {
                "name": "⬆️ Upload",
                "value": f"{uploadSpeed}"
            }, {
                "name": "🕒 Time",
                "value": f"{currentTime}"
            }, {
                "name": "⏱️ Elapsed",
                "value": f"{elapsedTime}"
            }, {
                "name": "🖥️ Host",
                "value": f"{serverName}"
            }, {
                "name": "🌍 Country",
                "value": f"{serverLocation}"
            }, {
                "name": "🏢 Physical Location",
                "value": f"{physicalLocation}"
            }],
            "markdown": "true"
        }]
    }

    requests.post(config.webhookURL, data=json.dumps(payload))
    print("Request Sent.")
    return

def sendWebhookNotificationLinux(ping, downloadSpeed, uploadSpeed, currentTime, elapsedTime, serverName, serverLocation, hostname, networkSSID, physicalLocation, wlanFreq, wlanRate, wlanQualityPercent, wlanSignalStrength):
    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
        "summary": f"⚡ Speedtest Data - {hostname} via {networkSSID}",
        "sections": [{
            "activityTitle": f"⚡ Speedtest Data - {hostname} via {networkSSID}",
            "activitySubtitle": "Open for all info",
            "activityImage": "https://www.newton.ac.uk/wp-content/uploads/2023/12/ini-socmed-green-white-graphic.png",
            "facts": [{
                "name": "📡 Frequency",
                "value": f"{wlanFreq}"
            }, {
                "name": "⏩ Bitrate",
                "value": f"{wlanRate}"
            },{
                "name": "📈 Signal Quality",
                "value": f"{wlanQualityPercent}"
            },{
                "name": "📶 Signal Strength",
                "value": f"{wlanSignalStrength}"
            },{
                "name": "💓 Ping",
                "value": f"{ping}"
            },{
                "name": "⬇️ Download",
                "value": f"{downloadSpeed}"
            }, {
                "name": "⬆️ Upload",
                "value": f"{uploadSpeed}"
            }, {
                "name": "🕒 Time",
                "value": f"{currentTime}"
            }, {
                "name": "⏱️ Elapsed",
                "value": f"{elapsedTime}"
            }, {
                "name": "🖥️ Host",
                "value": f"{serverName}"
            }, {
                "name": "🌍 Country",
                "value": f"{serverLocation}"
            }, {
                "name": "🏢 Physical Location",
                "value": f"{physicalLocation}"
            }],
            "markdown": "true"
        }]
    }

    requests.post(config.webhookURL, data=json.dumps(payload))
    print("Request Sent (Linux)")
    return