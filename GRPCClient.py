import os
import sys
import grpc
from dotenv import load_dotenv
from pathlib import Path

import demo_pb2
import demo_pb2_grpc

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

server_port = os.getenv('GRPC_SERVER_PORT')

if len(sys.argv) <= 1:
    print("""
    Invalid call made to gRPC Client.
    -----------------------------------------------------
    python3 GRPCClient.py <model_id>
    """)
    exit(1)

print("Subscribing to channel %s..." % server_port)
channel = grpc.insecure_channel('localhost:%s' % server_port)

demoStub = demo_pb2_grpc.DemoStub(channel)
print("Retrieving model: %s" % server_port)
modelIdMessage = demo_pb2.ModelId(id=int(sys.argv[1]))

print("Messaging server to obtain id for model: %s" % sys.argv[1])
response = demoStub.GetModelWithId(modelIdMessage)

print("Model Text Value: %s" % response.text_value)
print("Model Select Value: %s" % response.select_value)
