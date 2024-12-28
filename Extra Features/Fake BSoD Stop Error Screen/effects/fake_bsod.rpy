# Fake Blue Screen of Death / Stop Error Screen

# DDLC implements a fake BSoD scare during act 2.
# This attempts to recreate that effect with more customizability.
#
# The Windows BSoD now has a changing percentage for the fake error reporting
# as well as having the color of the background change depending on the version.
# The stop code can also be changed (default: CRITICAL_PROCESS_DIED).
#
# There are also now kernel panic screens for macOS and
# Linux distributions which were not present in DDLC.
#
# The correct stop error screen shows depending on the player's operating system.

# To display a BSoD, type the following into your script.
# call bsod (stop_code="CRITICAL_PROCESS_DIED", timer=0, delay=0, fullscreen_only=True, force_fullscreen=False)
# You can change any of the parameters to your liking.

# Parameter Definitions
# stop_code         = The stop code to show at the bottom of the Windows BSoD.
# timer             = The time to wait before continuing to the next interaction. If 0, wait until the player clicks.
# delay             = The time to wait before actually starting the BSoD.
# fullscreen_only   = If True, the BSoD will not happen if the player is not in fullscreen. Ignored if force_fullscreen is True.
# force_fullscreen  = If True, the player will be forced into fullscreen before the BSoD shows.

init python:
    class Screenshot(renpy.Displayable):
        def __init__(self):
            super(Screenshot, self).__init__()
            
        def render(self, width, height, st, at):
            srf = screenshot_srf()
            render = renpy.Render(srf.get_width(), srf.get_height())
            render.blit(srf, (0, 0))
            return render
    
    def bsod_percentage(st, at):

        x = random.random()

        if int(st * (5 + x)) < 100:
            percent = int(st * (5 + x))
        else:
            percent = 100

        d = Text(str(percent) + "% complete", style="bsod_windows_text")

        if percent < 100:
            return d, random.randint(2,3)
        else:
            return d, None

label bsod(stop_code="CRITICAL_PROCESS_DIED", timer=0, delay=0, fullscreen_only=True, force_fullscreen=False):

    if delay > 0:
        $ pause(delay)

    if fullscreen_only and not preferences.fullscreen and not force_fullscreen and not config.developer:
        return

    show expression Screenshot() as screenshot:
        size (config.screen_width,config.screen_height)
    window hide(None)
    window auto

    $ quick_menu = False
    $ config.allow_skipping = False

    if renpy.windows and platform.release() == "10" or platform.release() == "11":
        if renpy.music.get_pos() - 0.1 < 0:
            $ renpy.music.play("<from 0 to 0.1>" + renpy.music.get_playing().split('>')[-1])
        else:
            $ renpy.music.play("<from " + str(renpy.music.get_pos() - 0.1) + " to " + str(renpy.music.get_pos()) + ">" + renpy.music.get_playing().split('>')[-1])

        $ pause(1.0)

        $ mouse_visible = False

        if force_fullscreen:
            $ preferences.fullscreen = True

        show bsod_windows_blue:
            yoffset -480
            0.25/renpy.get_refresh_rate()
            yoffset -240
            0.25/renpy.get_refresh_rate()
            yoffset 0

        $ pause(1/renpy.get_refresh_rate())

        scene bsod_windows_blue

        show screen bsod_windows(stop_code)

        hide screenshot

    elif renpy.macintosh:

        if renpy.music.get_pos() - 0.3 < 0:
            $ renpy.music.play("<from 0 to 0.3>" + renpy.music.get_playing().split('>')[-1])
        else:
            $ renpy.music.play("<from " + str(renpy.music.get_pos() - 0.3) + " to " + str(renpy.music.get_pos()) + ">" + renpy.music.get_playing().split('>')[-1])

        $ mouse_visible = False

        $ pause(0.9)

        scene black

        $ pause(0.6)

        stop music

        $ pause(4)

        play sound "assets/fake_bsod/bsod_macos_sound.wav"

        $ pause(4)

        show expression "assets/fake_bsod/bsod_macos.png" at truecenter

    elif renpy.linux:

        if renpy.music.get_pos() - 0.3 < 0:
            $ renpy.music.play("<from 0 to 0.3>" + renpy.music.get_playing().split('>')[-1])
        else:
            $ renpy.music.play("<from " + str(renpy.music.get_pos() - 0.3) + " to " + str(renpy.music.get_pos()) + ">" + renpy.music.get_playing().split('>')[-1])

        show black:
            yoffset -360
            1/renpy.get_refresh_rate()
            yoffset 0

        $ pause(20/renpy.get_refresh_rate())

        scene black

        show black onlayer front:
            yoffset 12
            0.25/renpy.get_refresh_rate()
            yoffset 24
            0.25/renpy.get_refresh_rate()
            yoffset 36
            0.25/renpy.get_refresh_rate()
            yoffset 48
            0.25/renpy.get_refresh_rate()
            yoffset 60
            0.25/renpy.get_refresh_rate()
            yoffset 72
            0.25/renpy.get_refresh_rate()
            yoffset 84
            0.25/renpy.get_refresh_rate()
            yoffset 96
            0.25/renpy.get_refresh_rate()
            yoffset 108
            0.25/renpy.get_refresh_rate()
            yoffset 120
            0.25/renpy.get_refresh_rate()
            yoffset 132
            0.25/renpy.get_refresh_rate()
            yoffset 144
            0.25/renpy.get_refresh_rate()
            yoffset 156
            0.25/renpy.get_refresh_rate()
            yoffset 168
            0.25/renpy.get_refresh_rate()
            alpha 0

        show screen bsod_linux()

        stop music

        hide screenshot

    else:
        $ print("DDMT: Attempted to show a fake BSoD / Stop Error screen, but failed to determine operating system")

    $ pause(timer)

    $ quick_menu = True
    $ config.allow_skipping = True
    $ mouse_visible = True

    return

