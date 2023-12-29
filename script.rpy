image white = "#ffff"

label splashscreen:
    scene white
    show text "Horrible game studios presents..." with dissolve
    with Pause(2)
    hide text with dissolve
    show image "rick":
        xalign 0.5
        yalign 0.5
    play sound "inrickroll.mp3"
    with Pause(4)
    hide image "rick"
    show text "Warning, this game is not for haters, lmao" with dissolve
    with Pause(3)
    hide text with dissolve
    show image "ddlcbb_logo"
    play audio "intro.mp3"
    with Pause(2)
    stop sound fadeout 6
    with Pause(2)
    play sound "mtrack.mp3"
    queue sound "mtrackl.mp3"




