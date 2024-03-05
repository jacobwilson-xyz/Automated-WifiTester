import platform

# Webhook URL for POST Requests
webhookURL = "https://universityofcambridgecloud.webhook.office.com/webhookb2/2ac35c1a-495e-4253-89c8-e2f3cccb45ed@49a50445-bdfa-4b79-ade3-547b4f3986e9/IncomingWebhook/117f84ecd8d0473f9e5620b1c8720543/8f46ee48-0ba3-4fbf-893c-b1d9703170c0"
# Network SSID - Set automatically
ssid = "UniOfCam-IoT"
# Physical Building Location
location = "Room X00"
# Test Mode - Triggers a speedtest on boot
testMode = False
# Device Name
deviceName = "Unset"
# Device OS Name, 'Linux' or 'Windows' supported.
# systemPlatform = "Linux"
systemPlatform = platform.system()
# Which wlan to use for testing - For Linux
wlan = "wlan1"