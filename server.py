"""MiniGRPC server"""

from concurrent import futures
import time
import grpc
import minigrpc_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Maxims(minigrpc_pb2.MaximsServicer):
    def GetMaxim(self, request, context):
        combat_maxim = 'Always mind your surroundings.'
        security_maxim = 'Avoid scanf.'
        food_maxim = 'He was a bold man who first swallowed an oyster.'
        if request.maxim_type == minigrpc_pb2.GetMaximRequest.COMBAT:
            result = combat_maxim
        elif request.maxim_type == minigrpc_pb2.GetMaximRequest.SECURITY:
            result = security_maxim
        elif request.maxim_type == minigrpc_pb2.GetMaximRequest.FOOD:
            result = food_maxim
        elif request.maxim_type != minigrpc_pb2.GetMaximRequest.TYPE_NOT_SPECIFIED:
            # can't go wrong with a Batman quote
            result = combat_maxim
        return minigrpc_pb2.GetMaximResponse(maxim=result)


def serve():
      server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
      minigrpc_pb2.add_MaximsServicer_to_server(Maxims(), server)
      server.add_insecure_port('[::]:50051')
      server.start()
      try:
            while True:
                  time.sleep(_ONE_DAY_IN_SECONDS)
      except KeyboardInterrupt:
            server.stop(0)

if __name__ == '__main__':
    serve()
