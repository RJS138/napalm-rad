# -*- coding: utf-8 -*-
# Copyright 2016 Dravetech AB. All rights reserved.
#
# The contents of this file are licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

"""
Napalm driver for rad.

Read https://napalm.readthedocs.io for more information.
"""

import os

from napalm.base import NetworkDriver
from napalm.base.exceptions import (
    CommandErrorException,
    ConnectionException,
    MergeConfigException,
    ReplaceConfigException,
    SessionLockedException,
)
from netmiko import (
    ConnectHandler,
    NetmikoAuthenticationException,
    NetmikoTimeoutException,
)


class radDriver(NetworkDriver):
    """Napalm driver for rad."""

    def __init__(self, hostname, username, password, timeout=60, optional_args=None):
        """Constructor."""
        self.device = None
        self.hostname = hostname
        self.username = username
        self.password = password
        self.timeout = timeout

        if optional_args is None:
            optional_args = {}

        self.fsm_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "napalm_rad\\templates")
        )

    def open(self):
        """Implement the NAPALM method open (mandatory)"""

        connection_args = {
            "device_type": "autodetect",
            "ip": self.hostname,
            "username": self.username,
            "password": self.password,
            "port": 22,
            "timeout": 20,
        }

        try:
            self.conn = ConnectHandler(**connection_args)

        except Exception:
            self.conn = None

    def close(self):
        """Implement the NAPALM method close (mandatory)"""
        self.conn.disconnect()
