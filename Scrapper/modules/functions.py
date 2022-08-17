import time

class funcions_class:  
    def wait_time(self, seconds):
        while seconds > 0: 
            time.sleep(1)
            seconds -= 1
        
    def clean_unnecessary_characters(self, string_to_replace):      
        string_to_replace = string_to_replace.replace("\"", "")
        string_to_replace = string_to_replace.replace("\t","")
        string_to_replace = string_to_replace.replace("\n","")       
        return string_to_replace
