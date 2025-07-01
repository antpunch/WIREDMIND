# The script of the game goes in this file.

# characters
define mc = Character("[mcname]", color="#EC9594")
define mcanon = Character("???", color="#EC9594")
define koa = Character("Koa", color="#A12323")
define koaanon = Character("???", color="#A12323")
define cato = Character("Cato", color="#3F8C19")
define catoanon = Character("???", color="#3F8C19")
define patient = Character("Patient", color="#051a55")
define soldier = Character("Agent", color="#051a55")

# choice stuff
default ask = False

#darken bg to make centered text readable
image dark = "#00000088"
define portrait = Position(xpos=1620)


# The game starts here.

label start:

    scene hospital with dissolve
    show dark with dissolve
    #cycle through bgs or have some sort of bg that shows the virus
    centered "The cold crawl of metal,"
    centered "The fusing of your mind with some..."
    centered "{i}Thing{/i}"
    centered "Your memories,"
    centered "They aren't the same."
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

    scene hospital with dissolve
    patient "All of my memories that I had sorted into neat and organized folders,"
    patient "They're all just so..."
    patient "So...jumbled up."
    patient "But I should be grateful. After all, some people had them erased completely."
    patient "I'm one of the lucky ones, yet I'm here complaining to you."
    patient "I can't believe myself..."

    show mc sad at portrait
    mcanon "(This is always the hardest part. I wish there was something that I could do...)"
    mcanon "(The pain that these patients experience is something that I'll never be able to fully understand.)"
    mcanon "Please, don't think that way."
    mcanon "There might be people whose cases were more...extreme. But that doesn't discount your experience."
    show mc concentrated at portrait
    mcanon "The feeling of being erased and the feeling of being mixed up...we need to hear about {i}both{/i} of them."
    mcanon "Neither one takes precedence over the other."
    show mc talking at portrait
    mcanon "Your complaints aren't just complaints. Believe me, your story brings us one step closer to understanding the virus."
    mcanon "Every time you feel bad about it, remind yourself that you're helping us too."

    patient "..."
    patient "Thank you..."

    show mc neutral at portrait
    mcanon "I should be the one thanking you. It can't be easy to recount all of this."
    mcanon "I'll be back again in a few days to collect a few samples and ask some more questions, if you're still willing to proceed."

    patient "Of course."
    patient "..."
    patient "Miss..."

    show mc surprise at portrait
    mcanon "?"

    patient "I feel badly about not knowing your name."
    patient "If you're going to be here every week having to listen to my complaining, the least I could do is get to know you a bit in return."

    scene black
    centered "You can now input the name you want to use. Leaving it blank will allow you to use the default name."

    $ mcname = renpy.input("It's...", length = 12)
    $ mcname = mcname.strip()

    if not mcname:
            $ mcname = "Letha"

    scene hospital with dissolve
    show mc happy at portrait
    mc "It's [mcname]."

    patient "Thank you, [mcname]."

    show mc neutral at portrait
    mc "I'll see you next week."

    scene plaza with dissolve
    show mc sad at portrait
    mc "(These visits never get easier.)"
    mc "(Seeing our patients' faces as they try to recall their memories...)"
    mc "(It must be hard for them.)"
    mc "(I can't really understand what it must feel like.)"
    show mc concentrated at portrait
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

    show mc surprise at portrait
    koaanon "OUT OF THE WAY!"
    mc "?!"

    scene koa cg with dissolve
    $ renpy.pause(1.5)

    koaanon "Emergency control expedition!"
    koaanon "All citizens stay clear!"

    show mc neutral at portrait
    mc "(Ah, the patrol order.)"
    mc "(There must have been some sort of infiltration. It's rare to see them out in the main streets.)"
    show mc concentrated at portrait
    mc "What could have happened..."

    scene plaza with dissolve
    show mc surprise at portrait
    "In the corner of the plaza between a coffee shop and an upgrade store, about 5 members in distinct harnessed uniforms huddled around someone."
    "It's clear that a small struggle ensued, but no one could really tell what had happened."

    show mc concentrated at portrait
    mc "(I wonder what that was...)"
    mc "(I know that they're busy but...)"
    show mc happy at portrait
    mc "(Isn't it my job as an intern to get as much information about the virus as I can?)"
    mc "(The patrol order rarely ever works on assignments that have to do with something other than the virus.)"
    show mc sweat at portrait
    mc "(Technically, they're my coworkers in a way...kind of.)"

    menu:
        mc "(I doubt it would be all that bothersome and I could get good information by just asking...)"

        "Ask about what happened":
            $ ask = True
            jump ask

        "Stay out of the way":
            jump quiet

