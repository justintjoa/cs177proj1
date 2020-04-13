# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: configure.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='configure.proto',
  package='proj1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0f\x63onfigure.proto\x12\x05proj1\"\x12\n\x02m0\x12\x0c\n\x04type\x18\x01 \x01(\r\".\n\x02m1\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\t\"!\n\x02m2\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\r\n\x05\x63ount\x18\x02 \x01(\r\" \n\x02m3\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0c\n\x04\x66lag\x18\x02 \x01(\tb\x06proto3'
)




_M0 = _descriptor.Descriptor(
  name='m0',
  full_name='proj1.m0',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='proj1.m0.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=26,
  serialized_end=44,
)


_M1 = _descriptor.Descriptor(
  name='m1',
  full_name='proj1.m1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='proj1.m1.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='proj1.m1.key', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proj1.m1.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=46,
  serialized_end=92,
)


_M2 = _descriptor.Descriptor(
  name='m2',
  full_name='proj1.m2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='proj1.m2.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='proj1.m2.count', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=94,
  serialized_end=127,
)


_M3 = _descriptor.Descriptor(
  name='m3',
  full_name='proj1.m3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='proj1.m3.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flag', full_name='proj1.m3.flag', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=129,
  serialized_end=161,
)

DESCRIPTOR.message_types_by_name['m0'] = _M0
DESCRIPTOR.message_types_by_name['m1'] = _M1
DESCRIPTOR.message_types_by_name['m2'] = _M2
DESCRIPTOR.message_types_by_name['m3'] = _M3
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

m0 = _reflection.GeneratedProtocolMessageType('m0', (_message.Message,), {
  'DESCRIPTOR' : _M0,
  '__module__' : 'configure_pb2'
  # @@protoc_insertion_point(class_scope:proj1.m0)
  })
_sym_db.RegisterMessage(m0)

m1 = _reflection.GeneratedProtocolMessageType('m1', (_message.Message,), {
  'DESCRIPTOR' : _M1,
  '__module__' : 'configure_pb2'
  # @@protoc_insertion_point(class_scope:proj1.m1)
  })
_sym_db.RegisterMessage(m1)

m2 = _reflection.GeneratedProtocolMessageType('m2', (_message.Message,), {
  'DESCRIPTOR' : _M2,
  '__module__' : 'configure_pb2'
  # @@protoc_insertion_point(class_scope:proj1.m2)
  })
_sym_db.RegisterMessage(m2)

m3 = _reflection.GeneratedProtocolMessageType('m3', (_message.Message,), {
  'DESCRIPTOR' : _M3,
  '__module__' : 'configure_pb2'
  # @@protoc_insertion_point(class_scope:proj1.m3)
  })
_sym_db.RegisterMessage(m3)


# @@protoc_insertion_point(module_scope)
