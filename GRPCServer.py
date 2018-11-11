import os
import time
from concurrent import futures
import grpc
from sqlalchemy import *
from dotenv import load_dotenv
from pathlib import Path

import demo_pb2
import demo_pb2_grpc
from ModelRepository import ModelRepository

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class ModelService(demo_pb2_grpc.DemoServicer):

    def GetModelWithId(self, request: demo_pb2.ModelId, context):
        repository = ModelRepository(
            create_engine("postgresql://%s:%s@%s:%s/%s" % (
                    os.getenv('POSTGRES_USERNAME'),
                    os.getenv('POSTGRES_PASSWORD'),
                    os.getenv('POSTGRES_HOST'),
                    os.getenv('POSTGRES_PORT'),
                    os.getenv('POSTGRES_DATABASE')
                )
            )
        )

        response = demo_pb2.Model()
        model = repository.get_model_for_id(request.id)
        response.text_value = model.text_value
        response.select_value = model.select_value
        return response


if __name__ == '__main__':

    server_port = os.getenv('GRPC_SERVER_PORT')

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_DemoServicer_to_server(
        ModelService(),
        server
    )

    server.add_insecure_port("[::]:%s" % server_port)
    server.start()

    try:
        while True:
            print('Listening on port for requests %s...' % server_port)
            time.sleep(2000)
    except KeyboardInterrupt:
        server.stop(0)
