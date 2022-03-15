"""Provides a python interface for an IF fiction interpreter.
"""

from threading import Thread

import subprocess
import time

# This should be the filename for the interpreter program. Assumed to be
# in the top level of the project directory.
_INTERPRETER_FILENAME = "dfrotz.exe"

done_flag = False

class Interpreter:
    """Handles all interactions with the IF interpreter.
    """

    def __init__(self, game_filename, processing_time = 0.1):
        self._processing_time = processing_time

        interpreter_path = "./" + _INTERPRETER_FILENAME
        game_path = "./games/" + game_filename

        self._interpreter = subprocess.Popen(
            [interpreter_path, game_path],
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            text = True,
            encoding = 'utf-8',
            errors="ignore"
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
        if (self._interpreter.poll() is None
                and not self._interpreter.stdin.closed):
            self._interpreter.stdin.write(input + "\n")
            self._interpreter.stdin.flush()
            time.sleep(self._processing_time)
    
    def get_output(self):
        """Gets any output that hasn't been retrieved yet.

        Returns:
            string: The full contents of the output buffer.
        """

        if not self._interpreter_output_buffer:
            return "No game is currently running."

        output = ""
        while self._interpreter_output_buffer:
            nextChar = self._interpreter_output_buffer.pop(0)
            output += nextChar
        
        return output

    def close(self):
        """Closes the interpreter.
        """
        
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
            newoutput = stream.read(1)
            if newoutput:
                buffer.append(newoutput)
            else:
                buffer.append("Game closed.\n")
                break

    reading_thread = Thread(target = _read_stream,
                            args = (input_stream, buffer)
    )
    reading_thread.daemon = True
    reading_thread.start()
    return reading_thread
