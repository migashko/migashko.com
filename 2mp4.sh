#!/bin/bash
#Shell Script which converts all videos in a folder to MP4


#for file in *.*;
IFS=$'\n'; set -f
for file in $(find . -name '*.avi' -or -name "*.wmv" -or -name "*.flv" -or -name "*.mkv" -or -name "*.ts");	
do 
  echo "${file}"
  #if ! -d {file}; then
  #  echo      if[ ${file: -4} != ".mp4"]   #don't want to convert mp4 files           
  ffmpeg -i "$file" ${file%.*}.mp4
  #fi
done
unset IFS; set +f

