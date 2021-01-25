"""icons.py  -- TreeLine icons information & constants

resolve_icon(code)  -- return an ICON_ designator, given an input

icons  -- list of all icons
symbols  -- dictionary from symbol -> icon
"""

#region Icon Constants

ICON_ANCHOR = "anchor"
ICON_ARROW_1 = "arrow_1"
ICON_ARROW_2 = "arrow_2"
ICON_ARROW_3 = "arrow_3"
ICON_ARROW_4 = "arrow_4"
ICON_ARROW_5 = "arrow_5"
ICON_BELL = "bell"
ICON_BOOKMARK = "bookmark"
ICON_BOOK_1 = "book_1"
ICON_BOOK_2 = "book_2"
ICON_BOOK_3 = "book_3"
ICON_BULB = "bulb"
ICON_BULLET_1 = "bullet_1"
ICON_BULLET_2 = "bullet_2"
ICON_BULLET_3 = "bullet_3"
ICON_CHECK_1 = "check_1"
ICON_CHECK_2 = "check_2"
ICON_CHECK_3 = "check_3"
ICON_CLOCK = "clock"
ICON_COLORS = "colors"
ICON_DATE_1 = "date_1"
ICON_DATE_2 = "date_2"
ICON_DEFAULT = "default"
ICON_DISK = "disk"
ICON_DOC = "doc"
ICON_EURO = "euro"
ICON_FOLDER_1 = "folder_1"
ICON_FOLDER_2 = "folder_2"
ICON_FOLDER_3 = "folder_3"
ICON_GEAR = "gear"
ICON_GNU = "gnu"
ICON_HAND = "hand"
ICON_HEART = "heart"
ICON_HOME = "home"
ICON_LOCK_1 = "lock_1"
ICON_LOCK_2 = "lock_2"
ICON_MAG = "mag"
ICON_MAIL = "mail"
ICON_MINUS = "minus"
ICON_MISC = "misc"
ICON_MOVE = "move"
ICON_MUSIC = "music"
ICON_NOTE = "note"
ICON_PENCIL = "pencil"
ICON_PERSON = "person"
ICON_PHONE = "phone"
ICON_PLUS = "plus"
ICON_PRINT = "print"
ICON_QUESTION = "question"
ICON_ROCKET = "rocket"
ICON_ROUND_MINUS = "round_minus"
ICON_ROUND_PLUS = "round_plus"
ICON_SMILEY_1 = "smiley_1"
ICON_SMILEY_2 = "smiley_2"
ICON_SMILEY_3 = "smiley_3"
ICON_SMILEY_4 = "smiley_4"
ICON_SMILEY_5 = "smiley_5"
ICON_SPHERE = "sphere"
ICON_STAR = "star"
ICON_SUM = "sum"
ICON_TABLE = "table"
ICON_TASK_1 = "task_1"
ICON_TASK_2 = "task_2"
ICON_TERM = "term"
ICON_TEXT = "text"
ICON_TRASH = "trash"
ICON_TREELINE = "treeline"
ICON_TREELOGO = "treelogo"
ICON_TUX_1 = "tux_1"
ICON_TUX_2 = "tux_2"
ICON_WARNING = "warning"
ICON_WRENCH = "wrench"
ICON_WRITE = "write"
ICON_X_1 = "x_1"
ICON_X_2 = "x_2"
ICON_X_3 = "x_3"


#endregion
#region all icons

icons = [ICON_ANCHOR, ICON_ARROW_1, ICON_ARROW_2, ICON_ARROW_3,
         ICON_ARROW_4, ICON_ARROW_5, ICON_BELL, ICON_BOOKMARK,
         ICON_BOOK_1, ICON_BOOK_2, ICON_BOOK_3, ICON_BULB,
         ICON_BULLET_1, ICON_BULLET_2, ICON_BULLET_3, ICON_CHECK_1,
         ICON_CHECK_2, ICON_CHECK_3, ICON_CLOCK, ICON_COLORS,
         ICON_DATE_1, ICON_DATE_2, ICON_DEFAULT, ICON_DISK, ICON_DOC,
         ICON_EURO, ICON_FOLDER_1, ICON_FOLDER_2, ICON_FOLDER_3,
         ICON_GEAR, ICON_GNU, ICON_HAND, ICON_HEART, ICON_HOME,
         ICON_LOCK_1, ICON_LOCK_2, ICON_MAG, ICON_MAIL, ICON_MINUS,
         ICON_MISC, ICON_MOVE, ICON_MUSIC, ICON_NOTE, ICON_PENCIL,
         ICON_PERSON, ICON_PHONE, ICON_PLUS, ICON_PRINT, ICON_QUESTION,
         ICON_ROCKET, ICON_ROUND_MINUS, ICON_ROUND_PLUS, ICON_SMILEY_1,
         ICON_SMILEY_2, ICON_SMILEY_3, ICON_SMILEY_4, ICON_SMILEY_5,
         ICON_SPHERE, ICON_STAR, ICON_SUM, ICON_TABLE, ICON_TASK_1,
         ICON_TASK_2, ICON_TERM, ICON_TEXT, ICON_TRASH, ICON_TREELINE,
         ICON_TREELOGO, ICON_TUX_1, ICON_TUX_2, ICON_WARNING,
         ICON_WRENCH, ICON_WRITE, ICON_X_1, ICON_X_2, ICON_X_3]


#endregion
#region resolve_icon

symbols = {
    '^': ICON_ARROW_1,
    'v': ICON_ARROW_2,
    '<-': ICON_ARROW_3,
    '->': ICON_ARROW_4,
    'g-openbook': ICON_BOOK_1,
    'r-book': ICON_BOOK_2,
    'g-book': ICON_BOOK_3,
    '(r)': ICON_BULLET_1,
    '(g)': ICON_BULLET_2,
    '(b)': ICON_BULLET_3,
    './': ICON_CHECK_2,
    'chkbox': ICON_CHECK_3,
    '(12)': ICON_CLOCK,
    '(31)': ICON_DATE_1,
    'folder': ICON_FOLDER_1,
    'openfolder': ICON_FOLDER_2,
    '<3': ICON_HEART,
    'locked': ICON_LOCK_1,
    'unlocked': ICON_LOCK_2,
    '(-)': ICON_ROUND_MINUS,
    '(+)': ICON_ROUND_PLUS,
    '-': ICON_MINUS,
    '+': ICON_PLUS,
    '(*)': ICON_MISC,
    '?': ICON_QUESTION,
    ':)': ICON_SMILEY_1,
    ':(': ICON_SMILEY_2,
    ':|': ICON_SMILEY_3,
    'B)': ICON_SMILEY_4,
    ':O': ICON_SMILEY_5,
    'O': ICON_SPHERE,
    '*': ICON_STAR,
    '#': ICON_TABLE,
    'notes': ICON_TASK_1,
    '/!\\': ICON_WARNING,
    'black-x': ICON_X_1,
    'red-x': ICON_X_2,
    '(x)': ICON_X_3
}


def resolve_icon(code):
    if code in icons:
        return code
    if code in symbols:
        return symbols[code]
    raise ValueError(code)


#endregion
