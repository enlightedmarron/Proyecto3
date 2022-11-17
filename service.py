from cyberdog_app_pb2_grpc import *
from cyberdog_app_pb2 import *
import grpc
import time

MAX_SPEED = 10

cyberdog_ip = 0

def RunOrderCMD():

    if (cyberdog_ip):
        cyberdog_ip = input('Cyberdog Ip: ')
    with grpc.insecure_channel(str(cyberdog_ip) + ':50051') as channel:
        print("Wait connect")
        try:
            grpc.channel_ready_future(channel).result(timeout=10)
        except grpc.FutureTimeoutError:
            print("Connect error, Timeout")
            return
    cyberdog__app__pb2.MonOrder(
        id = cyberdog__app__pb2.MonOrder.MONO_ORDER_STAND_UP,
        para = 0
    )
    time.sleep(5)
    cyberdog__app__pb2.MonOrder(
        id = cyberdog__app__pb2.MonOrder.MONO_ORDER_HI_FIVE,
        para = 0
    )
    time.sleep(5)
    cyberdog__app__pb2.MonOrder(
        id = cyberdog__app__pb2.MonOrder.MONO_ORDER_STAND_UP,
        para = 0
    )
    time.sleep(5)
    cyberdog__app__pb2.MonOrder(
        id = cyberdog__app__pb2.MonOrder.MONO_ORDER_DANCE,
        para = 0
    )
    time.sleep(5)
    cyberdog__app__pb2.MonOrder(
        id = cyberdog__app__pb2.MonOrder.MONO_ORDER_SIT,
        para = 0
    )
    time.sleep(5)


RunOrderCMD()