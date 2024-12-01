# Check for Incompatible Ren'Py Version

python early:

    if renpy.version_tuple < (6,99,12,4,2187): # Older than 6.99.12.4.2187
        renpy.error("This version of Ren'Py is too outdated for DDMT. Please update to at least Ren'Py 6.99.12.4.2187.")

    elif renpy.version_tuple > (7,6,1,23060707) and renpy.version_tuple[0] == 7:
        renpy.error("This version of Ren'Py 7 is too new for DDMT. Please downgrade to at most Ren'Py 7.6.1.23060707")

    elif renpy.version_tuple > (8,1,1,23060707) and renpy.version_tuple[0] == 8:
        renpy.error("This version of Ren'Py 8 is too new for DDMT. Please downgrade to at most Ren'Py 8.1.1.23060707")

    elif renpy.version_tuple[0] > 8:
        renpy.error("This version of Ren'Py is too new for DDMT. Please downgrade to at most Ren'Py 7.6.1.23060707 or Ren'Py 8.1.1.23060707")