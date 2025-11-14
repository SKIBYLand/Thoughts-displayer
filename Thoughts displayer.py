#Display through spcecified font or not (sys commmand-line) a message prompted.
import sys, random, pyfiglet
from pyfiglet import Figlet

#Get all the fonts available on pyfiglet.
fonts = pyfiglet.FigletFont.getFonts()


if len(sys.argv) == 1: #if the command-line only has one argument,
    font_name = random.choice(fonts) #choose a random font.
    user_text = (input('What do you want to display: ')) #prompt the user's text.
    print(font_name.renderText(user_text)) #display it

elif len(sys.argv) == 2: #if the command-line has two argument, code CAN'T be executed! (font missing)
    sys.exit('Invalid usage')

elif len(sys.argv) == 0: #if no command-line arguments, code CAN'T be executed!
    sys.exit('Invalid usage')

elif len(sys.argv) == 3: #in the command-line has three arguments,
    if sys.argv[1] in ['-f', '--font'] and sys.argv[2] in fonts: #check if the 2nd & 3rd element are respectively '-f/--font' & valid font.
        user_font = sys.argv[2]
        user_font = Figlet(font=user_font) #select the font in FigletFont list.
        user_text = (input('What do you want to display: ')) #prompt the user's text.
        print(user_font.renderText(user_text)) #display it.

    elif sys.argv[1] not in ['-f', '--font']: #2nd command-line argument not valid
        sys.exit('Invalid Usage')
    elif sys.argv[2] not in fonts: #3rd command-line argument not valid
        sys.exit('Inavlid usage')
