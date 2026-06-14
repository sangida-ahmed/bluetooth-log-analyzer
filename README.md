# Bluetooth Log Analyzer

## Why I built this
I wanted to build a tool that mirrors 
what QA engineers actually do: analyze device logs, find failure 
patterns, and generate structured reports.

This tool reads a Bluetooth test log file, parses each event, 
identifies errors by device, and automatically saves a 
professional QA report. This is the same workflow used when 
validating Bluetooth accessories like AirPods, Beats headphones, 
and wireless devices before they ship to customers.

## What it does
- Reads any Bluetooth log file from the command line
- Parses timestamps, device names, and connection statuses
- Counts total events, errors, and unique devices tested
- Calculates error rate percentage per device
- Automatically flags devices exceeding 20% error rate
- Lists all errors with timestamps and details
- Generates actionable recommendations
- Saves the report to a file automatically with timestamp

## How to run
```bash
python3 log_analyzer.py bluetooth_log.txt
```
Works with any Bluetooth log file.

## Sample Output
```
====================================
   BLUETOOTH LOG ANALYZER REPORT
   Generated: 2026-06-14 10:38:01
====================================
Log File:        bluetooth_log.txt
Total Events:    20
Errors Found:    4
Devices Tested:  3

CONNECTION SUMMARY:
Device_A            6 connected  1 errors  (14.3% error rate)
Device_B            5 connected  2 errors  (28.6% error rate)  ⚠️  HIGH ERROR RATE
Device_C            5 connected  1 errors  (16.7% error rate)

ERROR DETAILS:
[10:03:21] Device_A ERROR: Pairing timeout
[10:07:45] Device_B ERROR: Connection dropped
[10:12:33] Device_B ERROR: Authentication failed
[10:18:02] Device_C ERROR: Signal too weak

RECOMMENDATIONS:
⚠️  Device_B requires immediate attention — error rate exceeds 20%
====================================
Report saved to: bt_report.txt
```
## Skills used
Python • File I/O • String parsing • Dictionaries • 
List comprehensions • Data analysis • Report generation
