import os
import sys

print("Executable:", sys.executable)
print("Version:", sys.version)
print("CWD:", os.getcwd())
print("UName:", getattr(os, "uname", lambda: None)())
for evn in ("PATH", "PYTHONHOME", "PYTHONPATH"):
    print("{:s}: {:}".format(evn, os.environ.get(evn)))
print("sys.path:", sys.path)

import fontforge as ff

fontfile = sys.argv[1]

f = ff.open(fontfile)

for glyph in f.glyphs():
    glyph.correctDirection()

f.generate(fontfile)
