# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import projections_pb2 as projections__pb2
import shared_pb2 as shared__pb2


class ProjectionsStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/event_store.client.projections.Projections/Create',
                request_serializer=projections__pb2.CreateReq.SerializeToString,
                response_deserializer=projections__pb2.CreateResp.FromString,
                )
        self.Update = channel.unary_unary(
                '/event_store.client.projections.Projections/Update',
                request_serializer=projections__pb2.UpdateReq.SerializeToString,
                response_deserializer=projections__pb2.UpdateResp.FromString,
                )
        self.Delete = channel.unary_unary(
                '/event_store.client.projections.Projections/Delete',
                request_serializer=projections__pb2.DeleteReq.SerializeToString,
                response_deserializer=projections__pb2.DeleteResp.FromString,
                )
        self.Statistics = channel.unary_stream(
                '/event_store.client.projections.Projections/Statistics',
                request_serializer=projections__pb2.StatisticsReq.SerializeToString,
                response_deserializer=projections__pb2.StatisticsResp.FromString,
                )
        self.Disable = channel.unary_unary(
                '/event_store.client.projections.Projections/Disable',
                request_serializer=projections__pb2.DisableReq.SerializeToString,
                response_deserializer=projections__pb2.DisableResp.FromString,
                )
        self.Enable = channel.unary_unary(
                '/event_store.client.projections.Projections/Enable',
                request_serializer=projections__pb2.EnableReq.SerializeToString,
                response_deserializer=projections__pb2.EnableResp.FromString,
                )
        self.Reset = channel.unary_unary(
                '/event_store.client.projections.Projections/Reset',
                request_serializer=projections__pb2.ResetReq.SerializeToString,
                response_deserializer=projections__pb2.ResetResp.FromString,
                )
        self.State = channel.unary_unary(
                '/event_store.client.projections.Projections/State',
                request_serializer=projections__pb2.StateReq.SerializeToString,
                response_deserializer=projections__pb2.StateResp.FromString,
                )
        self.Result = channel.unary_unary(
                '/event_store.client.projections.Projections/Result',
                request_serializer=projections__pb2.ResultReq.SerializeToString,
                response_deserializer=projections__pb2.ResultResp.FromString,
                )
        self.RestartSubsystem = channel.unary_unary(
                '/event_store.client.projections.Projections/RestartSubsystem',
                request_serializer=shared__pb2.Empty.SerializeToString,
                response_deserializer=shared__pb2.Empty.FromString,
                )


class ProjectionsServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Statistics(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disable(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Enable(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reset(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def State(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Result(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RestartSubsystem(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=projections__pb2.CreateReq.FromString,
                    response_serializer=projections__pb2.CreateResp.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=projections__pb2.UpdateReq.FromString,
                    response_serializer=projections__pb2.UpdateResp.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=projections__pb2.DeleteReq.FromString,
                    response_serializer=projections__pb2.DeleteResp.SerializeToString,
            ),
            'Statistics': grpc.unary_stream_rpc_method_handler(
                    servicer.Statistics,
                    request_deserializer=projections__pb2.StatisticsReq.FromString,
                    response_serializer=projections__pb2.StatisticsResp.SerializeToString,
            ),
            'Disable': grpc.unary_unary_rpc_method_handler(
                    servicer.Disable,
                    request_deserializer=projections__pb2.DisableReq.FromString,
                    response_serializer=projections__pb2.DisableResp.SerializeToString,
            ),
            'Enable': grpc.unary_unary_rpc_method_handler(
                    servicer.Enable,
                    request_deserializer=projections__pb2.EnableReq.FromString,
                    response_serializer=projections__pb2.EnableResp.SerializeToString,
            ),
            'Reset': grpc.unary_unary_rpc_method_handler(
                    servicer.Reset,
                    request_deserializer=projections__pb2.ResetReq.FromString,
                    response_serializer=projections__pb2.ResetResp.SerializeToString,
            ),
            'State': grpc.unary_unary_rpc_method_handler(
                    servicer.State,
                    request_deserializer=projections__pb2.StateReq.FromString,
                    response_serializer=projections__pb2.StateResp.SerializeToString,
            ),
            'Result': grpc.unary_unary_rpc_method_handler(
                    servicer.Result,
                    request_deserializer=projections__pb2.ResultReq.FromString,
                    response_serializer=projections__pb2.ResultResp.SerializeToString,
            ),
            'RestartSubsystem': grpc.unary_unary_rpc_method_handler(
                    servicer.RestartSubsystem,
                    request_deserializer=shared__pb2.Empty.FromString,
                    response_serializer=shared__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'event_store.client.projections.Projections', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Projections(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.projections.Projections/Create',
            projections__pb2.CreateReq.SerializeToString,
            projections__pb2.CreateResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.projections.Projections/Update',
            projections__pb2.UpdateReq.SerializeToString,
            projections__pb2.UpdateResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.projections.Projections/Delete',
            projections__pb2.DeleteReq.SerializeToString,
            projections__pb2.DeleteResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Statistics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/event_store.client.projections.Projections/Statistics',
            projections__pb2.StatisticsReq.SerializeToString,
            projections__pb2.StatisticsResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.projections.Projections/Disable',
            projections__pb2.DisableReq.SerializeToString,
            projections__pb2.DisableResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Enable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.projections.Projections/Enable',
            projections__pb2.EnableReq.SerializeToString,
            projections__pb2.EnableResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Reset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.projections.Projections/Reset',
            projections__pb2.ResetReq.SerializeToString,
            projections__pb2.ResetResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def State(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.projections.Projections/State',
            projections__pb2.StateReq.SerializeToString,
            projections__pb2.StateResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Result(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.projections.Projections/Result',
            projections__pb2.ResultReq.SerializeToString,
            projections__pb2.ResultResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RestartSubsystem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.projections.Projections/RestartSubsystem',
            shared__pb2.Empty.SerializeToString,
            shared__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
