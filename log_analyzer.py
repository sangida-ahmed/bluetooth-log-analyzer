# Open and read the log file
with open("bluetooth_log.txt", "r") as file:
    lines = file.readlines()

# Parse each line
events = []

for line in lines:
    parts = line.strip().split(" ")
    timestamp = parts[0]
    device = parts[1]
    status = parts[2].replace(":", "")
    
    events.append({
        "timestamp": timestamp,
        "device": device,
        "status": status,
        "detail": " ".join(parts[3:]) if len(parts) > 3 else ""
    })

# Count totals
total_events = len(events)
errors = [e for e in events if e["status"] == "ERROR"]
total_errors = len(errors)
devices = set(e["device"] for e in events)
total_devices = len(devices)

# Count per device
device_summary = {}

for event in events:
    device = event["device"]
    
    if device not in device_summary:
        device_summary[device] = {"connected": 0, "errors": 0}
    
    if event["status"] == "CONNECTED":
        device_summary[device]["connected"] += 1
    elif event["status"] == "ERROR":
        device_summary[device]["errors"] += 1

# Print the report
print("====================================")
print("   BLUETOOTH LOG ANALYZER REPORT")
print("====================================")
print(f"Log File:        bluetooth_log.txt")
print(f"Total Events:    {total_events}")
print(f"Errors Found:    {total_errors}")
print(f"Devices Tested:  {total_devices}")
print()
print("CONNECTION SUMMARY:")
for device, counts in device_summary.items():
    print(f"{device:<20}{counts['connected']} connected  {counts['errors']} errors")
print()
print("ERROR DETAILS:")
for error in errors:
    print(f"[{error['timestamp']}] {error['device']} ERROR: {error['detail']}")
print("====================================")

# Save report to file
with open("bt_report.txt", "w") as report:
    report.write("====================================\n")
    report.write("   BLUETOOTH LOG ANALYZER REPORT\n")
    report.write("====================================\n")
    report.write(f"Log File:        bluetooth_log.txt\n")
    report.write(f"Total Events:    {total_events}\n")
    report.write(f"Errors Found:    {total_errors}\n")
    report.write(f"Devices Tested:  {total_devices}\n")
    report.write("\n")
    report.write("CONNECTION SUMMARY:\n")
    for device, counts in device_summary.items():
        report.write(f"{device:<20}{counts['connected']} connected  {counts['errors']} errors\n")
    report.write("\n")
    report.write("ERROR DETAILS:\n")
    for error in errors:
        report.write(f"[{error['timestamp']}] {error['device']} ERROR: {error['detail']}\n")
    report.write("====================================\n")

print()
print("Report saved to: bt_report.txt")