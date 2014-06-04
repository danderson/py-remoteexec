#!/usr/bin/env python
#
# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import socket
import sys

mods = {
    'test1': '\n'.join([
        'import test',
        'import test2',
        'def print_stuff():',
        '  print "Hello from test1"',
        '  print test2.hello',
        '  print test.mods',
        '  test.hostname()',
        ]),
    'test2': '\n'.join([
        'hello = "Hello from test2"',
        ]),
    }

def hostname():
    print socket.gethostname()

if __name__ == '__main__':
    import remoteexec
    p, s = remoteexec.remote_exec(
        hostname=sys.argv[1],
        module_filenames=['test.py', 'remoteexec.py'],
        literal_modules=mods,
        main_func='test1.print_stuff',
        verbose_load=True)
    f = s.makefile('r')
    s.close()
    print f.read()
