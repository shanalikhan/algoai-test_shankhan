from command.CommandReader import CommandReader
from command.CommandProcessor import CommandProcessor

reader = CommandReader('data.txt')
parse_commands = reader.get_by_function_type('parse')
copy_commands = reader.get_by_function_type('copy')

processed_parsed = CommandProcessor.process_command(parse_commands,'parse')
processed_copy = CommandProcessor.process_command(copy_commands,'copy')

processed_commands = processed_parsed.copy()
processed_commands.extend(processed_copy)

print(f"parse_commands: {parse_commands}")
print(f"copy_commands: {copy_commands}")


print(f"functional_commands: {processed_commands}")


print(f"random_commands: {reader.get_random_samples(2)}")