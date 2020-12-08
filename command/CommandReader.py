import json
import random

class CommandReader:
    def __init__(self,file_path):
        self.file_path = file_path
        with open(self.file_path, 'r') as file:
            self.data = json.loads(file.read())

    def get_by_function_type(self,function_type):
        selected_commands= list()
        for row in self.data:
            if 'function' in row and row['function'] == function_type:
                selected_commands.append(row)
        return selected_commands        
        
    def get_random_samples(self,length):
        random_commands = random.sample(self.data, length)
        return random_commands