import os, shutil

# Copy the entry image to the output directory.
# A plain copy is deterministic: both runs write the same bytes.
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
shutil.copyfile(src, os.path.join(out, "entry.png"))
