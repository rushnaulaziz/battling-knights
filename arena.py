
from item import Item
from tile import Tile
from knight import Knight
import configuration as CONFIGURATION


class Arena:
    """
    The class maintians	8x8	square	"Arena"	

    The `board` property is a matrix that contains the	64	tiles	on	the	board which  are	identified	with	(row,	col)	co-ordinates	with	(0,0)	being	the	top	left	
    tile	and	(7,0)	being	the	bottom	left	tile	(row	7	col	0).
    """
    board = tuple(tuple([Tile(col, row) for row in range(0, CONFIGURATION.ARENA_COLUMNS+1)])
                  for col in range(0, CONFIGURATION.ARENA_ROWS+1))

    