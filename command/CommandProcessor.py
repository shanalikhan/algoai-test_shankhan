class CommandProcessor:
    def __init__(self) -> None:
        super().__init__()
    
    @staticmethod
    def process_command(commands, command_type):
        processed_commands = list()
        for idx,command in enumerate(commands):
            command['_list'] = command_type
            command['_counter'] = idx +1
            processed_commands.append(command)
        return processed_commands