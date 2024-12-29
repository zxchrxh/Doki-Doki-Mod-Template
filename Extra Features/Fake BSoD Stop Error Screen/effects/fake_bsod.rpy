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
# stop_code         = The stop code to show at the bottom of the Windows BSoD (recommended).
# file              = The failing file to show at the bottom of the Windows BSoD (optional).
# timer             = The time to wait before continuing to the next interaction. If 0, wait until the player clicks.
# delay             = The time to wait before actually starting the BSoD.
# fullscreen_only   = If True, the BSoD will not happen if the player is not in fullscreen. Ignored if force_fullscreen is True.
# force_fullscreen  = If True, the player will be forced into fullscreen before the BSoD shows.

init python:

    import platform
    import winreg

    class Screenshot(renpy.Displayable):
        def __init__(self):
            super(Screenshot, self).__init__()
            
        def render(self, width, height, st, at):
            srf = screenshot_srf()
            render = renpy.Render(srf.get_width(), srf.get_height())
            render.blit(srf, (0, 0))
            return render
    
    def bsod_percentage(st, at, win8=False):

        x = random.random()

        if int(st * (5 + x)) < 100:
            percent = int(st * (5 + x))
        else:
            percent = 100

        if win8:
            d = Text("Your PC ran into a problem and needs to restart. We're just\ncollecting some error info, and then we'll restart for you. (" + str(percent) + "%\ncomplete)", style="bsod_windows_segoe_text")
        else:
            d = Text(str(percent) + "% complete", style="bsod_windows_segoe_text")

        if percent < 100:
            return d, random.randint(2,3)
        else:
            return d, None

    winbuild = int(winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion"), "CurrentBuild")[0])

label bsod(stop_code="CRITICAL_PROCESS_DIED", file="win32k.sys", timer=0, delay=0, fullscreen_only=True, force_fullscreen=False):

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

    $ renpy.windows = False
    $ renpy.macintosh = True

    if renpy.windows:
        if renpy.music.get_pos() - 0.1 < 0:
            $ renpy.music.play("<from 0 to 0.1>" + renpy.music.get_playing().split('>')[-1])
        else:
            $ renpy.music.play("<from " + str(renpy.music.get_pos() - 0.1) + " to " + str(renpy.music.get_pos()) + ">" + renpy.music.get_playing().split('>')[-1])

        $ pause(1.0)

        $ mouse_visible = False

        if force_fullscreen:
            $ preferences.fullscreen = True

        if winbuild < 9200:
            scene black

        show bsod_windows_blue:
            yoffset -480
            0.25/renpy.get_refresh_rate()
            yoffset -240
            0.25/renpy.get_refresh_rate()
            yoffset 0

        $ pause(1/renpy.get_refresh_rate())

        scene bsod_windows_blue

        show screen bsod_windows(stop_code, file)

        hide screenshot

    elif renpy.macintosh:

        stop music

        $ mouse_visible = False

        $ pause(0.3)

        show black onlayer front:
            alpha 0.5
            yoffset -config.screen_height
            linear 1.5 yoffset 0

        $ pause(1.7)

        show expression "assets/fake_bsod/bsod_macos.png" at truecenter onlayer front

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

screen bsod_windows(stop_code, file):

    layer "master"

    if winbuild >= 9200:

        style_prefix "bsod_windows_segoe"

        vbox:
            if winbuild >= 10240:
                xalign 0.2
            else:
                xalign 0.4
            yalign 0.4
            text ":(" style "bsod_windows_segoe_text_emoticon"
            if winbuild >= 10240:
                text "Your device ran into a problem and needs to restart.\nWe're just collecting some error info, and then we'll\nrestart for you."
                null height 16
                add DynamicDisplayable(bsod_percentage)
                null height 32
                hbox:
                    add "assets/fake_bsod/bsod_windows_qrcode.png"
                    vbox:
                        xpos 0.06
                        vbox:
                            text "For more information about this issue and possible fixes, visit" style "bsod_windows_segoe_text_information"
                            text "https://www.windows.com/stopcode" style "bsod_windows_segoe_text_information"
                        null height 16
                        vbox:
                            text "If you call a support person, give them this info:" style "bsod_windows_segoe_text_support"
                            text "Stop code: [stop_code]" style "bsod_windows_segoe_text_support"
                            if file:
                                text "What failed: [file]" style "bsod_windows_segoe_text_support"
            else:
                add DynamicDisplayable(bsod_percentage, win8=True)
                null height 16
                text "If you'd like to know more, you can search online later for this error: [stop_code]" style "bsod_windows_segoe_text_information"
    
    else:

        style_prefix "bsod_windows_lucida"

        vbox:
            text """
A problem has been detected and Windows has been shut down to prevent damage
to your computer.
"""

            if stop_code:
                text "[stop_code]"

            text """
If this is the first time you've seen this Stop error screen,
restart your computer. If this screen appears again, follow
these steps:

Check to make sure any new hardware or software is properly installed.
If this is a new installation, ask your hardware or software manufacturer
for any Windows updates you might need.

If problems continue, disable or remove any newly installed hardware
or software. Disable BIOS memory options such as caching or shadowing.
If you need to use Safe Mode to remove or disable components, restart
your computer, press F8 to select Advanced Startup Options, and then
select Safe Mode.

Technical Information:

*** STOP: 0x000000F4 (0x00000003,0x84A467A0,0x8CFB8CD4,0x00000000)

"""

            if file:
                text "*** [file]  -  Address 8CFB8CD4 base at 8CE00000, DateStamp 4549aea2"

screen bsod_linux():
    layer "master"

    style_prefix "bsod_linux"

    python:
        version = platform.version()
        machine = platform.machine()

    vbox:
        text "Kernel panic  -  not syncing: VFS: Unable to mount root fs on unknown-block(0,0)"
        text "CPU: 0 PID: 1 Comm: swapper/0 Not tainted [version].[machine] #1"
        text "Hardware name: Metaverse Enterprise Solutions Virtual Platform/440BX Desktop Reference Platform, BIOS 1.1.1 11/06/2021"
        text "Call Trace:"
        text "  [[<ffffffffb8a2e073>] dump_stack+0x63/0x90"
        text "  [[<ffffffffb879e6ad>] panic+0xe4/0x226"
        text "  [[<ffffffffb9586540>] mount_block_root+0x1fb/0x2c2"
        text "  [[<ffffffffb958663a>] mount_root+0x33/0x35"
        text "  [[<ffffffffb9586776>] prepare_namespace+0x13a/0x18f"
        text "  [[<ffffffffb95861eb>] kernel_init_freeable+0x1ee/0x217"
        text "  [[<ffffffffb8e8d2ae>] kernel_init+0xe/0x100"
        text "  [[<ffffffffb8e9aa1f>] ret_from_fork+0x1f/0x40"
        text "  [[<ffffffffb8e8d2a0>] ? rest_init+0x80/0x80"
        text "_" at bsod_linux_caret_blink

style bsod_windows_segoe_text:
    color "#fff"
    font "C:/Windows/Boot/Fonts/segoe_slboot.ttf"
    size 24
    slow_cps renpy.get_refresh_rate()*(renpy.get_refresh_rate()/2)
    line_leading 2
    line_spacing -2
    outlines []

style bsod_windows_segoe_text_emoticon is bsod_windows_segoe_text:
    size 128
    xpos -8

style bsod_windows_segoe_text_information is bsod_windows_segoe_text:
    size 12

style bsod_windows_segoe_text_support is bsod_windows_segoe_text:
    size 10

style bsod_windows_lucida_text:
    color "#fff"
    font "C:/Windows/Fonts/LUCON.TTF"
    antialias False
    size 16
    slow_cps renpy.get_refresh_rate()*(renpy.get_refresh_rate()/2)
    outlines []

style bsod_linux_text is console_text:
    font "assets/fake_bsod/terminus.ttf"
    size 16

transform bsod_linux_caret_blink:
    alpha 1.0
    0.5
    alpha 0.0
    0.5
    repeat

image bsod_windows_blue = ConditionSwitch(
    "winbuild >= 22000", "#023d92",
    "winbuild >= 9200", "#0078d7",
    "winbuild < 9200", "#000080"
)