label ask:
    scene plaza with dissolve

    show mc concentrated at portrait
    mc "(Nothing ventured, nothing gained.)"

    #walking sound effect

    show mc talking at portrait
    mc "Um, excuse me."

    show koa halfbody neutral with dissolve
    koaanon "?"

    mc "I'm awfully sorry to intrude, but I was curious as to what this expedition was about."

    show koa halfbody talking
    koaanon "With all due respect, ma'am, this expedition is none of your business."

    show mc neutral at portrait
    mc "I don't know if this will change anything, but here's my badge. I'm an intern at the research center and-"

    show koa halfbody neutral
    koaanon "If you work at the research center, they'll tell you what you need to know and won't tell you what you don't need to know."

    show mc sad at portrait
    mc "..."

    show koa halfbody surprise
    koaanon "..."
    show koa halfbody talking
    koaanon "Look, this expedition is highly classified and there's nothing that I can tell any citizen directly."
    koaanon "But if you were to ask me...off the record, I'd say that something weird is going on with the virus..."
    show mc concentrated at portrait
    koaanon "It's just a feeling though. No need to take it seriously."

    play sound "scribble.wav"

    mc "No...need to take...it..."

    show koa halfbody surprise
    koaanon "H-hey! No, seriously! Why are you writing that down..."

    show mc surprise at portrait
    mc "Ah, sorry. This isn't for a report or anything, I swear! They're just my personal notes."
    show mc talking at portrait
    show koa halfbody surprise
    mc "I've felt that something might be off about the virus for a while too. Knowing that others feel the same way helps me feel like I'm not just overthinking it."

    show koa halfbody smirk
    koaanon "Hm."
    koaanon "What else do you have in there?"

    show mc angry at portrait
    mc "Hey, no peeking!"
    mc "(Aside from my interview notes with our patients, my journal holds a lot of my personal thoughts on the virus as well.)"
    mc "(Definitely not something I'd want just anyone to see. Certainly not something I would want to show to a government employee.)"
    mc "(You never know who might report what to higher ups.)"

    koaanon "What, got plans to overthrow the patrol order in there?"

    mc "I just have my reasons, alright. My research is important to me."

    show koa halfbody neutral
    koaanon "Hmm...fine, I won't push."
    koaanon "If you keep your notes that confidential, I'm sure that my off the record comment will be the same, right?"

    show mc talking at portrait   
    mc "Of course. Like I said, just personal notes."

    koaanon "If you have any thoughts on the virus, I-"

    soldier "KOA! Get over here and help me pack up this gear."

    show koa halfbody talking
    koaanon "I'll be right over!"
    show koa halfbody smirk
    koaanon "If you have any thoughts on the virus, I'd be curious to know about them. Off the record."
    hide koa halfbody smirk
    show mc neutral at portrait
    mc "..."
    show mc talking at portrait
    mc "(Ah, a crowd's starting to gather around.)"
    mc "(I guess it makes sense that everyone else would be curious too.)"
    show mc sweat at portrait
    mc "(Shoot, I only have 15 minutes to get back to the research center!)"

    scene black with dissolve
    $ renpy.pause(2.0)
    #SUBWAY NOISES

    jump main

label quiet:
    scene plaza with dissolve

    show mc neutral at portrait
    mc "(I should stay out of their way...)"
    mc "(If it's meant to be public knowledge, I'll hear about it. If it's classified, I doubt they'd tell me anything even if I begged.)"
    mc "(I should get back to the research center and update the patient file.)"
    scene black with dissolve
    $ renpy.pause(2.0)
    #SUBWAY NOISES

    jump main


