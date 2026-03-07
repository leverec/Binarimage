from colorama import init, Fore, Style
from animation import Loader
from PIL import Image
import time
import sys
import random
import uuid
import os

init(autoreset=True)

# === SETTING ===
WIDTH = 128
HEIGHT = 128

color_0 = (255, 255, 255)
color_1 = (0, 0, 0)

# checks
def is_valid_rgb(color_0, color_1) -> bool:
    for color in (color_0, color_1):
        for value in color:
            if value < 0 or value > 255:
                return False
    return True

# custom color
def custom_color():
    print("Enter RGB for binary 0:")
    r0: int = int(input(Fore.RED + "R: "))
    g0: int = int(input(Fore.GREEN + "G: "))
    b0: int = int(input(Fore.BLUE + "B: "))
    color_0 = (r0, g0, b0)
    
    print(Style.RESET_ALL + "Enter RGB for binary 1:")
    r1: int = int(input(Fore.RED + "R: "))
    g1: int = int(input(Fore.GREEN + "G: "))
    b1: int = int(input(Fore.BLUE + "B: "))
    color_1 = (r1, g1, b1)
    
    if not is_valid_rgb(color_0, color_1):
        return None, None
    
    return color_0, color_1

# binary convertion
def convert_binary(Din: str) -> str:
    Dout = ' '.join(format(ord(D), '08b') for D in Din)
    return Dout

def binary_to_image(binary, width, height, color0, color1):
    img = Image.new("RGB", (width, height))
    pixels = img.load()

    binary = binary.replace(" ", "")
    index = 0

    for y in range(height):
        for x in range(width):
            if index < len(binary):
                bit = binary[index]
                index += 1
            else:
                bit = random.choice(["0", "1"])  # random filler

            pixels[x, y] = color1 if bit == "1" else color0

    return img

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def random_text(lines=32, width=53, duration=1):
    chars = "01"
    
    end_time = time.time() + duration
    while time.time() < end_time:
        clear()
        for _ in range(lines):
            line = "".join(random.choice(chars) for _ in range(width))
            print(Fore.GREEN + line)
        time.sleep(0.05)

if __name__ == "__main__":
    clear()
    random_text()
    loader = Loader(0.05, Fore.GREEN)
    loader.dots("initialize script", "successfully", 3)
    user = input(Fore.GREEN + "\nUse custom colors? [Y/n] ").strip().lower()
    if user == "y":
        loader.spinner("loading custom colors modules", "done", 2)
        color_0, color_1 = custom_color()
        if color_0 is None or color_1 is None:
            print("[!] an error has occured")
    text = input(Fore.GREEN + "Enter the text : ")
    binary = convert_binary(text)
    max_bits = WIDTH * HEIGHT
    binary_length = len(binary.replace(" ", ""))

    if binary_length > max_bits:
        print(Fore.RED + "[!] text too long for this image size")
        print(Fore.YELLOW + f"max bits : {max_bits}")
        print(Fore.YELLOW + f"your bits: {binary_length}")
        sys.exit()

    loader.spinner("generating image", "done", 2)

    img = binary_to_image(binary, WIDTH, HEIGHT, color_0, color_1)

    # create output folder
    os.makedirs("output", exist_ok=True)

    # random filename
    filename = f"{uuid.uuid4().hex}.png"
    filepath = os.path.join("output", filename)

    loader.spinner("saving image", "done", 1)

    img.save(filepath)

    print(Fore.GREEN + "\n[+] image generated successfully")
    print(Fore.CYAN + f"[+] saved as: {filepath}")