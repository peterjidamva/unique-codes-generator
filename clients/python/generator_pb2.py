# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generator.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fgenerator.proto\x12\tgenerator\"\x14\n\x04\x43ode\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\"\x16\n\x05\x43odes\x12\r\n\x05\x63odes\x18\x01 \x03(\t\"\x1b\n\x19GenerateUniqueCodeRequest\"+\n\x1aGenerateUniqueCodesRequest\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x32\xac\x01\n\tGenerator\x12M\n\x12GenerateUniqueCode\x12$.generator.GenerateUniqueCodeRequest\x1a\x0f.generator.Code\"\x00\x12P\n\x13GenerateUniqueCodes\x12%.generator.GenerateUniqueCodesRequest\x1a\x10.generator.Codes\"\x00\x42\rZ\x0b./generatorb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'generator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\013./generator'
  _globals['_CODE']._serialized_start=30
  _globals['_CODE']._serialized_end=50
  _globals['_CODES']._serialized_start=52
  _globals['_CODES']._serialized_end=74
  _globals['_GENERATEUNIQUECODEREQUEST']._serialized_start=76
  _globals['_GENERATEUNIQUECODEREQUEST']._serialized_end=103
  _globals['_GENERATEUNIQUECODESREQUEST']._serialized_start=105
  _globals['_GENERATEUNIQUECODESREQUEST']._serialized_end=148
  _globals['_GENERATOR']._serialized_start=151
  _globals['_GENERATOR']._serialized_end=323
# @@protoc_insertion_point(module_scope)
