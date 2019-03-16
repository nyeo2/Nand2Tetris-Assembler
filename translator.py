# Takes C-Command assembly code and returns machine code based on 
# comp/dest/jump methods

class Translator():
    def __init__(self, code):
        self.code = code
        
        self.aTable = {'0' : '101010',
                       '1' : '111111',
                       '-1' : '111010',
                       'D' : '001100',
                       'A' : '110000',
                       '!D' : '001101',
                       '!A' : '110001',
                       '-D' : '001111',
                       '-A' : '110011',
                       'D+1' : '011111',
                       'A+1' : '110111',
                       'D-1' : '001110',
                       'A-1' : '110010',
                       'D+A' : '000010',
                       'D-A' : '010011',
                       'A-D' : '000111',
                       'D&A' : '000000',
                       'D|A' : '010101'}

        self.mTable = {'M' : '110000',
                       '!M' : '110001',
                       '-M' : '110011',
                       'M+1' : '110111',
                       'M-1' : '110010',
                       'D+M' : '000010',
                       'D-M' : '010011',
                       'M-D' : '000111',
                       'D&M' : '000000',
                       'D|M' : '010101'}
    
    def comp(self):
        compBits = ''
        if 'M' in self.code:
            compBits += '1'
            table = self.mTable
        else:
            compBits += '0'
            table = self.aTable
        
        return compBits + table[self.code]
        
        
    def dest(self):
        destBits = ['0'] * 3
        
        if 'A' in self.code:
            destBits[0] = '1'
        if 'D' in self.code:
            destBits[1] = '1'
        if 'M' in self.code:
            destBits[2] = '1'
        
        return ''.join(destBits)
            
    def jump(self):
        jumpBits = ['0'] * 3
        
        if 'G' in self.code:
            jumpBits[2] = '1'
        if 'L' in self.code:
            jumpBits[0] = '1'
        if 'E' in self.code:
            jumpBits[1] = '1'
        
        if 'N' in self.code:
            jumpBits = ['1', '0', '1']
        if 'M' in self.code:
            jumpBits = ['1'] * 3
        
        return ''.join(jumpBits)
