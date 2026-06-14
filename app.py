from flask import Flask, render_template, request
import sys
from datetime import datetime

app = Flask(__name__)

def analyze_log(lines):
    events = []
    for line in lines:
        parts = line.strip().split(" ")
        if len(parts) < 3:
            continue
        timestamp = parts[0]
        device = parts[1]
        status = parts[2].replace(":", "")
        events.append({
            "timestamp": timestamp,
            "device": device,
            "status": status,
            "detail": " ".join(parts[3:]) if len(parts) > 3 else ""
        })

    total_events = len(events)
    errors = [e for e in events if e["status"] == "ERROR"]
    total_errors = len(errors)
    devices = set(e["device"] for e in events)
    total_devices = len(devices)

    device_summary = {}
    for event in events:
        device = event["device"]
        if device not in device_summary:
            device_summary[device] = {"connected": 0, "errors": 0}
        if event["status"] == "CONNECTED":
            device_summary[device]["connected"] += 1
        elif event["status"] == "ERROR":
            device_summary[device]["errors"] += 1

    for device, counts in device_summary.items():
        total = counts["connected"] + counts["errors"]
        counts["error_rate"] = round((counts["errors"] / total) * 100, 1)
        counts["flagged"] = counts["error_rate"] > 20

    recommendations = [d for d, c in device_summary.items() if c["flagged"]]

    return {
        "total_events": total_events,
        "total_errors": total_errors,
        "total_devices": total_devices,
        "device_summary": device_summary,
        "errors": errors,
        "recommendations": recommendations,
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    filename = None
    if request.method == "POST":
        file = request.files["logfile"]
        filename = file.filename
        lines = file.read().decode("utf-8").splitlines()
        report = analyze_log(lines)
    return render_template("index.html", report=report, filename=filename)

if __name__ == "__main__":
    app.run(debug=True)