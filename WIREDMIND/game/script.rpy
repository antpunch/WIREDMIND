# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[mcname]")
define anon = Character("???")
define patient = Character("Patient")
define f = Character("Koa")
define s = Character ("Cato")


# The game starts here.

label start:

    scene black with dissolve
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

    #scene hospital with dissolve
    anon "I can't even imagine how it feels..."
    anon "To have your system separated from your brain."
    patient "..."
    patient "It's hell."
    patient "Just pure hell."
    patient "All my memories that I had sorted into neat and organized folders,"
    patient "They're all just so..."
    patient "So...jumbled up"
    patient "But I should be grateful. After all, some people had them erased completely."
    patient "I'm one of the lucky ones, yet I'm here complaining to you."
    patient "I can't believe myself..."
    anon "(This is always the hardest part. I wish there was something that I could do...)"
    anon "(The pain that these patients experience is something that I'll never be able to fully understand.)"
    anon "Please, don't think that way."
    anon "There might be people whose cases were more...extreme. But that doesn't discount your experience."
    anon "The feeling of being erased and the feeling of being mixed up...we need to hear about {i}both{/i} of them."
    anon "Your complaints aren't just complaints. Believe me, your complaints bring us one step closer to understanding the virus."
    anon "Every time you feel bad about it, remind yourself that you're helping."
    patient "..."
    patient "Thank you..."
    anon "I should be the one thanking you. It can't be easy to recount all of this."
    anon "I'll be back again in a few days to collect a few samples and ask some more questions, if you're still willing to proceed."
    patient "Of course."
    patient "..."
    patient "Miss..."
    anon "?"
    patient "I feel badly about not knowing your name."
    patient "If you're going to be here every week having to listen to my complaining, the least I could do is know your name."

    scene black
    centered "You can now input the name you want to use. Leaving it blank will allow you to use the default name."

    $ mcname = renpy.input("It's...", length = 12)
    $ mcname = mcname.strip()

    if not mcname:
            $ mcname = "Letha"

    mc "It's [mcname]."
    patient "Thank you, [mcname]."
    mc "I'll see you next week."

    #scene plaza with dissolve

    return
