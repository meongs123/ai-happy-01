import os, shutil

# Copy the v2 entry image ("The reunion") to the output directory.
# A plain copy is deterministic: both runs write the same bytes.
# No network, no randomness: the output is exactly the shipped image.
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
shutil.copyfile(src, os.path.join(out, "entry.png"))
