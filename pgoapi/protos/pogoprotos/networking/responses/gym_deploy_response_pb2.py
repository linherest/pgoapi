# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/gym_deploy_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.gym import gym_status_and_defenders_pb2 as pogoprotos_dot_data_dot_gym_dot_gym__status__and__defenders__pb2
from pogoprotos.data.badge import awarded_gym_badge_pb2 as pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/gym_deploy_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n9pogoprotos/networking/responses/gym_deploy_response.proto\x12\x1fpogoprotos.networking.responses\x1a\x32pogoprotos/data/gym/gym_status_and_defenders.proto\x1a-pogoprotos/data/badge/awarded_gym_badge.proto\"\xdd\x06\n\x11GymDeployResponse\x12I\n\x06result\x18\x01 \x01(\x0e\x32\x39.pogoprotos.networking.responses.GymDeployResponse.Result\x12L\n\x18gym_status_and_defenders\x18\x02 \x01(\x0b\x32*.pogoprotos.data.gym.GymStatusAndDefenders\x12\x41\n\x11\x61warded_gym_badge\x18\x03 \x01(\x0b\x32&.pogoprotos.data.badge.AwardedGymBadge\x12&\n\x1e\x63ooldown_complete_timestamp_ms\x18\x04 \x01(\x03\"\xc3\x04\n\x06Result\x12\x11\n\rNO_RESULT_SET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12%\n!ERROR_ALREADY_HAS_POKEMON_ON_FORT\x10\x02\x12!\n\x1d\x45RROR_OPPOSING_TEAM_OWNS_FORT\x10\x03\x12\x16\n\x12\x45RROR_FORT_IS_FULL\x10\x04\x12\x16\n\x12\x45RROR_NOT_IN_RANGE\x10\x05\x12\x1c\n\x18\x45RROR_PLAYER_HAS_NO_TEAM\x10\x06\x12\x1d\n\x19\x45RROR_POKEMON_NOT_FULL_HP\x10\x07\x12$\n ERROR_PLAYER_BELOW_MINIMUM_LEVEL\x10\x08\x12\x1a\n\x16\x45RROR_POKEMON_IS_BUDDY\x10\t\x12\x1d\n\x19\x45RROR_FORT_DEPLOY_LOCKOUT\x10\n\x12 \n\x1c\x45RROR_PLAYER_HAS_NO_NICKNAME\x10\x0b\x12\x1a\n\x16\x45RROR_POI_INACCESSIBLE\x10\x0c\x12\x17\n\x13\x45RROR_NOT_A_POKEMON\x10\r\x12\x1f\n\x1b\x45RROR_TOO_MANY_OF_SAME_KIND\x10\x0e\x12\x1b\n\x17\x45RROR_TOO_MANY_DEPLOYED\x10\x0f\x12\x1d\n\x19\x45RROR_TEAM_DEPLOY_LOCKOUT\x10\x10\x12\x1b\n\x17\x45RROR_LEGENDARY_POKEMON\x10\x11\x12\x19\n\x15\x45RROR_INVALID_POKEMON\x10\x12\x12\x15\n\x11\x45RROR_RAID_ACTIVE\x10\x13\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_gym_dot_gym__status__and__defenders__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2.DESCRIPTOR,])



_GYMDEPLOYRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GymDeployResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_RESULT_SET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ALREADY_HAS_POKEMON_ON_FORT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_OPPOSING_TEAM_OWNS_FORT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FORT_IS_FULL', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_IN_RANGE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_HAS_NO_TEAM', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_NOT_FULL_HP', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_BELOW_MINIMUM_LEVEL', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_IS_BUDDY', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FORT_DEPLOY_LOCKOUT', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_HAS_NO_NICKNAME', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POI_INACCESSIBLE', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_A_POKEMON', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_TOO_MANY_OF_SAME_KIND', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_TOO_MANY_DEPLOYED', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_TEAM_DEPLOY_LOCKOUT', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_LEGENDARY_POKEMON', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_POKEMON', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_RAID_ACTIVE', index=19, number=19,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=476,
  serialized_end=1055,
)
_sym_db.RegisterEnumDescriptor(_GYMDEPLOYRESPONSE_RESULT)


_GYMDEPLOYRESPONSE = _descriptor.Descriptor(
  name='GymDeployResponse',
  full_name='pogoprotos.networking.responses.GymDeployResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GymDeployResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gym_status_and_defenders', full_name='pogoprotos.networking.responses.GymDeployResponse.gym_status_and_defenders', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='awarded_gym_badge', full_name='pogoprotos.networking.responses.GymDeployResponse.awarded_gym_badge', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cooldown_complete_timestamp_ms', full_name='pogoprotos.networking.responses.GymDeployResponse.cooldown_complete_timestamp_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GYMDEPLOYRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=1055,
)

_GYMDEPLOYRESPONSE.fields_by_name['result'].enum_type = _GYMDEPLOYRESPONSE_RESULT
_GYMDEPLOYRESPONSE.fields_by_name['gym_status_and_defenders'].message_type = pogoprotos_dot_data_dot_gym_dot_gym__status__and__defenders__pb2._GYMSTATUSANDDEFENDERS
_GYMDEPLOYRESPONSE.fields_by_name['awarded_gym_badge'].message_type = pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2._AWARDEDGYMBADGE
_GYMDEPLOYRESPONSE_RESULT.containing_type = _GYMDEPLOYRESPONSE
DESCRIPTOR.message_types_by_name['GymDeployResponse'] = _GYMDEPLOYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GymDeployResponse = _reflection.GeneratedProtocolMessageType('GymDeployResponse', (_message.Message,), dict(
  DESCRIPTOR = _GYMDEPLOYRESPONSE,
  __module__ = 'pogoprotos.networking.responses.gym_deploy_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GymDeployResponse)
  ))
_sym_db.RegisterMessage(GymDeployResponse)


# @@protoc_insertion_point(module_scope)
