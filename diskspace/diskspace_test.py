import unittest
import diskspace
from diskspace import *
import os
import subprocess
import re
import sys
import StringIO

class testDiskSpace(unittest.TestCase):


    def test_subprocess_check_output(self):
        command = 'ls'
        check = subprocess.check_output(command)


    def test_bytes_to_readable(self):
        blocksB = 1
        blocksKb = 256
        blocksMb = 524288
        blocksGb = 1073741824

        self.assertEqual(diskspace.bytes_to_readable(blocksB), '512.00B')
        self.assertEqual(diskspace.bytes_to_readable(blocksKb), '128.00Kb')
        self.assertEqual(diskspace.bytes_to_readable(blocksMb), '256.00Mb')
        self.assertEqual(diskspace.bytes_to_readable(blocksGb), '512.00Gb')


    def test_print_tree(self):
        largest_size = 8
        total_size = 4
        cmd = 'du '
        path = os.path.abspath('.')
        cmd += path
        file_tree = {path: {'print_size': '50.00Kb', 'children': [], 'size': 3}}

        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput

        print_tree(file_tree, file_tree[path], path, largest_size, total_size)

        sys.stdout = sys.__stdout__
        self.assertEqual('50.00Kb   75%  '+ path, capturedOutput.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
