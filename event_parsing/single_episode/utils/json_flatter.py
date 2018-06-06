# Copyright 2018 Deep Air. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Parser to generate flat json file"""

import json
import os
from os.path import basename


def _mangle(s):
    return s.strip()[1:-1]


def _keyNameFix(dictionary, filename):
    '''
        Rename all the first level keys in the dictionary to
        filename_dictionary.
        inputs:
            dictionary: a python dict()
            filename: basepath of a file (string)
    '''
    changed = []
    for key in dictionary.keys():
        if (key not in changed) and (filename not in key):
            # 'os.path.splitext(filename)[0]' will remove extension from name
            new_key = os.path.splitext(filename)[0] + '_' + key
            changed.append(new_key)
            dictionary[new_key] = dictionary.pop(key)


def _generateTempFile(infile):
    '''
        Generate a temporary file with fixed dictionary keys.
        inputs:
            infile: file name (string)
    '''
    with open(infile) as f:
        data = json.load(f)

    _keyNameFix(data, basename(infile))
    with open('temp', 'w') as f:
        json.dump(data, f, indent=2)


def flat_json(output_filename, input_filenames):
    '''
        Generates one file from multiple json files :
            output_filename: file name for output file (string)
            input_filenames: list of names to merge (list)
    '''
    with open(output_filename, "w") as outfile:
        first = True
        for infile_name in input_filenames:
            _generateTempFile(infile_name)
            with open('temp') as infile:
                if first:
                    outfile.write('{')
                    first = False
                else:
                    outfile.write(',')
                outfile.write(_mangle(infile.read()))
            os.remove('temp')
        outfile.write('}')
