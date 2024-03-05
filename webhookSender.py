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
            "activitySubtitle": f"[{config.uniqueIdentifer}] - Open for data ouput",
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
                "value": f"{elapsedTime}s"
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
    print("Request Sent (Windows).")
    return

def sendWebhookNotificationLinux(ping, downloadSpeed, uploadSpeed, currentTime, elapsedTime, serverName, serverLocation, hostname, networkSSID, physicalLocation, wlanFreq, wlanRate, wlanQualityPercent, wlanSignalStrength):
    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
        "summary": f"⚡ Speedtest Data - {hostname} via {networkSSID}",
        "sections": [{
            "activityTitle": f"⚡ Speedtest Data - {hostname} via {networkSSID}",
            "activitySubtitle": f"[{config.uniqueIdentifer}] - Open for data ouput",
            "activityImage": "https://www.newton.ac.uk/wp-content/uploads/2023/12/ini-socmed-green-white-graphic.png",
            "facts": [{
                "name": "📡 Frequency",
                "value": f"{wlanFreq}"
            }, {
                "name": "⏩ Bitrate",
                "value": f"{wlanRate}"
            },{
                "name": "📈 Signal Quality",
                "value": f"{wlanQualityPercent}%"
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
                "value": f"{elapsedTime}s"
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

def sendTestWebhook(ping, downloadSpeed, uploadSpeed, currentTime, elapsedTime, serverName, serverLocation, hostname, networkSSID, physicalLocation, ip):
    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
        "summary": f"🟢 Device Online: '{hostname}' [{config.systemPlatform}]",
        "sections": [{
            "activityTitle": f"🟢 Device Online: '{hostname}'",
            "activitySubtitle": f"[{config.uniqueIdentifer}] - Open for data ouput",
            "activityImage": "https://www.newton.ac.uk/wp-content/uploads/2023/12/ini-socmed-green-white-graphic.png",
            "facts": [{
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
                "value": f"{elapsedTime}s"
            }, {
                "name": "🌐 SSID",
                "value": f"{networkSSID}"
            },{
                "name": "🖥️ Host",
                "value": f"{serverName}"
            }, {
                "name": "🌍 Country",
                "value": f"{serverLocation}"
            }, {
                "name": "🏢 Physical Location",
                "value": f"{physicalLocation}"
            }, {
                "name": "🏢 IP Address",
                "value": f"{ip}"
            }],
            "markdown": "true"
        }]
    }

    requests.post(config.webhookURL, data=json.dumps(payload))
    print("Request Sent (Windows)")
    return

def sendTestWebhookLinux(ping, downloadSpeed, uploadSpeed, currentTime, elapsedTime, serverName, serverLocation, hostname, networkSSID, physicalLocation, wlanFreq, wlanRate, wlanQualityPercent, wlanSignalStrength, ip):
    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
        "summary": f"🟢 Device Online: '{hostname}'",
        "sections": [{
            "activityTitle": f"🟢 Device Online: '{hostname}' [{config.systemPlatform}]",
            "activitySubtitle": f"[{config.uniqueIdentifer}] - Open for data ouput",
            "activityImage": "https://www.newton.ac.uk/wp-content/uploads/2023/12/ini-socmed-green-white-graphic.png",
            "facts": [{
                "name": "📡 Frequency",
                "value": f"{wlanFreq}"
            }, {
                "name": "⏩ Bitrate",
                "value": f"{wlanRate}"
            },{
                "name": "📈 Signal Quality",
                "value": f"{wlanQualityPercent}%"
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
                "value": f"{elapsedTime}s"
            }, {
                "name": "🌐 SSID",
                "value": f"{networkSSID}"
            },{
                "name": "🖥️ Host",
                "value": f"{serverName}"
            }, {
                "name": "🌍 Country",
                "value": f"{serverLocation}"
            }, {
                "name": "🏢 Physical Location",
                "value": f"{physicalLocation}"
            }, {
                "name": "🏢 IP Address",
                "value": f"{ip}"
            }],
            "markdown": "true"
        }]
    }

    requests.post(config.webhookURL, data=json.dumps(payload))
    print("Request Sent (Linux)")
    return
