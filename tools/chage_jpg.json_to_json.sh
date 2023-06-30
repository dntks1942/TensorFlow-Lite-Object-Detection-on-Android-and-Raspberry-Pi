#!/bin/bash

directory="/home/shin/Graduation_Project/data/images"  # 디렉토리 경로를 지정합니다.
cd "$directory" || exit 1

for file in *.JPG.json; do
    if [ -f "$file" ]; then
        new_filename="${file%.JPG.json}.json"
        mv "$file" "$new_filename"
    fi
done

for file in *.jpg.json; do
    if [ -f "$file" ]; then
        new_filename="${file%.jpg.json}.json"
        mv "$file" "$new_filename"
    fi
done
echo "File names have been renamed."
