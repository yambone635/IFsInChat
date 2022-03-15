"""Tests the if_interface module.
"""

import pytest

import if_interface as ifi

@pytest.fixture
def interpreter():
    interpreter = ifi.Interpreter()
    yield interpreter
    interpreter.close()

def test_initialize_interpreter(interpreter):
    output = interpreter.get_output()
    assert len(output) > 0

def test_send_command(interpreter):
    interpreter.send_command("test")
    output = interpreter.get_output()
    assert len(output) > 0
