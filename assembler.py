import parsing, translator, binConverter, symbolTable, sys

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
# Takes a line of C-Command assembly code and returns it in machine code
def translateC(line):
    parsedLine = parsing.Parser(line)
    translatedComp = translator.Translator(parsedLine.comp()).comp()
    translatedDest = translator.Translator(parsedLine.dest()).dest()
    translatedJump = translator.Translator(parsedLine.jump()).jump()
    
    return '111' + translatedComp + translatedDest + translatedJump

def translateA(line, table):
    if RepresentsInt(line[1:]):
        return '0' + binConverter.dectobin(line[1:]).zfill(15)
    elif table.contains(line[1:]):
        return '0' + binConverter.dectobin(str(table.getAddress(line[1:]))).zfill(15)
    else:
        table.addEntry(line[1:], table.currentRAM)
        table.incrementRAM()
        return '0' + binConverter.dectobin(str(table.getAddress(line[1:]))).zfill(15)

# Takes list of .asm commands and returns table obj with program labels
def passOne(assemLines):
    table = symbolTable.symbolTable()
    currentPtr = 0
    for line in assemLines:
        if not line or line[:2] == '//':
            continue
        elif '(' in line:
            table.addEntry(line[1:-1], currentPtr)
        else:
            currentPtr += 1
    return table

#opens and converts .asm file to list of lines
fileName = sys.argv[1]
assemLines = [line.partition('//')[0].strip() for line in open(fileName)]

#initialise table using passOne
table = passOne(assemLines)


outFile = open(fileName[:-4] + '.hack', 'w')

for line in assemLines:
    if not line or line[:2] == '//' or line[0] == '(':
        continue
    if '@' in line:
        outLine = translateA(line, table)
    else:
        outLine = translateC(line)
    outFile.write(outLine + '\n')
    
outFile.close()

