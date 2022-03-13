
import if_interface as ifi

interpreter = ifi.Interpreter()

interpreter.send_command("test")

interpreter.close()

print(interpreter.get_output())
