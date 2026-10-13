from src.analyzer import SecurityAnalyzer
from src.log_parser import LogParser

def test_count_events():
    parser = LogParser()
    true_answer ={
        "Login successful": 2,
        "Login failed": 1,
        "all": 3
    }
    parsed_logs = []
    logs = ["2026-10-11 10:16:05 WARNING Login failed user=admin ip=185.10.20.30",
            "2026-10-11 10:17:11 INFO Login successful user=user1 ip=192.168.1.15",
            "2026-10-11 10:19:45 INFO Login successful user=guest ip=192.168.1.20",
            ]
    for line in logs:
        parsed_logs.append(parser.parse(line))

    analyzer = SecurityAnalyzer(parsed_logs)

    assert analyzer.count_events() == true_answer

def test_count_failed_attempts_by_ip():
    parser = LogParser()
    true_answer ={
        "185.10.20.30": 2,
        "45.12.33.21": 1
    }
    parsed_logs = []
    logs = ["2026-10-11 10:16:05 WARNING Login failed user=admin ip=185.10.20.30",
            "2026-10-11 10:17:11 WARNING Login failed user=user1 ip=185.10.20.30",
            "2026-10-11 10:19:45 WARNING Login failed user=guest ip=45.12.33.21",
            "2026-10-11 10:20:23 INFO Login successful user=guest ip=192.168.1.10",
            ]
    for line in logs:
        parsed_logs.append(parser.parse(line))

    analyzer = SecurityAnalyzer(parsed_logs)

    assert analyzer.count_failed_attempts_by_ip() == true_answer


def test_find_suspicious_ips():
    parser = LogParser()
    true_answer ={
        "45.12.33.21": 4
    }
    parsed_logs = []
    logs = ["2026-10-11 10:16:05 WARNING Login failed user=admin ip=185.10.20.30",
            "2026-10-11 10:17:11 WARNING Login failed user=user1 ip=185.10.20.30",
            "2026-10-11 10:19:45 WARNING Login failed user=guest ip=45.12.33.21",
            "2026-10-11 10:19:45 WARNING Login failed user=guest ip=45.12.33.21",
            "2026-10-11 10:19:45 WARNING Login failed user=guest ip=45.12.33.21",
            "2026-10-11 10:19:45 WARNING Login failed user=guest ip=45.12.33.21",
            "2026-10-11 10:20:23 INFO Login successful user=guest ip=192.168.1.10",
            ]
    for line in logs:
        parsed_logs.append(parser.parse(line))

    analyzer = SecurityAnalyzer(parsed_logs)

    assert analyzer.find_suspicious_ips() == true_answer

def test_find_suspicious_ips_argument():
    parser = LogParser()
    true_answer ={
        "185.10.20.30": 2,
        "45.12.33.21": 3
    }
    parsed_logs = []
    logs = ["2026-10-11 10:16:05 WARNING Login failed user=admin ip=185.10.20.30",
            "2026-10-11 10:17:11 WARNING Login failed user=user1 ip=185.10.20.30",
            "2026-10-11 10:19:45 WARNING Login failed user=guest ip=45.12.33.21",
            "2026-10-11 10:19:45 WARNING Login failed user=guest ip=45.12.33.21",
            "2026-10-11 10:19:45 WARNING Login failed user=guest ip=45.12.33.21",
            "2026-10-11 10:20:23 INFO Login successful user=guest ip=192.168.1.10",
            ]
    for line in logs:
        parsed_logs.append(parser.parse(line))

    analyzer = SecurityAnalyzer(parsed_logs)

    assert analyzer.find_suspicious_ips(2) == true_answer