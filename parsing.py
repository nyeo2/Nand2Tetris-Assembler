# Takes C-Command assembly code and returns comp/dest/jump using respectively named methods
import re

class Parser():
    def __init__(self, line):
        self.parsed = re.split('[=; ]+', line)
        self.line = line
        
    def comp(self):
        if '=' in self.line:
            return self.parsed[1]
        else:
            return self.parsed[0]
    
    def dest(self):
        if '=' in self.line:
            return self.parsed[0]
        else:
            return ''
    
    def jump(self):
        if ';' in self.line:
            if '=' in self.line:
                return self.parsed[2]
            else:
                return self.parsed[1]
        else:
            return ''
