import sys
import websocket #pip install websocket-client
import threading
import time
import json
import requests
import traceback
import time
from .constants import socket_message_schemas as sms #Switching to Schema System from message system

class SocketPipe(object): # TODO: Subclass WebSocket type from websocket-client

    def __init__(self, _ws_endpoint, _bind, _callback = None):
        self.ws_endpoint = _ws_endpoint
        self.callback = _callback
        self.thread = None
        self.bind = _bind

    @staticmethod
    def on_message(ws, message):
        if self.callback:
            self.callback(message)

    @staticmethod
    def on_error(ws, error):
        # optional_logger(error)
        return

    @staticmethod
    def on_close(ws):
        # optional_logger(ws)
        return

    @staticmethod
    def on_open(ws):
        print("### SOCKET OPEN ###")

    def setThread(self,_thread):
        self.thread = _thread

    def closeThread(self):
        self.thread.close()

    def sendMessage(self,ws, _frame):
        print("Setting Framd: %s" % _frame)
        try:
            ws.send(_frame)
        except:
            return

    def connect(self):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(self.ws_endpoint,
                              on_message = self.callback,
                              on_error = self.on_error,
                              on_close = self.on_close)

        self.bind(ws)
        ws.on_open = self.on_open
        ws.run_forever()



class Subscriber(object):

    def __init__(self, _socket_endpoint):
        self.ws_endpoint = _socket_endpoint
        self.websock = None
        self.pipe = None


    def __bindSocket(self, _ws):
        self.websock = _ws


    def __updatePipe(self, _message):
        """
        JSON Serializes python dictionary and sends message to Pipe
        """

        self.pipe.sendMessage(self.websock, json.dumps(_message))


    def openSocket(self, _callback, _is_daemon = False):
        """
        Opens Socket connection to server and bind callback and socket controllers.
        Requires callback for processing and handling messages.
        DO NOT Call, utilize the connectSocket method in the AMPClient
        """
        self.pipe = SocketPipe(self.ws_endpoint, self.__bindSocket, _callback) # Callback handles messages for the user
        t = threading.Thread(target = self.pipe.connect)
        t.daemon = _is_daemon
        t.start()
        time.sleep(3) # Delay for connection to complete #TODO: Read off of pipe to synchronize behavior


    def closeSocket(self):
        if self.websock: self.websock.close()


    def sendRawMessageToSock(self, _message):
        self.__updatePipe(_message)


    def subscribeTrades(self, _base_token_addr, _quote_token_addr, _base_token_symbol, _quote_token_symbol):
        msg = sms.subscribeTrades(_base_token_addr, _quote_token_addr, _base_token_symbol, _quote_token_symbol)
        self.__updatePipe(json.dumps(msg))



    def unsubscribeTrades(self):
        msg = sms.unsubscribeTrades()
        self.__updatePipe(msg)


    def subscribeOrderBookMessage(self, _base_token_addr, _quote_token_addr, _base_token_symbol, _quote_token_symbol):
        sms.subscribeOrderBookMessage(_base_token_addr, _quote_token_addr, _base_token_symbol, _quote_token_symbol)
        self.__updatePipe(msg)


    def unsubscribeOrderBookMessage(self):
        msg = sms.unsubscribeOrderBookMessage()
        self.__updatePipe(msg)


    def subscribeCandlestickMessage(self, _to, _from, _duration, _units, _base_token_address, _quote_token_address, _base_token_symbol, _quote_token_symbol):
        msg = sms.subscribeCandlestickMessage(_to, _from, _duration, _units, _base_token_address, _quote_token_address, _base_token_symbol, _quote_token_symbol)
        self.__updatePipe(msg)


    def unsubscribeCandlestickMessage(self):
        msg = sms.unsubscribeCandlestickMessage()
        self.__updatePipe(msg)


    def newOrder(self, _orderhash, _order):
        msg = sms.newOrder(_orderhash, _order)
        self.__updatePipe(msg)

    def cancelOrder(self, _hash, _order_hash, _signature):
        msg = sms.cancelOrder(_hash, _order_hash, _signature)
        self.__updatePipe(msg)

    def submitSignature(self, _order_hash, _order, _remaining_order, _matches_array):
        msg = sms.submitSignature(_order_hash, _order, _remaining_order, _matches_array)
        self.__updatePipe(msg)
