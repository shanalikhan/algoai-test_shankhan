import unittest
import pytest
import os
from command.CommandReader import CommandReader
from command.CommandProcessor import CommandProcessor

class TestCommand(unittest.TestCase):
    
    def file_check(self):
        assert os.path.exists('data.txt')

    def test_parse(self):
        reader = CommandReader('data.txt')
        parse_commands = reader.get_by_function_type('parse')
        assert parse_commands ==[{'function': 'parse', 'help': 'file help', 'value': 'file'}]

    def test_copy(self):
        reader = CommandReader('data.txt')
        copy_commands = reader.get_by_function_type('copy')
        assert copy_commands ==[{'function': 'copy', 'help': 'copy help', 'value': 'file'}]


    def test_functional(self):
        reader = CommandReader('data.txt')
        parse_commands = reader.get_by_function_type('parse')
        copy_commands = reader.get_by_function_type('copy')
        processed_parsed = CommandProcessor.process_command(parse_commands,'parse')
        processed_copy = CommandProcessor.process_command(copy_commands,'copy')
        processed_commands = processed_parsed.copy()
        processed_commands.extend(processed_copy)
        assert processed_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]

    def test_random(self):
        reader = CommandReader('data.txt')
        assert len(reader.get_random_samples(2))==2
