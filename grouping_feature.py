# Initializing the feature_names list from user's provided data
feature_names = [
    "Quick Charge", "Dash Charge", "SuperCharge", "Warp Charge", "TurboPower",
    "Retina Display", "Super AMOLED", "OLED", "Liquid Retina", "Infinity Display",
    "IP68", "IP67", "Water-repellent", "Waterproof", "Dustproof",
    "Selfie Camera", "Front-facing Camera", "Secondary Camera",
    "Night Sight", "Bright Night", "Night Mode",
    "Face Unlock", "Face ID", "Facial Recognition Unlock",
    "Infinity-O Display", "Notch Display", "Punch-hole Display", "Waterdrop Notch",
    "Air Actions", "Motion Sense", "Raise to Wake",
    "Qi Wireless Charging", "AirPower", "Reverse Wireless Charging", "PowerShare",
    "S Pen", "Apple Pencil", "Stylus Pen",
    "5G Connectivity", "Dual SIM", "Expandable Storage", "HDR10 Playback", "Dolby Atmos Sound",
    "In-display Fingerprint", "Gorilla Glass", "Pop-up Camera", "Ultrawide Lens", "Macro Camera",
    "Optical Zoom", "AI Camera", "Stereo Speakers", "Wireless DeX", "FM Radio",
    "USB Type-C", "One UI", "Oxygen OS", "Zen UI", "IR Blaster",
    "NFC", "Bluetooth 5.0", "Under-display Camera", "ARCore Support", "Always-On Display",
    "Speed Dial", "Caller ID", "Call Waiting", "Voice Mail", "Three-way Calling",
    "Hold Music", "Cordless", "Redial", "Flash", "Backlit Keypad",
    "Volume Control", "Speakerphone", "Mute Button", "Pulse/Tone Switching", "Wall Mountable",
    "Battery Backup", "Built-in Answering Machine", "Headset Jack", "Memory Dial", "Ringer Modes",
    "Call Blocking", "Call Forwarding", "Visual Ringer", "Desk or Wall Mount", "Cord Storage",
    "Call Timer", "Page/Intercom", "Alarm/Reminder", "Adjustable Ringer Volume", "LED Status Indicator"
]


categories = {
    "Charging Technologies": [
        "Quick Charge", "Dash Charge", "SuperCharge", "Warp Charge", "TurboPower",
        "Qi Wireless Charging", "AirPower", "Reverse Wireless Charging", "PowerShare"
    ],
    "Display Technologies": [
        "Retina Display", "Super AMOLED", "OLED", "Liquid Retina", "Infinity Display",
        "Infinity-O Display", "Notch Display", "Punch-hole Display", "Waterdrop Notch", "Always-On Display"
    ],
    "Water and Dust Resistance": [
        "IP68", "IP67", "Water-repellent", "Waterproof", "Dustproof"
    ],
    "Camera Technologies": [
        "Selfie Camera", "Front-facing Camera", "Secondary Camera",
        "Night Sight", "Bright Night", "Night Mode", "In-display Fingerprint",
        "Pop-up Camera", "Ultrawide Lens", "Macro Camera", "Optical Zoom", "AI Camera", "Under-display Camera"
    ],
    "Unlocking Mechanisms": [
        "Face Unlock", "Face ID", "Facial Recognition Unlock"
    ],
    "Sound and Audio": [
        "HDR10 Playback", "Dolby Atmos Sound", "Stereo Speakers", "Wireless DeX", "FM Radio"
    ],
    "Connectivity and Networking": [
        "5G Connectivity", "Dual SIM", "Expandable Storage", "USB Type-C", "NFC", "Bluetooth 5.0", "IR Blaster", "ARCore Support"
    ],
    "Software and UI": [
        "One UI", "Oxygen OS", "Zen UI"
    ],
    "Physical Features": [
        "S Pen", "Apple Pencil", "Stylus Pen", "Gorilla Glass", "Air Actions", "Motion Sense", "Raise to Wake"
    ],
    "Calling Features": [
        "Speed Dial", "Caller ID", "Call Waiting", "Voice Mail", "Three-way Calling",
        "Hold Music", "Cordless", "Redial", "Flash", "Backlit Keypad",
        "Volume Control", "Speakerphone", "Mute Button", "Pulse/Tone Switching", "Wall Mountable",
        "Battery Backup", "Built-in Answering Machine", "Headset Jack", "Memory Dial", "Ringer Modes",
        "Call Blocking", "Call Forwarding", "Visual Ringer", "Desk or Wall Mount", "Cord Storage",
        "Call Timer", "Page/Intercom", "Alarm/Reminder", "Adjustable Ringer Volume", "LED Status Indicator"
    ],
    "Other Features": []
}


# Re-run the categorization process
# Finding features that haven't been categorized
for feature in feature_names:
    found = False
    for category, features in categories.items():
        if feature in features:
            found = True
            break
    if not found:
        categories["Other Features"].append(feature)

# Creating the output structure
output = [{"feature_name": feature, "generic_name": category} for category, features in categories.items() for feature in features]

output