label main:
    scene hallway with dissolve
    show mc sweat at portrait
    mc "*huff* *huff*"
    mc "Just...barely...made it..."
    show mc talking at portrait
    mc "(I can't help but think about that expedition.)"
    show mc concentrated at portrait
    mc "(It's so unusual for an expedition to be public like that.)"
    mc "(Cutting through the plaza instead of taking the smaller streets? I've never seen that happen before.)"
    mc "(Whatever the problem was, it was handled quickly. But for it to have been handled {i}that{/i} quickly means that it was serious.)"
    #paper rustling sound
    $ renpy.pause (0.5)
    #scribbling sound
    $ renpy.pause (0.5)
    mc "(Emergency control expedition...)"
    mc "(There weren't any newly announced cases.)"
    mc "(Which means...)"
    show mc surprise at portrait
    mc "An information leak!"
    #scribbling sound
    $ renpy.pause (0.5)
    show mc concentrated at portrait
    mc "(The situation surrounding this virus just keep getting more confusing.)"

    if ask:
        scene hallway with dissolve
        show mc neutral at portrait
        mc "(And it seems like that patrol order agent agrees.)"
        show mc concentrated at portrait
        mc "(Koa, huh...)"
        #scribbling sound
        $ renpy.pause (0.5)
        mc "(I wonder if working with him would help me clear up some of the questions I have.)"
        show mc sad at portrait
        mc "(Though it's unlikely that I'll ever even get the chance to have a talk with him again.)"
    
    show mc angry at portrait
    mc "(Why can't anyone get to the bottom of this virus?)"
    mc "Whatever, I'll think about this later."

    catoanon "[mcname]..."

    show mc blush at portrait
    mc "!"
    #door slide open sound
    
    scene cato cg with dissolve
    $ renpy.pause(1.5)

    show mc blush at portrait
    cato "You're late. About 45 seconds."

    show mc sweat at portrait
    mc "Cato, I'm so sorry! There was a sudden control expedition and I couldn't stop thinking about it when I got back to the center."

    show mc neutral at portrait
    cato "I know."

    mc "About the control expedition? Or about me standing outside in the hallway?"

    show mc sweat at portrait
    cato "Both."
    show mc neutral at portrait
    cato "And you're right about the control expedition. There was an information leak that they needed to handle as soon as possible."

    show mc sweat at portrait
    mc "Ah...so you heard me out there too..."

    cato "I always do. I was just curious as to how long it would take you to break out of your thoughts on your own."
    cato "Hand me that pipette by the freezer."

    scene lab with dissolve

    show mc neutral at portrait
    mc "(He's always does things with such precision even when he's multitasking...)"
    mc "(Cato's the researcher that I've been working under for the past few months. His dedication to understanding the virus never fails to amaze me.)"
    show mc sweat at portrait
    mc "(He's never angry with me when I'm late, but he times me whenever I am.)"
    $ renpy.pause (0.5)

    show cato halfbody neutral

    show mc talking at portrait
    mc "Here you go."

    scene cato cg with dissolve
    #glass clink sound effect

    show mc neutral at portrait
    cato "So, how did the patient interview go?"

    show mc sad at portrait
    mc "Difficult...as always."

    scene lab with dissolve
    show cato halfbody happy

    show mc sad at portrait
    cato "That's why I send you guys to do them."

    mc "It's not that I don't like talking to them. It's just...hard to look them in the eyes when they have to recall everything."

    cato "I'm sure that you put them at much greater ease than I do."
    cato "..."
    cato "If it ever gets too hard, let me know and you can take a break."

    show mc surprise at portrait
    mc "No, no! Even if it's hard, it's still important work. When I talk to our patients, I feel like I'm actually working towards something."
    show mc sweat at portrait
    mc "Plus, I need to be working a certain amount of hours to be permanently hired."

    cato "Well, if you need the break, it's there. I'd still sign the papers."
    cato "What would they do? Fire me?"

    show mc neutral at portrait
    mc "(It's true. Cato had done a lot for the research facility. We wouldn't have the cure for other mindbugs and we'd know even less about the virus than we do now, if it weren't for him.)"






return
