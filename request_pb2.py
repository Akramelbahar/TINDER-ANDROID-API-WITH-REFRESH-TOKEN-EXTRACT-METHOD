# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: request.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'request.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rrequest.proto\"$\n\x0bRefreshAuth\x12\x15\n\rrefresh_token\x18\x01 \x01(\t\" \n\x0f\x41uthFlowVariant\x12\r\n\x05value\x18\x01 \x01(\t\"^\n\x0bMainRequest\x12\"\n\x0crefresh_auth\x18\n \x01(\x0b\x32\x0c.RefreshAuth\x12+\n\x11\x61uth_flow_variant\x18\x17 \x01(\x0b\x32\x10.AuthFlowVariantb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'request_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REFRESHAUTH']._serialized_start=17
  _globals['_REFRESHAUTH']._serialized_end=53
  _globals['_AUTHFLOWVARIANT']._serialized_start=55
  _globals['_AUTHFLOWVARIANT']._serialized_end=87
  _globals['_MAINREQUEST']._serialized_start=89
  _globals['_MAINREQUEST']._serialized_end=183
# @@protoc_insertion_point(module_scope)
