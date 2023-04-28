#!/bin/bash

[ ! -d "./anonym8" ] && exec git clone https://github.com/HiroshiManRise/anonym8

cd anonym8

chmod +x INSTALL.sh

sudo bash INSTALL.sh
