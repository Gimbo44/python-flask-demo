import sys
import grpc
from dotenv import load_dotenv
from pathlib import Path

import demo_pb2
import demo_pb2_grpc

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

if (len(sys.argv) <= 1):
    print("""
    Invalid call made to gRPC Client.
    -----------------------------------------------------
    python3 GRPCClient.py <model_id>
    """)
    exit(1)

print("Subscribing to channel 50051...")
channel = grpc.insecure_channel('localhost:50051')

demoStub = demo_pb2_grpc.DemoStub(channel)
modelIdMessage = demo_pb2.ModelId(sys.argv[1])

print("Messaging server to obtain id for model: %s" % sys.argv[1])
response = demoStub.GetModelWithId(modelIdMessage)

print("Model Text Value: %s" % response.text_value)
print("Model Select Value: %s" % response.select_value)
