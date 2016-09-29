"""MiniGRPC client"""

from __future__ import print_function
import grpc
import minigrpc_pb2


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = minigrpc_pb2.MaximsStub(channel)
  response = stub.GetMaxim(minigrpc_pb2.GetMaximRequest(
                maxim_type=minigrpc_pb2.GetMaximRequest.FOOD))
  print("Client received: '%s'" % response.maxim)


if __name__ == '__main__':
  run()
