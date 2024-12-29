from fontforge import *
from sys import argv

fontfile = sys.argv[1]

f = fontforge.open(fontfile)

for glyph in f.glyphs():
    glyph.correctDirection()

f.generate(fontfile)
