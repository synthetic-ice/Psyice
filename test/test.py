#!/usr/bin/env python

import psyice
import os


os.system("cp mirrorlist target")
psyice.modifyMirrorlist("./target")
