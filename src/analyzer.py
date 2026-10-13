from collections import Counter

class SecurityAnalyzer:

    def __init__(self, logs):
        self._logs = logs

    def count_events(self):
        answer = {
            "Login successful" : 0,
            "Login failed" : 0,
            "all": 0
        }

        for log_line in self._logs:
            if log_line is None:
                continue
            if log_line["event"] is None:
                continue
            if log_line["event"] in ("Login successful", "Login failed"):
                answer[log_line["event"]] += 1
                answer["all"] += 1

        return answer

    def count_failed_attempts_by_ip(self):
        ips = []
        for log_line in self._logs:
            if log_line is None:
                continue
            if log_line["event"] is None or log_line["ip"] is None:
                continue
            if log_line["event"] == "Login failed":
                ips.append(log_line["ip"])
        return Counter(ips)

    def find_suspicious_ips(self, threshold = 3):
        dangerous_ips = {}
        for ip, count in self.count_failed_attempts_by_ip().items():
            if count >= threshold:
                dangerous_ips[ip] = count

        return dangerous_ips

