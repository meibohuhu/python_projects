import pyfiglet
import termcolor

result = pyfiglet.figlet_format("Hi")
# print(result)


def print_color(msg, color):
    valid_colors = ("black", "red", "green", "yellow", "blue", "magenta", "cyan", "white")
    if color not in valid_colors:
        print("Not valid")
        return
    arcii_art = pyfiglet.figlet_format(msg)
    colored_art = termcolor.colored(arcii_art, color=color)
    print(colored_art)

# print(help(termcolor))
msg = input("What would you like to print?\n")
color = input("What color\n")
print_color(msg, color)