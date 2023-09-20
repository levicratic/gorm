# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    fun = 'times'

    def setName():
        pass # it's a function!

define q_name = "???"

define k = Character("???", color="#334499")
define q = Character("q_name", color="#ffffff", dynamic=True)

# special definition, assigns the narrator character
define narrator = Character(what_italic=True)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    play music "ceaseless-hunger.mp3" fadeout 1

    # These display lines of dialogue.

    q "You've created a new Ren'Py game."

    q "Once you add a story, pictures, and music, you can release it to the world!"

    k "Gosh, it's so exciting." (what_color="#996699")

    "You've got work to do."
    # This ends the game.

    return
