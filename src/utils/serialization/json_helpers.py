"""JSON serializer with ISO datetime support."""
import json, datetime
class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime.date, datetime.datetime)): return o.isoformat()
        return super().default(o)
