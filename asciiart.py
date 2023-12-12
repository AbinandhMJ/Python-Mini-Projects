from pyfiglet import Figlet

def generate_ascii_art(text, font='standard'):
    fig = Figlet(font=font)
    return fig.renderText(text)

if __name__ == "__main__":
    input_text = input("Enter text to convert to ASCII art: ")
    font_choice = input("Enter font (press Enter for standard): ")

    if not font_choice:
        font_choice = 'standard'

    ascii_art = generate_ascii_art(input_text, font_choice)
    print(ascii_art)
