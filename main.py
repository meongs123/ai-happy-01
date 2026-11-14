import os, shutil

# Copy the v4 entry image ("Birthday surprise": grandmother laughing as a
# golden retriever puppy pops out of a birthday gift box) to the output dir.
# A plain copy is deterministic: both runs write the same bytes.
# No network, no randomness: the output is exactly the shipped image.
# The file is a JPEG by magic bytes; the name stays entry.png either way.
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
shutil.copyfile(src, os.path.join(out, "entry.png"))
