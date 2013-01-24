#!/bin/sh
# 
# Уменьшение размера файлов 
# и изменение размера изображений .jpg в каталоге
# 
# Зависимости:
#     mjpegtools (для jpegtran)
#     imagemagick
# 
 
for f in *.jpg
do
    jpegtran -copy none -optimize "$f" > "tmp$f"
    convert -resize 2048 "tmp$f" "new$f"
    rm -f "tmp$f"
done

