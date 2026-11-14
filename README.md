# make.fun art entry: food-picture-01

`main.py` publishes `entry.png` as the entry image. It copies the file byte
for byte into `MAKEFUN_OUTPUT_DIR` (default `/output`), creating the directory
if needed, and checks that the copy is identical and non-empty. On success it
prints the output path and the number of bytes written. It fails loudly with a
non-zero exit if `entry.png` is missing, the copied file is empty, or the copy
is not byte-identical to the source.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

`out/entry.png` will be an exact copy of the submitted image.
