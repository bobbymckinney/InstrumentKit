#!/usr/bin/python
# -*- coding: utf-8 -*-
##
# _moves.py: Py2/3 moves not fully captured by six.
##
# © 2013 Steven Casagrande (scasagrande@galvant.ca).
#
# This file is a part of the InstrumentKit project.
# Licensed under the AGPL version 3.
##
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
##

## IMPORTS ####################################################################

import six
import flufl.enum

## PY2/3 COMPAT ################################################################

if six.PY2:
    IntEnum = flufl.enum.IntEnum
elif six.PY3:
	# Define a subclass of Enum that does nothing but marks as being different,
	# so that we can test in enum_property.
	class IntEnum(flufl.enum.Enum):
		pass
else:
    assert False, "this should never happen."
