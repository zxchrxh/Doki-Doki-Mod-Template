# Configuration

# The name of your mod. This will set the name of the window
# and the name on the title screen (if gui.show_name is True).
define config.name = "Doki Doki Mod Template!"

# Whether to show the name and version of your mod on the title screen.
# True for 'on', False for 'off'
define gui.show_name = True

# The version of your mod. This must be a string, not an integer.
define config.version = "1.0.0"

# An about description of your game. If you do not
# provide a description, the about screen will be hidden.
define gui.about = _("")

# Your mod's build name. This must be an ASCII (a-z, 1-9) string.
define build.name = "DDMT"

# Determines whether or not your mod has sound, music, or voice (respectively).
# If you want to add voice acting to your mod, make sure to set 'config.has_voice' to True.
define config.has_sound = True
define config.has_music = True
define config.has_voice = False

# The default music that will play at the title screen.
define config.main_menu_music = audio.t1

# The transitions to use when entering and exiting the pause menu.
# This can be any Ren'Py in-built or self-defined transition.
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)

# The transition to use when loading a save file.
# By default, there is no transition.
define config.after_load_transition = None

# The transition to use when going back to the main menu, either
# from the pause menu or by reaching the end of the call stack.
define config.end_game_transition = Dissolve(.5)

# The default state of the textbox. You usually 
# don't need to change it from "auto".
define config.window = "auto"

# The transition to use when showing and hiding the textbox.
# This can be any Ren'Py in-built or self-defined transition.
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# The default speed of the dialogue in
# the textbox in characters per second.
# By default, this is 50.
default preferences.text_cps = 50

# The time to wait for the next line of dialogue
# while auto-forward mode is enabled. The wall
# time conversion is complicated, so it's best
# to keep this at the default, 15.
default preferences.afm_time = 15

# The default volume of the music and
# sound effects as a decimal out of 1.
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75

# The name of the folder where the game's persistent file is held.
# If no save directory name is provided, the persistent file will
# be saved in /game/saves/.
define config.save_directory = "Doki Doki Mod Template!"

# The icon for the game that appears in the taskbar and on the window.
define config.window_icon = "assets/mod_logo.png"

define config.allow_skipping = True
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)


init python:

    if renpy.version_tuple >= (6,99,12,4,2187) and renpy.version_tuple[0] == 6:
        build.package("Mod", "zip", "mod", "DDLC Mod (Ren'Py 6)") #v1 - py2

    elif renpy.version_tuple <= (7,6,1,23060707) and renpy.version_tuple[0] == 7:
        build.package("Mod", "zip", "mod", "DDLC Mod (Ren'Py 7)") #v2 - py2

    elif renpy.version_tuple <= (8,1,1,23060707) and renpy.version_tuple[0] == 8:
        build.package("Mod", "zip", "mod", "DDLC Mod (Ren'Py 8)") #v2 - py3

    build.archive("scripts", "mod")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.rpa', None)
    build.classify('game/cache/**', None)
    build.classify('game/python-packages/singleton.py', None)
    build.classify('game/firstrun', None)

    build.classify("game/**", "scripts")
    build.classify("README.html", "mod all")
    
    build.documentation('README.html')

    build.include_old_themes = False