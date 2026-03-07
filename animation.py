import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

class Loader:
    def __init__(self, speed=0.1, color=Fore.WHITE):
        self.speed = speed
        self.color = color

    def _clear_line(self, length):
        sys.stdout.write("\r" + " " * length + "\r")
        sys.stdout.flush()

    # 1️⃣ spinner
    def spinner(self, text="Loading", output="Done", duration=5):
        spinner = ["\\", "|", "/", "-"]
        end_time = time.time() + duration
        last_len = 0

        while time.time() < end_time:
            for frame in spinner:
                current = f"{text} {frame}"
                last_len = len(current)
                sys.stdout.write(f"\r{self.color}{current}{Style.RESET_ALL}")
                sys.stdout.flush()
                time.sleep(self.speed)

        self._clear_line(last_len)
        print(f"{self.color}{text} {output}{Style.RESET_ALL}")

    # 2️⃣ dots (FIXED TOTAL)
    def dots(self, text="Loading", output="Done", duration=5):
        end_time = time.time() + duration

        while time.time() < end_time:
            for dots in range(0, 4):
                message = f"{text}{'.' * dots}     "
                last_len = len(message)

                sys.stdout.write(f"\r{self.color}{message}{Style.RESET_ALL}")
                sys.stdout.flush()
                time.sleep(0.3)

        self._clear_line(last_len)
        print(f"{self.color}{text} {output}{Style.RESET_ALL}")

    # 3️⃣ progress
    def progress(self, text="Loading", output="Done", total=100):
        last_len = 0

        for i in range(total + 1):
            percent = int((i / total) * 100)
            bar = "█" * (percent // 5)
            spaces = " " * (20 - len(bar))
            current = f"{text} |{bar}{spaces}| {percent}%"
            last_len = len(current)

            sys.stdout.write(f"\r{self.color}{current}{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(self.speed)

        self._clear_line(last_len)
        print(f"{self.color}{text} {output}{Style.RESET_ALL}")