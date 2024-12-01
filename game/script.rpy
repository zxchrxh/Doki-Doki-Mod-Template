# Script.rpy

label start:

    # This sets the save file's anti-cheat number to the game's anti-cheat number.
    #
    # If a player loads a save file that's anti-cheat number does not match's the game's
    # anti-cheat number (like when loading a save file from someone else's game), it will
    # take the player to a separate scene where Monika scolds the player for cheating.
    #
    # Usually, it's best not to tamper with this.
    #
    # In DDLC, a new global (game-wide) anti-cheat number is generated at the end of
    # act 1, at the start of act 2, at the end of act 2, and at the start of act 3.
    $ anticheat = persistent.anticheat

    # These determine what the girls' names will be
    # upon starting the game from 'New Game'.
    $ s_name = "Sayori"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ m_name = "Monika"

    # These determine some quick preferences during the game.
    $ quick_menu = True                 # Whether or not the player is allowed to open the pause menu or use the textbox buttons.
    $ style.say_dialogue = style.normal # What dialogue type character's will write in (normal, glitchy, or broken)
    $ in_sayori_kill = None             # Whether or not the player is in Sayori's death scene (unused, safe to delete)
    $ allow_skipping = True             # Whether or not the player is allowed to skip dialogue (save file)
    $ config.allow_skipping = True      # Whether or not the player is allowed to skip dialogue (global, until game restart)
    # When disallowing skipping during the game, make sure to set both 'allow_skipping' and 'config.allow_skipping' to False.

    # This line of code shows a dialog box informing you (yes, you, the developer) about not yet deleting this line of code.
    # Delete this line of code so that you can start to write your game code!
    call screen dialog ("Welcome to Doki Doki Mod Template!\n\nYou have not added any game code yet or have not yet\ndeleted the line of code that shows this dialog box.\n\nPlease refer to script.rpy.", MainMenu(confirm=False))

    # Here's where you write your code. Usually, it's best
    # to call or jump to another label from another file.
    # Think of this part of the script as a flowchart to
    # help organize your mod's chapters and events.





    






    return # Make sure to end your game with "return"!

    # Below is DDLC's original flowchart, which you can use
    # as a reference or example. You can either delete this
    # to clear up space or keep it commented out.

    # if persistent.playthrough == 0:

    #     $ chapter = 0
    #     call ch0_main


    #     call poem


    #     $ chapter = 1
    #     call ch1_main
    #     call poemresponse_start
    #     call ch1_end


    #     call poem


    #     $ chapter = 2
    #     call ch2_main
    #     call poemresponse_start
    #     call ch2_end


    #     call poem


    #     $ chapter = 3
    #     call ch3_main
    #     call poemresponse_start
    #     call ch3_end

    #     $ chapter = 4
    #     call ch4_main

    #     python:
    #         try: renpy.file(config.basedir + "/hxppy thxughts.png")
    #         except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
    #     $ chapter = 5
    #     call ch5_main

    #     call endgame

    #     return

    # elif persistent.playthrough == 1:
    #     $ chapter = 0
    #     call ch10_main
    #     jump playthrough2


    # elif persistent.playthrough == 2:

    #     $ chapter = 0
    #     call ch20_main

    #     label playthrough2:


    #         call poem
    #         python:
    #             try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
    #             except: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())


    #         $ chapter = 1
    #         call ch21_main
    #         call poemresponse_start
    #         call ch21_end


    #         call poem (False)
    #         python:
    #             try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
    #             except: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())


    #         $ chapter = 2
    #         call ch22_main
    #         call poemresponse_start
    #         call ch22_end


    #         call poem (False)


    #         $ chapter = 3
    #         call ch23_main
    #         if y_appeal >= 3:
    #             call poemresponse_start2
    #         else:
    #             call poemresponse_start

    #         if persistent.demo:
    #             stop music fadeout 2.0
    #             scene black with dissolve_cg
    #             "End of demo"
    #             return

    #         call ch23_end

    #         return

    # elif persistent.playthrough == 3:
    #     jump ch30_main

    # elif persistent.playthrough == 4:

    #     $ chapter = 0
    #     call ch40_main
    #     jump credits

# This label indicates an endgame scene, originally seen
# at the end of act 1, after Sayori's hanging. This is
# not DDLC's credits scene, despite the name. That is
# located in credits.rpy.
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return