# Check for Incompatible Ren'Py Version

python early:

    if renpy.version_tuple != (8,1,1,23060707):

        import webbrowser

        with open(config.basedir + "/RenPyVersionError.txt", "w") as f:

            if renpy.version_tuple < (8,1,1,23060707):

                if ("lib" or "renpy") not in os.listdir(config.basedir):
                    
                    if renpy.version_tuple[0] == 8:
                        f.write("This version of Ren'Py 8 is too old for DDMT.\nPlease upgrade to Ren'Py 8.1.1.")

                    else:
                        f.write("This version of Ren'Py is too old for DDMT.\nPlease upgrade to Ren'Py 8.1.1.")

                else:
                    f.write("An error has occurred.\nPlease replace all of the files in the '/lib/' and '/renpy/' folders with the ones included with this mod.\n\n" + config.name + " " + config.version + "\n" + renpy.version())

            if renpy.version_tuple > (8,1,1,23060707):

                if ("lib" or "renpy") not in os.listdir(config.basedir):

                        if renpy.version_tuple[0] == 8:
                            f.write("This version of Ren'Py 8 is too new for DDMT.\nPlease downgrade to Ren'Py 8.1.1.")

                        else:
                            f.write("This version of Ren'Py is too new for DDMT.\nPlease downgrade to Ren'Py 8.1.1.")

                else:
                    f.write("An error has occurred.\nSomehow, your version of Ren'Py is too new for this mod.\nPlease contact the mod developer for support.\n\n" + config.name + " " + config.version + "\n" + renpy.version())

            f.close()

        webbrowser.open(config.basedir + "/RenPyVersionError.txt")

        renpy.quit()