
class Model():
    def __init__(self):
        self._log_file_raw = list();
        self._log_file_filtered = list()
        self._log_file_to_display = ""
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
        self.__clear_buffers()

        with open(file_name, "r") as file:
            self._log_file_raw = file.readlines()

            # Concat all lines to good format for view
            for line in self._log_file_raw:
                self._log_file_to_display+=line

        return self._log_file_to_display

    def filter_log(self, words:list):        
        self._log_file_filtered=list()
        self._log_file_to_display=""

        for line in self._log_file_raw:
            word_found_counter = 0
            for word in words:
                if word in line:
                    word_found_counter +=1
                
            if word_found_counter == len(words):
                self._log_file_filtered.append(line)
                pass

        # Concat all lines to good format for view
        for line in self._log_file_filtered:
            self._log_file_to_display+=line

        return self._log_file_to_display


    # def export_file():
    #     return

    # def search(words):
    #     return

    # def get_log_to_display():        
    #     return _log_file_to_display


    def __clear_buffers(self):
        self._log_file_raw = list()
        self._log_file_filtered = list()
        self._log_file_to_display = ""