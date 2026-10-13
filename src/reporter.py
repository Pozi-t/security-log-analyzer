import json
import csv
from pathlib import Path

class Reporter:
    def __init__(self, file_path_json, file_path_csv):
        self._file_path_csv = file_path_csv
        self._file_path_json = file_path_json

    @property
    def file_path_json(self):
        return self._file_path_json
    @file_path_json.setter
    def file_path_json(self, file_path):
        self._file_path_json = file_path

    @property
    def file_path_csv(self):
        return self._file_path_csv

    @file_path_csv.setter
    def file_path_csv(self, file_path):
        self._file_path_csv = file_path

    def save_json(self, data):
        self._create_directory(self.file_path_json)

        with open(self.file_path_json, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def save_csv(self, data):
        self._create_directory(self.file_path_csv)

        rows = []

        for ip, count in data.items():
            rows.append({"ip": ip, "failed_attempts": count})

        with open(self.file_path_csv, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, ["ip", "failed_attempts"])

            writer.writeheader()
            writer.writerows(rows)

    def _create_directory(self, file_path):
        direct = Path(file_path).parent
        direct.mkdir(parents=True, exist_ok=True)