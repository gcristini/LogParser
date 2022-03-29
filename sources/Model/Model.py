
class Model():
    def __init__(self):
        self._log_file_raw = None
        self._log_file_filtered = None
        self._log_file_to_display = None
        return

    @property
    def log_file_raw(self):
        return self._log_file_raw

    @log_file_raw.setter
    def log_file_raw(self, log_file):
        self._log_file_raw = log_file

    @property
    def log_file_filtered(self):
        return self._log_file_filtered

    @log_file_filtered.setter
    def log_file_raw(self, log_file):
        self._log_file_filtered = log_file

    @property
    def log_file_to_display(self):
        return self.log_file_to_display

    @log_file_to_display.setter
    def log_file_raw(self, log_file):
        self.log_file_to_display = log_file


    def import_log(self, file_name: str):
        self._log_file_raw = open(file_name, "r")       
        self._log_file_to_display = self._log_file_raw
        return self._log_file_to_display

    # def export_file():
    #     return

    # def search(words):
    #     return

    # def get_log_to_display():        
    #     return _log_file_to_display

