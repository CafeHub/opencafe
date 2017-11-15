# Copyright 2015 Rackspace
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

import argparse
import os
import subprocess
from cafe.configurator.managers import TestEnvManager


def entry_point():

    # Set up arguments
    argparser = argparse.ArgumentParser(prog='behave-runner')

    argparser.add_argument(
        "product",
        nargs=1,
        metavar="<product>",
        help="Product name")

    argparser.add_argument(
        "config",
        nargs=1,
        metavar="<config_file>",
        help="Product test config")

    argparser.add_argument(
        dest='behave_opts',
        nargs=argparse.REMAINDER,
        metavar="<behave_opts>",
        help="Options to pass to Behave")

    args = argparser.parse_args()
    config = str(args.config[0])
    product = str(args.product[0])
    behave_opts = args.behave_opts

    test_env_manager = TestEnvManager(product, config)
    test_env_manager.finalize()

    print_mug(test_env_manager)
    behave_opts.insert(0, "behave")

    subprocess.call(behave_opts)

    exit(0)


def print_mug(test_env):
    mug0 = "      ( ("
    mug1 = "       ) )"
    mug2 = "    ........."
    mug3 = "    |       |___"
    mug4 = "    |       |_  |"
    mug5 = "    |  :-)  |_| |"
    mug6 = "    |       |___|"
    mug7 = "    |_______|"
    mug8 = "=== CAFE Behave Runner ==="

    print("\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}".format(
        mug0,
        mug1,
        mug2,
        mug3,
        mug4,
        mug5,
        mug6,
        mug7,
        mug8))

    config = "TEST CONFIG FILE..: {0}".format(test_env.test_config_file_path)
    data = "DATA DIRECTORY....: {0}".format(test_env.test_data_directory)
    log = "LOG PATH..........: {0}".format(test_env.test_log_dir)
    wrapper_len = max(len(s) for s in [config, data, log])

    print("-" * wrapper_len)
    print(config)
    print(data)
    print(log)
    print("-" * wrapper_len)


if __name__ == '__main__':
    entry_point()
