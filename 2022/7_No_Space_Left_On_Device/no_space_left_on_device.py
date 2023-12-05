import os


class cmd_to_json:

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
        for i, s in enumerate(str(self.file_structure).replace('\n', '')):
            if passing:
                passing = False
            elif s == ',':
                passing = True
                out += s + '\n' + (tabs * '    ')
            elif s == '{':
                tabs += 1
                out += s + '\n' + (tabs * '    ')
            elif s == '}':
                tabs -= 1
                out += '\n' + (tabs * '    ') + s
            else:
                out += s
        return (out + '\n').replace("'", '"')


class size_of_folder:

    def __init__(self, dictionary, capacity, program_size):
        self.capacity = capacity
        self.program_size = program_size

        self.sum_sub_100k = 0
        self.super_100k = capacity

        self.total = self.folder_size(dictionary)
        self.get_super_100k(dictionary)

    def folder_size(self, dictionary):
        size = 0
        if type(dictionary) == int:
            return dictionary
        for element in dictionary:
            size += self.folder_size(dictionary[element])
        if size <= 100_000:
            self.sum_sub_100k += size
        return size

    def get_super_100k(self, dictionary):
        size = 0
        if type(dictionary) == int:
            return dictionary
        for element in dictionary:
            size += self.get_super_100k(dictionary[element])
        if size <= 100_000:
            self.sum_sub_100k += size
        if size >= self.total + self.program_size - self.capacity and size < self.super_100k:
            self.super_100k = size
        return size


file = open('7_No_Space_Left_On_Device\\input.txt', 'r')
json_folder = cmd_to_json(file)
file.close()

folder_size = size_of_folder(json_folder.get_file_structure(), 70_000_000, 30_000_000)
print(f'{folder_size.total} : {folder_size.sum_sub_100k} : {folder_size.super_100k}')

log = open('7_No_Space_Left_On_Device\\root_directory.json', 'w')
log.write(json_folder.__str__())
log.close()
