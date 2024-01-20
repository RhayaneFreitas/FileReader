from tkinter import filedialog, Tk
import csv
import json
import xml.dom.minidom


class Txtfile():
    def __init__(self, file_name, content):
        self.file_name = file_name
        self.content = content

    def read_file(self):
        with open(self.file_name, "r", encoding="UTF-8") as file:
            content = file.read()
            file.close()
        self.content = content

    def print_file(self):
        print(self.content)    

class Jsonfile():
    def __init__(self, file_name, content):
        self.file_name = file_name
        self.content = content

    def read_file(self):
        with open(self.file_name, "r", encoding="UTF-8") as file:
            content = json.load(file)
        self.content = content        

    def print_file(self):
        print(self.content)

class Xmlfile():
    def __init__(self, file_name, content):
        self.file_name = file_name
        self.content = content

    def read_file(self):
        with open(self.file_name, "r") as file:
            content = file.read()
        self.content = content.replace("\n", "")

    def print_file(self):
        temp = xml.dom.minidom.parseString(self.content)
        new_xml = temp.toprettyxml()
        print(new_xml)

class Csvfile():
    def __init__(self, file_name, content):
        self.file_name = file_name
        self.content = content

    def read_file(self):
        with open(self.file_name, "r", encoding="utf-8-sig") as file:
            csvreader = csv.reader(file)
            header = []
            header = next(csvreader)
            rows = []
            for row in csvreader:
                rows.append(row)

            self.content = {"header": header,
                            "rows": rows}

    def print_file(self):
        print(self.content["header"])
        for row in self.content["rows"]:
            print(row)

Tk().withdraw()
file_name = filedialog.askopenfilename(
filetypes=(("Json Files", "*.json"),
            ("Text files", "*.txt"),
            ("XML Files", "*.xml"),
            ("CSV Files", "*.csv")))
file_extension = file_name.split(".")[-1]
    
if file_extension == "json":
    file = Jsonfile(file_name, None)

elif file_extension == "txt":
    file = Txtfile(file_name, None)

elif file_extension == "xml":
    file = Xmlfile(file_name, None)

elif file_extension == "csv":
    file = Csvfile(file_name, None)

file.read_file()
file.print_file()