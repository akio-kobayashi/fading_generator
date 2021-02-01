#!/bin/sh

cat temp2.list | perl fading.pl 0 &
cat temp2.list | perl fading.pl 1 &
cat temp2.list | perl fading.pl 2 &
cat temp2.list | perl fading.pl 3 &
wait
