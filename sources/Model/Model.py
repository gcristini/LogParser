

from tkinter.filedialog import asksaveasfile, asksaveasfilename


class Model():    
    __files_extensions = [("All Files", "*.*"),
                          ("Comma Separated File", "*.csv"),
                          ("Text Document", "*.txt")]
    
    
    def __init__(self, database):        
        self.db = database
        return

    def import_log(self, file_name: str):        
        self._clear_log_data()
        try:
            with open(file_name, "r") as file:
                self.db.log_file_raw = file.readlines()

                self.db.log_file_to_display = list(self.db.log_file_raw)
        except:
            print (f"file not found: {file_name}")

        # Concat all lines to good format for view
        return self._concat_list_into_string(self.db.log_file_to_display)
    
    def export_log(self):
        file = asksaveasfile(mode = "w", filetypes=Model.__files_extensions, defaultextension=Model.__files_extensions)
        if file is not None:
            file.write(self._concat_list_into_string(self.db.log_file_to_display))
            file.close()
        return

    def filter_log(self, words:list):                        
        tmp_log_file=[]
        if (len(self.db.log_file_filtered_buffer) == 0):
            log_to_filter = list(self.db.log_file_raw)
        else:
            log_to_filter = list(self.db.log_file_filtered_buffer[-1])
            
        for line in log_to_filter:
            word_found_counter = 0
            for word in words:
                if word in line:
                    word_found_counter +=1
                
            if word_found_counter == len(words):
                tmp_log_file.append(line)
                pass
        
        # Store log into buffer and in list to display
        self.db.append_to_log_file_filtered_buffer(tmp_log_file)
        self.db.log_file_to_display=list(tmp_log_file)
        
        # Concat log to good format for display        
        return "".join(line for line in tmp_log_file)
    
    def get_previous_filtered_log(self):
        ret = None
        
        if (len(self.db.log_file_filtered_buffer)>1):          
            self.db.pop_from_log_file_filtered_buffer(-1)
            ret = self._concat_list_into_string(self.db.log_file_filtered_buffer[-1])
        elif (len(self.db.log_file_filtered_buffer)==1):
            if (len(self.db.log_file_raw)>0):
                ret = self._concat_list_into_string(self.db.log_file_raw)
        else:
            ret = None
            
        # print (ret)
        return ret
    
    def _clear_log_data(self):
        self._log_file_raw = list()
        self._log_file_filtered_buffer = list()
        self._log_file_to_display = list()


    def _concat_list_into_string(self, text_list:list()):
        return "".join(line for line in text_list)
        

    # # def export_file():
    # #     return

    # # def search(words):
    # #     return

    # # def get_log_to_display():        
    # #     return _log_file_to_display


    # def __clear_buffers(self):
    #     self._log_file_raw = list()
    #     self._log_file_filtered = list()
    #     self._log_file_to_display = ""