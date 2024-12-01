# Python Functions

init python:

    # Gets the position of the currently playing
    # audio in the specified channel (in seconds)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

    # Deletes all save files
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    # Deletes the specified character file in /characters/
    def delete_character(name):
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass

    # Deletes all character file in /characters/
    def delete_all_characters():
        try:
            for name in os.listdir(config.basedir + "/characters/"):
                if name.endswith(".chr"):
                    os.remove(config.basedir + "/characters/" + name)
        except: pass

    # Restores the specified character file from /game/character_files/ to /characters/
    def restore_character(name):
        try: renpy.file("../characters/" + name + ".chr")
        except: open(config.basedir + "/characters/" + name + ".chr", "wb").write(renpy.file("character_files/" + name + ".chr").read())

    # Restores all character files from /game/character_files to /characters/
    def restore_all_characters():
        try:
            for name in os.listdir(config.basedir + "/game/character_files/"):
                if name.endswith(".chr"):
                    try: renpy.file("../characters/" + name)
                    except: open(config.basedir + "/characters/" + name, "wb").write(renpy.file(name).read())
        except: pass

    # In DDLC, this was used to restore the correct characters
    # for the correct act. It would start by restoring all
    # characters, then deleting the characters based on
    # which act the player was in.
    def restore_relevant_characters():
        restore_all_characters()
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            delete_character("sayori")
        elif persistent.playthrough == 3:
            delete_character("sayori")
            delete_character("natsuki")
            delete_character("yuri")
        elif persistent.playthrough == 4:
            delete_character("monika")

    # Pause. Use this instead of the regular Ren'Py pause.
    def pause(time=None):
        global _windows_hidden
        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0: return
        _windows_hidden = True
        renpy.pause(time)
        _windows_hidden = False