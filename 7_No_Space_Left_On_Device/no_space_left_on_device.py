import os

####### COMMAND TO DICTIONARY #######

class file_dictionary:

    def __init__(self, file):
        self.f = file
        self.file_structure = {}
        self.current_path = []
        self.get_file_dictionary()

    def get_file_dictionary(self):
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
                self.file_structure[s[5:]] = {}
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

        
        pass

####### FOLDER SIZE MATH #######


####### MAIN LOGIC #######




file = open('7_No_Space_Left_On_Device\\input.txt', 'r')

print(file_dictionary(file).get_file_structure())




file.close()