screen bsod_windows(stop_code):

    layer "master"

    style_prefix "bsod_windows"

    vbox:
        xalign 0.2
        yalign 0.4
        text ":(" style "bsod_windows_text_emoticon"
        text "Your device ran into a problem and needs to restart.\nWe're just collecting some error info, and then we'll\nrestart for you."
        null height 16
        add DynamicDisplayable(bsod_percentage)
        null height 32
        hbox:
            add "assets/fake_bsod/bsod_windows_qrcode.png"
            vbox:
                xpos 0.06
                vbox:
                    text "For more information about this issue and possible fixes, visit" style "bsod_windows_text_information"
                    text "https://www.windows.com/stopcode" style "bsod_windows_text_information"
                null height 16
                vbox:
                    text "If you call a support person, give them this info:" style "bsod_windows_text_support"
                    text "Stop code: [stop_code]" style "bsod_windows_text_support"

screen bsod_linux():
    layer "master"

    style_prefix "bsod_linux"

    python:
        version = platform.version()
        machine = platform.machine()

    vbox:
        text "  Kernel panic  -  not syncing: VFS: Unable to mount root fs on unknown-block(0,0)"
        text "  CPU: 0 PID: 1 Comm: swapper/0 Not tainted [version].[machine] #1"
        text "  Hardware name: Metaverse Enterprise Solutions Virtual Platform/440BX Desktop Reference Platform, BIOS 1.1.1 11/06/2021"
        text "  Call Trace:"
        text "    [[<ffffffffb8a2e073>] dump_stack+0x63/0x90"
        text "    [[<ffffffffb879e6ad>] panic+0xe4/0x226"
        text "    [[<ffffffffb9586540>] mount_block_root+0x1fb/0x2c2"
        text "    [[<ffffffffb958663a>] mount_root+0x33/0x35"
        text "    [[<ffffffffb9586776>] prepare_namespace+0x13a/0x18f"
        text "    [[<ffffffffb95861eb>] kernel_init_freeable+0x1ee/0x217"
        text "    [[<ffffffffb8e8d2ae>] kernel_init+0xe/0x100"
        text "    [[<ffffffffb8e9aa1f>] ret_from_fork+0x1f/0x40"
        text "    [[<ffffffffb8e8d2a0>] ? rest_init+0x80/0x80"

style bsod_windows_text:
    color "#fff"
    font "C:/Windows/Boot/Fonts/segoe_slboot.ttf"
    size 24
    slow_cps renpy.get_refresh_rate()*(renpy.get_refresh_rate()/2)
    line_leading 2
    line_spacing -2
    outlines []

style bsod_windows_text_emoticon is bsod_windows_text:
    size 128
    xpos -8

style bsod_windows_text_information is bsod_windows_text:
    size 12

style bsod_windows_text_support is bsod_windows_text:
    size 10

style bsod_linux_text is console_text:
    font "assets/fake_bsod/terminus.ttf"
    size 16

image bsod_windows_blue = ConditionSwitch(
    "platform.release() == '11'", "#023d92",
    "platform.release() == '10'", "#0078d7"
)