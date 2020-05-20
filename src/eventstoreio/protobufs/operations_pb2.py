# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: operations.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import shared_pb2 as shared__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='operations.proto',
  package='event_store.client.operations',
  syntax='proto3',
  serialized_options=b'\n com.eventstore.client.operations',
  serialized_pb=b'\n\x10operations.proto\x12\x1d\x65vent_store.client.operations\x1a\x0cshared.proto\"\x97\x01\n\x10StartScavengeReq\x12H\n\x07options\x18\x01 \x01(\x0b\x32\x37.event_store.client.operations.StartScavengeReq.Options\x1a\x39\n\x07Options\x12\x14\n\x0cthread_count\x18\x01 \x01(\x05\x12\x18\n\x10start_from_chunk\x18\x02 \x01(\x05\"z\n\x0fStopScavengeReq\x12G\n\x07options\x18\x01 \x01(\x0b\x32\x36.event_store.client.operations.StopScavengeReq.Options\x1a\x1e\n\x07Options\x12\x13\n\x0bscavenge_id\x18\x01 \x01(\t\"\xb4\x01\n\x0cScavengeResp\x12\x13\n\x0bscavenge_id\x18\x01 \x01(\t\x12S\n\x0fscavenge_result\x18\x02 \x01(\x0e\x32:.event_store.client.operations.ScavengeResp.ScavengeResult\":\n\x0eScavengeResult\x12\x0b\n\x07Started\x10\x00\x12\x0e\n\nInProgress\x10\x01\x12\x0b\n\x07Stopped\x10\x02\"&\n\x12SetNodePriorityReq\x12\x10\n\x08priority\x18\x01 \x01(\x05\x32\xc6\x04\n\nOperations\x12m\n\rStartScavenge\x12/.event_store.client.operations.StartScavengeReq\x1a+.event_store.client.operations.ScavengeResp\x12k\n\x0cStopScavenge\x12..event_store.client.operations.StopScavengeReq\x1a+.event_store.client.operations.ScavengeResp\x12N\n\x08Shutdown\x12 .event_store.client.shared.Empty\x1a .event_store.client.shared.Empty\x12R\n\x0cMergeIndexes\x12 .event_store.client.shared.Empty\x1a .event_store.client.shared.Empty\x12P\n\nResignNode\x12 .event_store.client.shared.Empty\x1a .event_store.client.shared.Empty\x12\x66\n\x0fSetNodePriority\x12\x31.event_store.client.operations.SetNodePriorityReq\x1a .event_store.client.shared.EmptyB\"\n com.eventstore.client.operationsb\x06proto3'
  ,
  dependencies=[shared__pb2.DESCRIPTOR,])



_SCAVENGERESP_SCAVENGERESULT = _descriptor.EnumDescriptor(
  name='ScavengeResult',
  full_name='event_store.client.operations.ScavengeResp.ScavengeResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Started', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InProgress', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Stopped', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=466,
  serialized_end=524,
)
_sym_db.RegisterEnumDescriptor(_SCAVENGERESP_SCAVENGERESULT)


_STARTSCAVENGEREQ_OPTIONS = _descriptor.Descriptor(
  name='Options',
  full_name='event_store.client.operations.StartScavengeReq.Options',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='thread_count', full_name='event_store.client.operations.StartScavengeReq.Options.thread_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_from_chunk', full_name='event_store.client.operations.StartScavengeReq.Options.start_from_chunk', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=217,
)

_STARTSCAVENGEREQ = _descriptor.Descriptor(
  name='StartScavengeReq',
  full_name='event_store.client.operations.StartScavengeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='options', full_name='event_store.client.operations.StartScavengeReq.options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STARTSCAVENGEREQ_OPTIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=217,
)


_STOPSCAVENGEREQ_OPTIONS = _descriptor.Descriptor(
  name='Options',
  full_name='event_store.client.operations.StopScavengeReq.Options',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scavenge_id', full_name='event_store.client.operations.StopScavengeReq.Options.scavenge_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=311,
  serialized_end=341,
)

_STOPSCAVENGEREQ = _descriptor.Descriptor(
  name='StopScavengeReq',
  full_name='event_store.client.operations.StopScavengeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='options', full_name='event_store.client.operations.StopScavengeReq.options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STOPSCAVENGEREQ_OPTIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=341,
)


_SCAVENGERESP = _descriptor.Descriptor(
  name='ScavengeResp',
  full_name='event_store.client.operations.ScavengeResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scavenge_id', full_name='event_store.client.operations.ScavengeResp.scavenge_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scavenge_result', full_name='event_store.client.operations.ScavengeResp.scavenge_result', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCAVENGERESP_SCAVENGERESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=524,
)


_SETNODEPRIORITYREQ = _descriptor.Descriptor(
  name='SetNodePriorityReq',
  full_name='event_store.client.operations.SetNodePriorityReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='priority', full_name='event_store.client.operations.SetNodePriorityReq.priority', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=526,
  serialized_end=564,
)

