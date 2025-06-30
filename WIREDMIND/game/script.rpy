# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[mcname]", color="#FCC1DF")
define mcanon = Character("???", color="#FCC1DF")
define patient = Character("Patient")
define koa = Character("Koa")
define koaanon = Character("???", color="#A12323")
define cato = Character ("Cato")


# The game starts here.

label start:

    scene plaza with dissolve
    #cycle through bgs or have some sort of bg that shows the virus
    centered "The cold crawl of metal,"
    centered "The fusing of your mind with some..."
    centered "{i}Thing{/i}"
    scene hallway with dissolve
    centered "Your memories,"
    centered "They aren't the same."
    scene lab with dissolve
    centered "The virus invades your mind in a way that you can't even understand."
    centered "You can {i}feel{/i} the disconnect of flesh and metal."
    scene black with dissolve
    centered "It's like all of the threads that sew them together just..."
    centered "Snap."

    mcanon "I can't even imagine how it feels..."
    mcanon "To have your system separated from your brain."

    patient "..."
    patient "It's hell."
    patient "Just pure hell."
    #scene hospital with dissolve
    patient "All of my memories that I had sorted into neat and organized folders,"
    patient "They're all just so..."
    patient "So...jumbled up."
    patient "But I should be grateful. After all, some people had them erased completely."
    patient "I'm one of the lucky ones, yet I'm here complaining to you."
    patient "I can't believe myself..."

    mcanon "(This is always the hardest part. I wish there was something that I could do...)"
    mcanon "(The pain that these patients experience is something that I'll never be able to fully understand.)"
    mcanon "Please, don't think that way."
    mcanon "There might be people whose cases were more...extreme. But that doesn't discount your experience."
    mcanon "The feeling of being erased and the feeling of being mixed up...we need to hear about {i}both{/i} of them."
    mcanon "Neither one takes precedence over the other."
    mcanon "Your complaints aren't just complaints. Believe me, your story brings us one step closer to understanding the virus."
    mcanon "Every time you feel bad about it, remind yourself that you're helping us too."

    patient "..."
    patient "Thank you..."

    mcanon "I should be the one thanking you. It can't be easy to recount all of this."
    mcanon "I'll be back again in a few days to collect a few samples and ask some more questions, if you're still willing to proceed."

    patient "Of course."
    patient "..."
    patient "Miss..."

    mcanon "?"

    patient "I feel badly about not knowing your name."
    patient "If you're going to be here every week having to listen to my complaining, the least I could do is get to know you a bit in return."

    scene black
    centered "You can now input the name you want to use. Leaving it blank will allow you to use the default name."

    $ mcname = renpy.input("It's...", length = 12)
    $ mcname = mcname.strip()

    if not mcname:
            $ mcname = "Letha"

    mc "It's [mcname]."

    patient "Thank you, [mcname]."

    mc "I'll see you next week."

    scene plaza with dissolve
    mc "(These visits never get easier.)"
    mc "(Seeing our patients' faces as they try to recall their memories...)"
    mc "(It must be hard for them.)"
    mc "(I can't really understand what it must feel like.)"
    mc "(Someone's system splitting from their brain without being able to be reunited? How can that even be possible?)"
    mc "(The split isn't just a feeling. It's really happening, physically.)"
    mc "(And the virus attacking both the system and the brain is unusual.)"
    mc "(Most sicknesses are one or the other, but for it to be both is...)"
    mc "(Unprecedented.)"
    mc "(What's worse than that is, we can't seem to figure out how it's transmitted.)"
    mc "(There's no clear pattern between these cases at all.)"


    #motorbike sound effects
    scene plaza with vpunch
    scene plaza with hpunch
    scene plaza with vpunch
    scene plaza with hpunch
    scene plaza with vpunch
    scene plaza with hpunch

    koaanon "OUT OF THE WAY!"
    mc "?!"

    scene koa cg

    koaanon "Emergency control expedition!"
    koaanon "All citizens stay clear!"

    mc "(Ah, the patrol order.)"
    mc "(There must have been some sort of infiltration. It's rare to see them out in the main streets.)"
    mc "What could have happened..."

    scene plaza with dissolve
    "In the corner of the plaza between a coffee shop and an upgrade store, about 5 members in distinct harnessed uniforms huddled around someone."
    "It's clear that a small struggle ensued, but no one could really tell what had happened."

    mc "(I wonder what that was...)"
    mc "(I know that they're busy but...)"
    mc "(Isn't it my job as an intern to get as much information about the virus as I can?)"
    mc "(The patrol order rarely ever works on assignments that have to do with something other than the virus.)"
    mc "(Technically, they're my coworkers in a way...kind of.)"

    menu:
        mc "(I doubt it would be all that bothersome and I could get good information by just asking...)"

        "Ask about what happened":
            jump ask

        "Stay out of the way":
            jump quiet

label ask:
    scene plaza

    mc "(Nothing ventured, nothing gained.)"

    koaanon "Go away bruh."

    mc "Damn okay."

    jump main

label quiet:
    scene plaza

    mc "(I should stay out of their way...)"
    mc "(If it's meant to be public knowledge, I'll hear about it. If it's classified, I doubt they'd tell me anything even if I begged.)"

    jump main


label main:
    "blah blah blah i'll write this out tmrw"

    return
