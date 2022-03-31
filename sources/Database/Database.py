
class Database():
    
    def __init__(self):        
        self._log_file_raw = list()
        self._log_file_filtered_buffer = list()
        self._log_file_to_display = list()

        return

    @property
    def log_file_raw(self):
        return self._log_file_raw

    @log_file_raw.setter
    def log_file_raw(self, log_file):
        self._log_file_raw = log_file

    @property
    def log_file_filtered_buffer(self):
        return self._log_file_filtered_buffer

    def append_to_log_file_filtered_buffer(self, log_file):
        self._log_file_filtered_buffer.append(log_file)

    def pop_from_log_file_filtered_buffer(self, index=-1):
        return self._log_file_filtered_buffer.pop(index)

    @property
    def log_file_to_display(self):
        return self._log_file_to_display

    @log_file_to_display.setter
    def log_file_to_display(self, log_file):
        self._log_file_to_display = log_file
