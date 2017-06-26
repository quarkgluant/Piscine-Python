#!/bin/sh
if [ ! -z $1 ] ; then 
	curl --silent -I $1 | grep -oE "[a-z]+:/+([0-9a-zA-Z_\./]|-)+"
fi