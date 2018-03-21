# Copyright 2018 Rackspace
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import os
import sys
import unittest

from contextlib import contextmanager
from six import StringIO

from cafe.drivers.base import print_exception


@contextmanager
def capture_stderr(command, *args, **kwargs):
    out, sys.stderr = sys.stderr, StringIO()
    command(*args, **kwargs)
    sys.stderr.seek(0)
    yield sys.stderr.read()
    sys.stderr = out


class PrintExceptionsTests(unittest.TestCase):

    def test_print_with_file_and_method(self):
        with capture_stderr(print_exception, file_='File1',
                            method='method1') as output:
            self.assertIn('File1: method1', output)

    def test_print_with_file_and_method_and_value(self):
        with capture_stderr(print_exception, file_='File1',
                            method='method1', value='value1') as output:
            self.assertIn('File1: method1: value1', output)

    def test_print_with_file_and_method_and_value_and_exception(self):
        with capture_stderr(print_exception, file_='File1', method='method1',
                            value='value1', exception=TypeError()) as output:
            self.assertIn('File1: method1: value1: TypeError', output)
