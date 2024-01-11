from tkinter import filedialog, Tk


class readFile():
    def __init__(self, _filename=str, _fileExtension=str, _lines=list):
        self.filename = _filename
        self.fileExtension = _fileExtension
        self.lines = _lines

    # Function used to choose which file you want to open:
    def setFilename(self):
        Tk().withdraw()
        filename = filedialog.askopenfilename(
        filetypes=(("Json Files", "*.json"),
                   ("Text files", "*.txt"),
                   ("XML Files", "*.xml"),
                   ("CSV Files", "*.csv")))
        self.filename = filename

    def setExtension(self):
        self.fileExtension = self.filename.split(".")[-1]

    # Function used for reading the file:
    def readFile(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        self.lines = lines

    # Function used for processing files: json, txt, xml and csv.
    def processFile(self):
        if self.fileExtension == "json" or self.fileExtension == "txt" or self.fileExtension == "xml":
            for i in range(len(self.lines)):
                line = self.lines[i]
                newLine = line.replace("\n", "")
                self.lines[i] = newLine

        elif self.fileExtension == "csv":
            splittedLines = list()
            for i in range(len(self.lines)):
                line = self.lines[i]
                newLine = line.replace("ï»¿", "").replace("\n", "")
                splittedNewLine = newLine.split(";") # Retrieve the elements between the semicolons and store them in a list.
                splittedLines.append(splittedNewLine)

            # Transpose a list of lists:
            transposedSplittedLines = list()
            for i in range(len(splittedLines[0])):
                row = list()
                for sublist in splittedLines:
                    row.append(sublist[i])
                transposedSplittedLines.append(row)

            # Identify the one with the highest number of characters and place it in a list named maxNumberCharactersPerColumn
            maxNumberCharactersPerColumn = [0] * len(transposedSplittedLines)
            for i in range(len(transposedSplittedLines)):
                for j in range(len(transposedSplittedLines[i])):
                    numberCharacters = len(transposedSplittedLines[i][j])
                    if maxNumberCharactersPerColumn[i] < numberCharacters:
                        maxNumberCharactersPerColumn[i] = numberCharacters
            
            # Analyze each element in the column and check if it contains maxNumberCharactersPerColumn. If not, add spaces to align all the elements.
            for i in range(len(splittedLines)):
                line = " | "
                for j in range(len(splittedLines[i])):
                    item = splittedLines[i][j]
                    if len(item) < maxNumberCharactersPerColumn[j]:
                        spacesLeft = maxNumberCharactersPerColumn[j] - len(item)
                        item = item + " "*spacesLeft
                    splittedLines[i][j] = item + " | "
                    line = line + splittedLines[i][j]
                self.lines[i] = line

    # Function used to display the contents of the file
    def printFile(self):
        for i in range(len(self.lines)):
            line = self.lines[i]
            print(line)

content = readFile()
content.setFilename()
content.setExtension()
content.readFile()
content.processFile()
content.printFile()