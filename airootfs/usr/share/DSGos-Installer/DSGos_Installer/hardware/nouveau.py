#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nouveau.py
#
#  Copyright © 2013-2015 DSGos
#
#  This file is part of DSGos_Installer.
#
#  DSGos_Installer is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  DSGos_Installer is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  The following additional terms are in effect as per Section 7 of the license:
#
#  The preservation of all legal notices and author attributions in
#  the material or in the Appropriate Legal Notices displayed
#  by works containing it is required.
#
#  You should have received a copy of the GNU General Public License
#  along with DSGos_Installer; If not, see <http://www.gnu.org/licenses/>.


""" Nouveau (Nvidia) driver installation """

try:
    from hardware.hardware import Hardware
except ImportError:
    from hardware import Hardware

import os

CLASS_NAME = "Nouveau"
CLASS_ID = "0x03"
VENDOR_ID = "0x10de"
DEVICES = []

# Give this driver more priority so it is chosen instead of
# nvidia or nvidia-340xx or nvidia-304xx
PRIORITY = 3


class Nouveau(Hardware):
    def __init__(self):
        Hardware.__init__(self, CLASS_NAME, CLASS_ID, VENDOR_ID, DEVICES, PRIORITY)

    @staticmethod
    def get_packages():
        pkgs = ["xf86-video-nouveau"]
        if os.uname()[-1] == "x86_64":
            pkgs.extend(["lib32-mesa", "lib32-mesa-libgl"])
        return pkgs

    @staticmethod
    def post_install(dest_dir):
        path = os.path.join(dest_dir, "etc/modprobe.d/nouveau.conf")
        with open(path, 'w') as modprobe:
            modprobe.write("options nouveau modeset=1\n")

        # path = os.path.join(dest_dir, "etc/modprobe.d/blacklist-nvidia.conf")
        # with open(path, "w") as blacklist:
        #    blacklist.write("blacklist nvidia\n")
