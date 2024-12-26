import python3-fontforge
import sys

fontfile = sys.argv[1]

f = python3-fontforge.open(fontfile)

for glyph in f.glyphs():
    glyph.correctDirection()

f.generate(fontfile)
