import os
import subprocess

import pytest

TEST_DATA_DIR = 'tests/data/'
TEST_INPUT_READCOUNT = TEST_DATA_DIR + 'test.readcount'

TEST_VAF_OUTPUT = TEST_DATA_DIR + 'test.output.vaf'
EXPECTED_VAF_OUTPUT = TEST_DATA_DIR + 'expected.vaf'


def test_basic_run():
    tool_args = ['python', 'quartzite/quartzite.py',
            '--output', TEST_VAF_OUTPUT,
            TEST_INPUT_READCOUNT]
    
    results = subprocess.check_output(tool_args).decode('utf-8')

    f1 = open(TEST_VAF_OUTPUT)
    f2 = open(EXPECTED_VAF_OUTPUT)

    assert f1.read() == f2.read()