_STARTSCAVENGEREQ_OPTIONS.containing_type = _STARTSCAVENGEREQ
_STARTSCAVENGEREQ.fields_by_name['options'].message_type = _STARTSCAVENGEREQ_OPTIONS
_STOPSCAVENGEREQ_OPTIONS.containing_type = _STOPSCAVENGEREQ
_STOPSCAVENGEREQ.fields_by_name['options'].message_type = _STOPSCAVENGEREQ_OPTIONS
_SCAVENGERESP.fields_by_name['scavenge_result'].enum_type = _SCAVENGERESP_SCAVENGERESULT
_SCAVENGERESP_SCAVENGERESULT.containing_type = _SCAVENGERESP
DESCRIPTOR.message_types_by_name['StartScavengeReq'] = _STARTSCAVENGEREQ
DESCRIPTOR.message_types_by_name['StopScavengeReq'] = _STOPSCAVENGEREQ
DESCRIPTOR.message_types_by_name['ScavengeResp'] = _SCAVENGERESP
DESCRIPTOR.message_types_by_name['SetNodePriorityReq'] = _SETNODEPRIORITYREQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartScavengeReq = _reflection.GeneratedProtocolMessageType('StartScavengeReq', (_message.Message,), {

  'Options' : _reflection.GeneratedProtocolMessageType('Options', (_message.Message,), {
    'DESCRIPTOR' : _STARTSCAVENGEREQ_OPTIONS,
    '__module__' : 'operations_pb2'
    # @@protoc_insertion_point(class_scope:event_store.client.operations.StartScavengeReq.Options)
    })
  ,
  'DESCRIPTOR' : _STARTSCAVENGEREQ,
  '__module__' : 'operations_pb2'
  # @@protoc_insertion_point(class_scope:event_store.client.operations.StartScavengeReq)
  })
_sym_db.RegisterMessage(StartScavengeReq)
_sym_db.RegisterMessage(StartScavengeReq.Options)

StopScavengeReq = _reflection.GeneratedProtocolMessageType('StopScavengeReq', (_message.Message,), {

  'Options' : _reflection.GeneratedProtocolMessageType('Options', (_message.Message,), {
    'DESCRIPTOR' : _STOPSCAVENGEREQ_OPTIONS,
    '__module__' : 'operations_pb2'
    # @@protoc_insertion_point(class_scope:event_store.client.operations.StopScavengeReq.Options)
    })
  ,
  'DESCRIPTOR' : _STOPSCAVENGEREQ,
  '__module__' : 'operations_pb2'
  # @@protoc_insertion_point(class_scope:event_store.client.operations.StopScavengeReq)
  })
_sym_db.RegisterMessage(StopScavengeReq)
_sym_db.RegisterMessage(StopScavengeReq.Options)

ScavengeResp = _reflection.GeneratedProtocolMessageType('ScavengeResp', (_message.Message,), {
  'DESCRIPTOR' : _SCAVENGERESP,
  '__module__' : 'operations_pb2'
  # @@protoc_insertion_point(class_scope:event_store.client.operations.ScavengeResp)
  })
_sym_db.RegisterMessage(ScavengeResp)

SetNodePriorityReq = _reflection.GeneratedProtocolMessageType('SetNodePriorityReq', (_message.Message,), {
  'DESCRIPTOR' : _SETNODEPRIORITYREQ,
  '__module__' : 'operations_pb2'
  # @@protoc_insertion_point(class_scope:event_store.client.operations.SetNodePriorityReq)
  })
_sym_db.RegisterMessage(SetNodePriorityReq)


DESCRIPTOR._options = None

_OPERATIONS = _descriptor.ServiceDescriptor(
  name='Operations',
  full_name='event_store.client.operations.Operations',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=567,
  serialized_end=1149,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartScavenge',
    full_name='event_store.client.operations.Operations.StartScavenge',
    index=0,
    containing_service=None,
    input_type=_STARTSCAVENGEREQ,
    output_type=_SCAVENGERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopScavenge',
    full_name='event_store.client.operations.Operations.StopScavenge',
    index=1,
    containing_service=None,
    input_type=_STOPSCAVENGEREQ,
    output_type=_SCAVENGERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Shutdown',
    full_name='event_store.client.operations.Operations.Shutdown',
    index=2,
    containing_service=None,
    input_type=shared__pb2._EMPTY,
    output_type=shared__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MergeIndexes',
    full_name='event_store.client.operations.Operations.MergeIndexes',
    index=3,
    containing_service=None,
    input_type=shared__pb2._EMPTY,
    output_type=shared__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ResignNode',
    full_name='event_store.client.operations.Operations.ResignNode',
    index=4,
    containing_service=None,
    input_type=shared__pb2._EMPTY,
    output_type=shared__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetNodePriority',
    full_name='event_store.client.operations.Operations.SetNodePriority',
    index=5,
    containing_service=None,
    input_type=_SETNODEPRIORITYREQ,
    output_type=shared__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_OPERATIONS)

DESCRIPTOR.services_by_name['Operations'] = _OPERATIONS

# @@protoc_insertion_point(module_scope)
