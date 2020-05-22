#!/usr/bin/env python3

# MISITcms - https://github.com/frankkramer-lab/MISITcms/
# Copyright © 2020 Dominik Müller, Johann Frei
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""This script allow easy parsing the CMS config file in JSON format.
"""

import os
import sys
import json

# Parse the config file and obtain the value of a given key
def obtain_value(key, config_path=os.path.join("config", "cms.conf")):
    # Transform relative to absolute path
    config_path_abs = os.path.abspath(config_path)
    # Read JSON config file as dictionary
    with open(config_path_abs, "r", encoding="utf-8") as f:
        conf_data = json.load(f)
    # Return value for given key
    return conf_data[key]

# Provide an interface for direct script calling
if __name__ == '__main__':
    # IF script is called with one argument (key)
    if len(sys.argv) == 2:
        # Get value for given key from config file
        value = obtain_value(sys.argv[1])
        print(value)
    else:
        # Unknown parameter / Wrong call
        # Do nothing
        pass
