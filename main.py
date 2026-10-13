from src.log_parser import LogParser
from src.log_reader import LogReader
from src.analyzer import SecurityAnalyzer
from src.reporter import Reporter

file_path = "data/sample.log"

try:
    reader = LogReader(file_path)
    parser = LogParser()
    reporter = Reporter("reports/report.json", "reports/suspicious_ips.csv")
    parsed_logs = []

    for line in reader.read_logs():
        parsed_logs.append(parser.parse(line))

    analyzer = SecurityAnalyzer(parsed_logs)

    events = analyzer.count_events()
    suspicious_ips = analyzer.find_suspicious_ips()

    reporter.save_json({
        "events": events,
        "suspicious_ips": suspicious_ips,
    })

    reporter.save_csv(suspicious_ips)

    print("Анализ завершён!")
    print(f"Всего событий: {events['all']}")
    print(f"Подозрительных IP: {len(suspicious_ips)}")
    print("Отчёты сохранены в папке reports/")
except FileNotFoundError as error:
    print(error)