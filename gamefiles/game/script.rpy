image white = "#ffff"
define sy = Character("Sayore", color="#BC131F")
define mk = Character("Moneka", color="#1e0027")
transform midright:
    xalign 0.7

transform mid:
    xalign 0.5

transform midleft:
    xalign 0.3

transform zoomer:
    zoom 1.5


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
    hide rick fade
    scene white

    show text "Warning this game is not for haters, lmao" with dissolve
    with Pause(3)

    play audio dokidokiintro
    hide text with dissolve

    show ddlcbb_logo with dissolve
    with Pause(2)
    stop sound fadeout 6
    with Pause(2)

    hide ddlcbb_logo with dissolve
    with Pause(2)
    play audio "mtrack.mp3"
    queue music "mtrackl.mp3"
    return

label start:
    scene cool
    show sautori colored at midleft:
        zoomer

    sy "Wazza my nigga welcome to da hood"

    show moneka at midright:
        zoomer

    mk "Wazza nigga u cool"


    sy "Nigga follow me"
    scene hotcool
    play music "audio/airhorn.mp3"

    "After that they hit it out of the park so hard the moon dissapeared"

    stop music
    return

    
    