# Check for Missing RPAs

python early:

    for archive in ['audio','images','fonts']:
        if archive not in config.archives:
            renpy.error("'" + archive + ".rpa' could not be found in the 'game' folder. Please place the missing RPA file in the 'game' folder and try again.")