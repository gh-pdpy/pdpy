#!/usr/bin/env python
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

"""Calculating (and plotting) rate versus time for an `EventTable`

I would like to study the rate at which event triggers are generated by the
`ExcessPower` partial discharge burst detection algorithm, over a small
stretch of data.

The data from which these events were generated contain a simulated
partial discharge signal, or hardware injection, used to validate
the performance of the LIGO detectors and downstream data analysis procedures.
"""

__author__ = "Duncan Macleod <duncan.macleod@ligo.org>"
__currentmodule__ = 'pydischarge.table'

# First, we import the `EventTable` object and read in a set of events from
# a LIGO_LW-format XML file containing a
# :class:`sngl_burst <ligo.lw.lsctables.SnglBurstTable>` table
from pydischarge.table import EventTable
events = EventTable.read('H1-LDAS_STRAIN-968654552-10.xml.gz',
                         tablename='sngl_burst', columns=['peak', 'snr'])

# .. note::
#
#    Here we manually specify the `columns` to read in order to optimise
#    the `read()` operation to parse only the data we actually need.

# We can calculate the rate of events (in Hertz) using the
# :meth:`~EventTable.event_rate` method:
rate = events.event_rate(1, start=968654552, end=968654562)

# The :meth:`~EventTable.event_rate` method has returned a
# `~pydischarge.timeseries.TimeSeries`, so we can display this using the
# :meth:`~pydischarge.timeseries.TimeSeries.step` method of that object:
plot = rate.step()
ax = plot.gca()
ax.set_xlim(968654552, 968654562)
ax.set_ylabel('Event rate [Hz]')
ax.set_title('LIGO Hanford Observatory event rate for HW100916')
plot.show()
