import os
import time


####### COMMAND TO DICTIONARY #######

class file_dictionary:

    def __init__(self, file):
        self.f = file
        self.file_structure = {}
        self.current_path = []
        for s in self.f:
            if s[0] == '$':
                self.command(self.current_path, s[:-1])
            else:
                self.parse(s[:-1])

    def command(self, current_path, s):
        if s[2:4] == 'cd':
            if s[5:7] == '..':
                current_path.pop()
            else:
                self.current_folder()[s[5:]] = {}
                current_path += [str(s[5:])]

    def current_folder(self):
        folder = self.file_structure
        for part in self.current_path:
            folder = folder[part]
        return folder

    def parse(self, s):
        if s[0:3] == 'dir':
            self.current_folder()[s[4:]] = {}
        else:
            self.current_folder()[s[s.index(' ')+1:]] = int(s[:s.index(' ')])

    def get_file_structure(self):
        return self.file_structure

    def __str__(self):
        tabs, passing, out = 0, False, ''
        for i, s in enumerate(str(self.file_structure)):
            if passing:
                passing = False
            elif s == '\n':
                pass
            elif s == ',':
                passing = True
                out += s + '\n' + (tabs * '   ')
            elif s == '{':
                tabs += 1
                out += s + '\n' + (tabs * '   ')
            elif s == '}':
                tabs -= 1
                out += '\n' + (tabs * '   ') + s
            else:
                out += s
        return out + '\n'


####### FOLDER SIZE #######

def folder_size(directionary, sub):
    size = 0
    if type(directionary) == int:
        return directionary
    for element in directionary:
        size += folder_size(directionary[element], sub)
    if size <= 100000:
        sub += size
    return size



####### MAIN LOGIC #######

file = open('7_No_Space_Left_On_Device\\input.txt', 'r')
log = open('7_No_Space_Left_On_Device\\log.txt', 'w')

directory = file_dictionary(file)
directionary = directory.get_file_structure()
log.write(directory.__str__())

sub = 0
print(folder_size(directionary, sub))


file.close()
