import fontforge as ff
import sys

fontfile = sys.argv[1]

f = ff.open(fontfile)

for glyph in f.glyphs():
    glyph.correctDirection()

f.generate(fontfile)
