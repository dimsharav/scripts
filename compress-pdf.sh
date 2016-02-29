#!/bin/sh
echo Compress arguments...
echo For filenames with spaces use "*.pdf"
echo " "

compressed_dir="compressed"
mkdir $compressed_dir
for file in $*; do
    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$compressed_dir/"$file" "$file"
done
