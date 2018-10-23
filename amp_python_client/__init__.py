
import requests
import sys
import os
import json
from .amp_client import AmpClient


"""
!!! Requires Python >=3.5 !!!

This is a simple python client for the AMP Decentralized Exchange API.
It provides a simple interface utilizing Python types for accessing
various functions on the AMP API.  Given that the API itself is in
development, this client-lib will be changing rapidly and we do not
recommend utilizing it yet for production-level code.

Serialization occurs last minute in all returns.
"""
