# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2014-2020)
#
# This file is part of pyDischarge.
#
# pyDischarge is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyDischarge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyDischarge.  If not, see <http://www.gnu.org/licenses/>.

"""Input/Output routines for Channel and ChannelList
"""

from . import (  # pylint: disable=unused-import
    cis,  # querying Channel Information System (cis.ligo.org)
    clf,  # LIGO Channel List File (clf) format
    omega,  # Omega pipeline scan configurations
)

__author__ = "Duncan Macleod <duncan.macleod@ligo.org>"