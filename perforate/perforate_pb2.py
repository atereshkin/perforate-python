# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: perforate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='perforate.proto',
  package='perforate',
  serialized_pb=_b('\n\x0fperforate.proto\x12\tperforate\"U\n\nEventClass\x12\r\n\x05label\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x14\n\x0cis_prolonged\x18\x03 \x02(\x08\x12\x14\n\x0csession_code\x18\x04 \x01(\r\";\n\x06Metric\x12\r\n\x05label\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x14\n\x0csession_code\x18\x04 \x01(\r\"D\n\x05\x45vent\x12\x1a\n\x12\x63lass_session_code\x18\x01 \x02(\r\x12\r\n\x05value\x18\x02 \x01(\t\x12\x10\n\x08\x64uration\x18\x03 \x01(\x02\"9\n\x0bMeasurement\x12\x1b\n\x13metric_session_code\x18\x01 \x02(\r\x12\r\n\x05value\x18\x02 \x01(\x02\"\xb8\x01\n\x07Message\x12+\n\neventclass\x18\x01 \x01(\x0b\x32\x15.perforate.EventClassH\x00\x12#\n\x06metric\x18\x02 \x01(\x0b\x32\x11.perforate.MetricH\x00\x12!\n\x05\x65vent\x18\x03 \x01(\x0b\x32\x10.perforate.EventH\x00\x12-\n\x0bmeasurement\x18\x04 \x01(\x0b\x32\x16.perforate.MeasurementH\x00\x42\t\n\x07\x63ontent')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EVENTCLASS = _descriptor.Descriptor(
  name='EventClass',
  full_name='perforate.EventClass',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='perforate.EventClass.label', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='perforate.EventClass.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_prolonged', full_name='perforate.EventClass.is_prolonged', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session_code', full_name='perforate.EventClass.session_code', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=115,
)


_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='perforate.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='perforate.Metric.label', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='perforate.Metric.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session_code', full_name='perforate.Metric.session_code', index=2,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=176,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='perforate.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_session_code', full_name='perforate.Event.class_session_code', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='perforate.Event.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='perforate.Event.duration', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=178,
  serialized_end=246,
)


_MEASUREMENT = _descriptor.Descriptor(
  name='Measurement',
  full_name='perforate.Measurement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric_session_code', full_name='perforate.Measurement.metric_session_code', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='perforate.Measurement.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=305,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='perforate.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='eventclass', full_name='perforate.Message.eventclass', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metric', full_name='perforate.Message.metric', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event', full_name='perforate.Message.event', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='measurement', full_name='perforate.Message.measurement', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='content', full_name='perforate.Message.content',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=308,
  serialized_end=492,
)

_MESSAGE.fields_by_name['eventclass'].message_type = _EVENTCLASS
_MESSAGE.fields_by_name['metric'].message_type = _METRIC
_MESSAGE.fields_by_name['event'].message_type = _EVENT
_MESSAGE.fields_by_name['measurement'].message_type = _MEASUREMENT
_MESSAGE.oneofs_by_name['content'].fields.append(
  _MESSAGE.fields_by_name['eventclass'])
_MESSAGE.fields_by_name['eventclass'].containing_oneof = _MESSAGE.oneofs_by_name['content']
_MESSAGE.oneofs_by_name['content'].fields.append(
  _MESSAGE.fields_by_name['metric'])
_MESSAGE.fields_by_name['metric'].containing_oneof = _MESSAGE.oneofs_by_name['content']
_MESSAGE.oneofs_by_name['content'].fields.append(
  _MESSAGE.fields_by_name['event'])
_MESSAGE.fields_by_name['event'].containing_oneof = _MESSAGE.oneofs_by_name['content']
_MESSAGE.oneofs_by_name['content'].fields.append(
  _MESSAGE.fields_by_name['measurement'])
_MESSAGE.fields_by_name['measurement'].containing_oneof = _MESSAGE.oneofs_by_name['content']
DESCRIPTOR.message_types_by_name['EventClass'] = _EVENTCLASS
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['Measurement'] = _MEASUREMENT
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE

EventClass = _reflection.GeneratedProtocolMessageType('EventClass', (_message.Message,), dict(
  DESCRIPTOR = _EVENTCLASS,
  __module__ = 'perforate_pb2'
  # @@protoc_insertion_point(class_scope:perforate.EventClass)
  ))
_sym_db.RegisterMessage(EventClass)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), dict(
  DESCRIPTOR = _METRIC,
  __module__ = 'perforate_pb2'
  # @@protoc_insertion_point(class_scope:perforate.Metric)
  ))
_sym_db.RegisterMessage(Metric)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'perforate_pb2'
  # @@protoc_insertion_point(class_scope:perforate.Event)
  ))
_sym_db.RegisterMessage(Event)

Measurement = _reflection.GeneratedProtocolMessageType('Measurement', (_message.Message,), dict(
  DESCRIPTOR = _MEASUREMENT,
  __module__ = 'perforate_pb2'
  # @@protoc_insertion_point(class_scope:perforate.Measurement)
  ))
_sym_db.RegisterMessage(Measurement)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'perforate_pb2'
  # @@protoc_insertion_point(class_scope:perforate.Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
