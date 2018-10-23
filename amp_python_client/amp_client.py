#!/usr/bin/env python

import urllib
import requests
from .__rest import ampRestEndpoints
from .__socket import Subscriber
from .utils.BoundMethods import BoundInstanceMethods

class AmpClient(object):

    def __init__(self, _host = None, _port = None, _rest_protocol = "http", _ws_protocol = "ws"):
        """
        All calls return as Python Objects
        """
        self.host = str(_host) or str(HOST)
        self.port = str(_port) or str(PORT)

        self.rest_protocol = _rest_protocol + "://"
        self.rest_endpoint = self.rest_protocol + _host + ":" + self.port

        self.ws_protocol = _ws_protocol + "://"
        self.ws_endpoint = self.ws_protocol + _host + ":" + self.port + "/socket"

        self.rest_methods = ampRestEndpoints(self.rest_endpoint)
        self.ws_subscriber = None

        self.methods = BoundInstanceMethods(self.rest_methods)

    def createSocket(self, _callback):
        self.ws_subscriber = Subscriber(self.ws_endpoint)
        self.ws_subscriber.openSocket(_callback)
        self.methods.update(self.ws_subscriber)

    def __getattr__(self, _attr):
        return getattr(self.methods, _attr)
