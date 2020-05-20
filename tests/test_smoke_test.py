from eventstoreio.protobufs.streams_pb2_grpc import StreamsStub
channel = grpc.insecure_channel('localhost:92113')
stub = StreamsStub(channel)
