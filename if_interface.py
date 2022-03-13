"""Provides a python interface for an IF fiction interpreter.
"""

from threading import Thread

import subprocess
import time

# This should be the filename for the interpreter program. Assumed to be
# in the top level of the project directory.
_INTERPRETER_FILENAME = "dummy_interpreter.exe"
_CLOSE_COMMAND = "exit\n"

class Interpreter:
    """Handles all interactions with the IF interpreter.
    """

    def __init__(self, processing_time = 0.1):
        self._processing_time = processing_time

        interpreter_path = "./" + _INTERPRETER_FILENAME

        self._interpreter = subprocess.Popen(
            [interpreter_path, "test", "-abc", "--arguments"],
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            encoding = 'utf8'
        )
        time.sleep(self._processing_time)

        self._interpreter_output_buffer = []
        _nonblocking_output_buffer(
            self._interpreter.stdout,
            self._interpreter_output_buffer
        )

        self._interpreter_error_buffer = []
        _nonblocking_output_buffer(
            self._interpreter.stderr,
            self._interpreter_error_buffer
        )

    def send_command(self, input):
        """Sends a command to the interpreter.

        Args:
            input (string): The command to send to the interpreter.
        """

        self._interpreter.stdin.write(input + "\n")
        self._interpreter.stdin.flush()
        time.sleep(self._processing_time)
    
    def get_output(self):
        """Gets any output that hasn't been retrieved yet.

        Returns:
            string: The full contents of the output buffer.
        """

        output = ""
        while True:
            if self._interpreter_output_buffer:
                nextLine = self._interpreter_output_buffer.pop(0)
                output += nextLine.strip() + '\n'
            else:
                break
        return output

    def close(self):
        """Closes the interpreter.
        """

        self.send_command(_CLOSE_COMMAND)
        time.sleep(self._processing_time)

        # Just in case the interpreter is still alive
        self._interpreter.terminate()

def _nonblocking_output_buffer(input_stream, buffer):
    """Allows for reading from a stream without hanging when there's
    nothing to read.

    Args:
        input_stream (stream): A stream to read from.
        buffer (list): A list to put the stream's output into.
    """

    def _read_stream(stream, buffer):
        while not stream.closed:
            stream.flush()
            line = stream.readline()
            if line:
                buffer.append(line)
            else:
                break

    reading_thread = Thread(target = _read_stream,
                            args = (input_stream, buffer)
    )
    # reading_thread.daemon = True
    reading_thread.start()
    return reading_thread
