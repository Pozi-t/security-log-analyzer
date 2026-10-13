import re

class LogParser:

    def parse(self, log_line):

        timestamp_result = re.search(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}", log_line)
        level_result = re.search(r"\d{2}:\d{2}:\d{2}\s(DEBUG|ERROR|WARNING|INFO)\b", log_line)
        event_result = re.search(r"(Login\s.*?)\suser", log_line)
        user_result = re.search(r"user=(\w+)", log_line)
        ip_result = re.search(r"ip=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", log_line)



        if timestamp_result and level_result:
            return {
                "timestamp": timestamp_result.group(0),
                "level": level_result.group(1),
                "event": event_result.group(1) if event_result else None,
                "user": user_result.group(1) if user_result else None,
                "ip": ip_result.group(1) if ip_result else None,
            }
        else:
            return None