"""Structured JSON output logger."""
import json, time
def log_event(event_type, payload):
    record = {'timestamp': time.time(), 'event': event_type, 'data': payload}
    print(json.dumps(record))
