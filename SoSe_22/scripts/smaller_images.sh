#!/bin/bash

for i in $PWD/*.JPG; do
	convert "$i" -resize 30%  "$PWD/${i##*/}"
done


