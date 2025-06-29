# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[mcname]")
define anon = Character("???")
define patient = Character("Patient")
define f = Character("Koa")
define s = Character ("NAME")


# The game starts here.

label start:

    scene black
    #cycle through bgs or have some sort of bg that shows the virus
    centered "The cold crawl of metal,"
    centered "The fusing of your mind with some..."
    centered "{i}Thing{/i}"
    centered "Your memories,"
    centered "They aren't the same."
    centered "The virus invades your mind in a way that you can't even understand."
    centered "You can {i}feel{/i} the disconnect of flesh and metal."
    centered "It's like all of the threads that sew them together just..."
    centered "Snap."

    #hospital bg
    anon "I can't even imagine how it feels..."
    anon "To have your system separated from your brain."

    scene black
    centered "You can now input the name you want to use. Leaving it blank will allow you to use the default name."

    $ mcname = renpy.input("It's...", length = 12)
    $ mcname = mcname.strip()

    if not mcname:
            $ mcname = "Letha"



    mc "Test text."

    mc "yayayay ma-aow"

    # This ends the game.

    return
