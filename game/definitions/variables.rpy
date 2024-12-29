# Variables

# This variable determines whether or not the game is in a demo mode.
#
# Team Salvato used this during development to prevent playtesters
# from proceeding to a part of the game that wasn't finished.
#
# It isn't useful for developing your mod and is safe to delete, unless you
# choose to implement a demo / shortened version of your mod for play-testing.
define persistent.demo = False

# This variable determines whether or not the game is being
# played from a version of DDLC downloaded from Steam.
#
# DDLC uses this in Act 3, where Monika asks you to check
# on her character file, and tells you how to get there.
define persistent.steam = ("steamapps" in config.basedir.lower())

# This variable determines whether or not
# Ren'Py's developer mode should be enabled.
#
# Developer mode gives you access to tools that will
# help you create your mod with the following keybinds:
# Shift+D - Developer Menu
# Shift+R - Reload Game
# Shift+O - Console
#
# Keep this set to "auto" as it will automatically set
# developer mode on or off depending if the game is
# run from the Ren'Py SDK or a built distribution.
#
# You can learn more about Ren'Py's developer mode
# at https://renpy.org/doc/html/developer_tools.html.
define config.developer = "auto"

# This variable determines whether or not
# to enable auto-reload with Shift+R.
#
# If you use VS Code with Auto Save enabled,
# it's a good idea to set this to True.
define config.autoreload = (".vscode" not in os.listdir(config.basedir))

# This variables determines whether or not
# the player is allowed to skip pauses.
#
# By default, the player is only allowed to skip
# pauses if Ren'Py's developer mode is enabled.
#
# Usually, there is no need to change this.
define _dismiss_pause = config.developer

# Character Objects
define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

# Default Persistent & Local Variables
default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None
default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"

default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

default poemwinner = ['sayori', 'sayori', 'sayori']

default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

default n_read3 = False
default y_read3 = False

default n_poemearly = False

default poemsread = 0

default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

default n_exclusivewatched = False
default y_exclusivewatched = False

default y_gave = False
default y_ranaway = False

default ch1_choice = "sayori"

default help_sayori = None
default help_monika = None

default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True

default natsuki_23 = None