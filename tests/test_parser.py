from src.log_parser import LogParser


def test_parse_valid_log():
    parser = LogParser()
    log_line = "2026-10-11 10:15:21 INFO Login successful user=admin ip=192.168.1.10"
    answer = parser.parse(log_line)
    true_answer = {
        "timestamp": "2026-10-11 10:15:21",
        "level": "INFO",
        "event": "Login successful",
        "user": "admin",
        "ip": "192.168.1.10"
    }

    assert answer == true_answer

def test_parse_missing_optional_fields():
    parser = LogParser()
    log_line = "2026-10-11 10:15:21 INFO"
    answer = parser.parse(log_line)
    true_answer = {
        "timestamp": "2026-10-11 10:15:21",
        "level": "INFO",
        "event": None,
        "user": None,
        "ip": None
    }

    assert answer == true_answer

def test_parse_invalid_log():
    parser = LogParser()
    log_line = "Некорректная строка лога"
    answer = parser.parse(log_line)
    assert answer is None

def test_parse_invalid_log2():
    parser = LogParser()
    log_line = "2026-10-11 10:15:21 Login successful user=admin ip=192.168.1.10"
    answer = parser.parse(log_line)
    assert answer is None