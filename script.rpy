##Define IMages
image white = "#ffff"
image res = "bg_res.png"
image black = "#000"
image cs = "bg_class.png"
##Define Characters
define uk = Character("???", color="#0000")
define sy = Character("Sayori", color="#F89880")
define mk = Character("Moneka", color="#ff5500")
define yr = Character("Yaori", color="#b500ec" )
define nt = Character("Nazuki", color="#ff00f2")
define mc = Character("69Hikaru69", color=("#00b421"))
# Transform animations
transform chopper_anime:
    xalign 0.0
    linear 2.0 xalign 0.7
#Splash Screen
label splashscreen:
    scene white 
    with Pause(1)
    show text "Horrible Game Studios presents..." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1) 
    show rick:
        xalign 0.5
        yalign 0.5
    play sound "astley.mp3"
    with Pause(4)
    hide rick
    scene white
    show text "Warning this game is not for haters, lmao" with dissolve
    with Pause(3)
    play audio dokidokiintro
    hide text with dissolve
    show logo with dissolve
    with Pause(2)
    stop sound fadeout 6
    with Pause(2)
    hide logo with dissolve
    with Pause(2)
    play sound "mtrack.mp3"
    queue sound "mtrackl.mp3" loop
    return

label start:
    stop sound fadeout(0.5)
    #play music "soundt.mp3" volume 0.01 loop
    scene res
    uk "Heyyyyyyyyyyyyyyy"
    "I see an annoying pink haired rodent looking ass that looks like she just came out of an Isekai Harem type like 0 idea that she drawing more attention than fireworks during an execution type shit like "
    "This RODENT is my childhood friend and neighbor"
    "Yknow the kind of friend u saw once and they stuck with you for the rest of your life and they eventually start to stick with you?"
    "{cps=10}Yeah{/cps} that type of friend"
    "We used to go to school on days like these but the stupid pink rodent was too lazy and spent too much time sleeping"
    "But if she keeps running after me like this Id rather Hang Myself, but theres nothing to do so with right now so I guess Ill just wait."
    show image "sy_stand" with dissolve:
        zoom 1.5
    sy "Haaahhh...haaahhh..."
    sy "I forgot I was supposed to wake up every day, wouldve rathered staying asleep {cps=4}forever{/cps}, but here we are! Caught you this time! "
    mc "Maybe cuz I didnt have anywhere to hang myself so I decided to wait instead."
    scene res
    show image "sy_uwu.png":
        zoom 1.5
    sy "Pfft, meanie."
    with Pause(1)
    scene black
    show image "sy_hng.png":
        zoom 3
    play sound "sacry.mp3"
    with Pause(0.2)
    scene res
    stop sound fadeout 0.1
    show image "sy_uwu":
        zoom 1.5
    sy "You say that like u were going to actually do it"
    mc "Ofc I would"
    sy "Man ur REALLY mean"
    mc "Well, if people stare at you for acting weird then I don't want them to think we're a couple thatd be devastating."
    play audio "rizz.mp3"
    show image "duo.png":
        xalign 0.7
        yalign 0.7
    mc "Or would it?"
    with Pause(4)
    stop audio fadeout 1
    scene res
    show image "sy_uwu.png":
        zoom 1.5
    sy "I guess you do have it in you to be mean like the chopper that kobe was in if you want to~"
    mc "This woman is delusional I swear"
    sy "Ehehe~"
    scene black
    "After this me and the rodent took kobe's chopper to school, "
    scene cs
    show image "copter.jpeg":
        chopper_anime
    with Pause(2)
    show image "explode.jpeg":
        xalign 0.7
    play audio "vbm.mp3"
    with Pause(2)
    scene cs
    "Were here"