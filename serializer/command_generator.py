"""Command generator:

Receives a coordinate tuple and makes a smart decision
on what command is appropriate.
Returns a string of the command.
"""


def generate_command(tup, etup=None):
    """
      args:
          tup - Coordinate tuple.
              format: (r1, c1, r2, c2)
          etup - Erase cell tuple.
              format: (r, c)
    """

    if (etup is not None):
        # erase a single cell.
        return 'ERASE_CELL ' + str(etup[0]) + ' ' + str(etup[1])

    if ((tup[0] == tup[2]) and (tup[1] == tup[3])):
        # draw a single cell.
        return 'PAINT_SQUARE ' + str(tup[0]) + ' ' + str(tup[1]) + ' 0'

    elif ((tup[0] == tup[2]) or (tup[1] == tup[3])):
        # draw a line.
        return 'PAINT_LINE %s %s %s %s' % (str(tup[0]), str(tup[1]),
                                           str(tup[2]), str(tup[3]))
    else:
        # draw a square
        s = tup[2] - tup[0] + 1
        s = (s - 1) / 2
        c = ((tup[0] + tup[2]) / 2, (tup[1] + tup[3]) / 2)
        return 'PAINT_SQUARE %s %s %s' % (str(c[0]), str(c[1]), s)
