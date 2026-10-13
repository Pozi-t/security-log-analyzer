class LogReader:

    def __init__(self, file_path):
        self._file_path = file_path

    @property
    def file_path(self):
        return self._file_path
    @file_path.setter
    def file_path(self, file_path):
        self._file_path = file_path

    def read_logs(self):
        logs = []

        try:
            with open(self._file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    logs.append(line.strip())

            return logs
        except FileNotFoundError:
            # print(f"Файл не найден {self.file_path}")
            raise FileNotFoundError(f"Файл не найден: {self._file_path}")
