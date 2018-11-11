import time
from concurrent import futures
import grpc
from sqlalchemy import *

from gPRC import demo_pb2, demo_pb2_grpc
from ModelRepository import ModelRepository

username = 'postgres'
password = 'password'
host = 'postgres'
port = '5432'
database = 'test'


class ModelService(demo_pb2_grpc.DemoServicer):

    def __init__(self):
        self.repository = ModelRepository(
            create_engine("postgresql://%s:%s@%s:%s/%s" % (username, password, host, port, database))
        )

    def GetModelWithId(self, request: demo_pb2.ModelId, context):
        response = demo_pb2.Model
        model = self.repository.get_model_for_id(request.id)
        response.text_value = model.text_value
        response.select_value = model.select_value


server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
demo_pb2_grpc.add_DemoServicer_to_server(
    ModelService(),
    server
)

server.add_insecure_port('[::]: 50051')
server.start()

try:
    while True:
        time.sleep(2000)
except KeyboardInterrupt:
    server.stop(0)