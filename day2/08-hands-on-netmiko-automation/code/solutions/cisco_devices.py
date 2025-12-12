"""
cisco_devices.py
================

This module contains device configurations for all network devices in the topology.
It includes device details such as device type, host address, and credentials.

The device credentials are loaded from environment variables to ensure sensitive information
is not hardcoded in the script.
"""

import os

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

devices = [
    {
        "name": "R1",
        "device_type": "cisco_ios",
        "host": "10.1.1.201",
        "username": USERNAME,
        "password": PASSWORD,
    },
    {
        "name": "R2",
        "device_type": "cisco_ios",
        "host": "10.1.1.202",
        "username": USERNAME,
        "password": PASSWORD,
    },
    {
        "name": "R3",
        "device_type": "cisco_ios",
        "host": "10.1.1.203",
        "username": USERNAME,
        "password": PASSWORD,
    }
]