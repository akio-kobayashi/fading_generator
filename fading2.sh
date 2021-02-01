#!/bin/sh

head temp3.list | perl fading2.pl 0 &
head temp3.list | perl fading2.pl 1 &
head temp3.list | perl fading2.pl 2 &
head temp3.list | perl fading2.pl 3 &
wait
