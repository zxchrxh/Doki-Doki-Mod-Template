# Backgrounds
image black = "#000"         # Black
image dark = "#000000e4"        # Black (with transparency)
image darkred = "#110000c8"     # Dark red
image white = "#fff"         # White
image splash = "bg/splash.png"  # Splash image (Team Salvato logo)
image end:                      # End 
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"     # Residential neighborhood
image bg class_day = "bg/class.png"                 # Classroom
image bg corridor = "bg/corridor.png"               # School corridor
image bg club_day = "bg/club.png"                   # Literature clubroom
image bg club_day2:                                 # Clubroom + 1/6 chance to show Sayori hanging poster
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png"                   # Clubroom closet
image bg bedroom = "bg/bedroom.png"                 # MC's bedroom
image bg sayori_bedroom = "bg/sayori_bedroom.png"   # Sayori's bedroom
image bg house = "bg/house.png"                     # Outside MC's house
image bg kitchen = "bg/kitchen.png"                 # MC's kitchen

image bg notebook = "bg/notebook.png"               # Poem game notebook
image bg notebook-glitch = "bg/notebook-glitch.png" # Poem game notebook (Glitched, from act 3)

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0



image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0