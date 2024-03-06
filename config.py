import platform
import uuid

# Webhook URL for POST Requests
webhookURL = "Webhook URL"
# Network SSID - Set automatically on Linux
ssid = "SSID"
# Physical Building Location
location = "Location"
# Test Mode - Triggers a speedtest on boot
testMode = True
# Device Name
deviceName = "Device"
# Runtime interval in seconds
testInterval = 3600
# Device OS Name, 'Linux' or 'Windows' supported. You can use systemPlatform = "Linux"
systemPlatform = platform.system()
# Which wlan to use for testing - For Linux
wlan = "wlan0"
# Display IP on startup for SSH Purposes (Linux).
displayDeviceIP = False
encodeDeviceIP = False
# Random UUID each session for better tracking of mutliple devices
uniqueIdentifer = str(uuid.uuid4())[:4]
