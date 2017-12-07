#!/usr/bin/python
#
# Copyright (C) 2016 Matthew Barnes <mbarnes2084@gmail.com>
#
# This script queries the SQLite games database produced by GNOME Video
# Arcade and locates vertically-oriented arcade games appropriate for my
# cocktail-style arcade cabinet.
#

import os.path
import sqlite3

GAMESDB = '~/.local/share/gnome-video-arcade/games.db'

conn = sqlite3.connect(os.path.expanduser(GAMESDB))

cursor = conn.cursor()

query_games = (
    'SELECT name, description, year'
    ' FROM game LEFT JOIN display ON game.name = display.game'
    ' WHERE (display.rotate = "90" OR display.rotate = "270")'
    ' AND CAST(year AS INTEGER) < 1990')

for name, desc, year in cursor.execute(query_games):
    print('{0}        // {1} [{2}]'.format(name.ljust(11), desc, year))
