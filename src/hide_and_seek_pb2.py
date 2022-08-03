# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hide_and_seek.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13hide_and_seek.proto\x12\"ir.sharif.aic.hideandseek.api.grpc\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"Z\n\x04Turn\x12\x12\n\nturnNumber\x18\x01 \x01(\x05\x12>\n\x08turnType\x18\x02 \x01(\x0e\x32,.ir.sharif.aic.hideandseek.api.grpc.TurnType\"\xaa\x01\n\x05\x41gent\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x04team\x18\x02 \x01(\x0e\x32(.ir.sharif.aic.hideandseek.api.grpc.Team\x12;\n\x04type\x18\x03 \x01(\x0e\x32-.ir.sharif.aic.hideandseek.api.grpc.AgentType\x12\x0f\n\x07node_id\x18\x04 \x01(\x05\x12\x0f\n\x07is_dead\x18\x05 \x01(\x08\"\x12\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\x05\"P\n\x04Path\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x15\n\rfirst_node_id\x18\x02 \x01(\x05\x12\x16\n\x0esecond_node_id\x18\x03 \x01(\x05\x12\r\n\x05price\x18\x04 \x01(\x01\"y\n\x05Graph\x12\x37\n\x05paths\x18\x01 \x03(\x0b\x32(.ir.sharif.aic.hideandseek.api.grpc.Path\x12\x37\n\x05nodes\x18\x02 \x03(\x0b\x32(.ir.sharif.aic.hideandseek.api.grpc.Node\"M\n\x0eIncomeSettings\x12\x1c\n\x14policeIncomeEachTurn\x18\x01 \x01(\x01\x12\x1d\n\x15thievesIncomeEachTurn\x18\x02 \x01(\x01\"6\n\x0cTurnSettings\x12\x10\n\x08maxTurns\x18\x01 \x01(\x05\x12\x14\n\x0cvisibleTurns\x18\x02 \x03(\x05\"D\n\x0c\x43hatSettings\x12\x16\n\x0e\x63hatBoxMaxSize\x18\x01 \x01(\x05\x12\x1c\n\x14\x63hatCostPerCharacter\x18\x02 \x01(\x01\"\xa2\x02\n\nGameConfig\x12\x38\n\x05graph\x18\x01 \x01(\x0b\x32).ir.sharif.aic.hideandseek.api.grpc.Graph\x12J\n\x0eincomeSettings\x18\x02 \x01(\x0b\x32\x32.ir.sharif.aic.hideandseek.api.grpc.IncomeSettings\x12\x46\n\x0cturnSettings\x18\x03 \x01(\x0b\x32\x30.ir.sharif.aic.hideandseek.api.grpc.TurnSettings\x12\x46\n\x0c\x63hatSettings\x18\x04 \x01(\x0b\x32\x30.ir.sharif.aic.hideandseek.api.grpc.ChatSettings\"=\n\x17\x44\x65\x63lareReadinessCommand\x12\r\n\x05token\x18\x01 \x01(\t\x12\x13\n\x0bstartNodeId\x18\x02 \x01(\x05\".\n\x0bMoveCommand\x12\r\n\x05token\x18\x01 \x01(\t\x12\x10\n\x08toNodeId\x18\x02 \x01(\x05\"\x1d\n\x0cWatchCommand\x12\r\n\x05token\x18\x01 \x01(\t\"\xcc\x03\n\x08GameView\x12>\n\x06status\x18\x01 \x01(\x0e\x32..ir.sharif.aic.hideandseek.api.grpc.GameStatus\x12>\n\x06result\x18\x02 \x01(\x0e\x32..ir.sharif.aic.hideandseek.api.grpc.GameResult\x12\x36\n\x04turn\x18\x03 \x01(\x0b\x32(.ir.sharif.aic.hideandseek.api.grpc.Turn\x12>\n\x06\x63onfig\x18\x04 \x01(\x0b\x32..ir.sharif.aic.hideandseek.api.grpc.GameConfig\x12\x39\n\x06viewer\x18\x05 \x01(\x0b\x32).ir.sharif.aic.hideandseek.api.grpc.Agent\x12\x0f\n\x07\x62\x61lance\x18\x06 \x01(\x01\x12\x41\n\x0evisible_agents\x18\x07 \x03(\x0b\x32).ir.sharif.aic.hideandseek.api.grpc.Agent\x12\x39\n\x07\x63hatBox\x18\x08 \x03(\x0b\x32(.ir.sharif.aic.hideandseek.api.grpc.Chat\"*\n\x0b\x43hatCommand\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"d\n\x04\x43hat\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x66romAgentId\x18\x02 \x01(\x05\x12\x0c\n\x04text\x18\x03 \x01(\t\x12-\n\ttimeStamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*\x1d\n\x04Team\x12\t\n\x05\x46IRST\x10\x00\x12\n\n\x06SECOND\x10\x01*+\n\x08TurnType\x12\x0e\n\nTHIEF_TURN\x10\x00\x12\x0f\n\x0bPOLICE_TURN\x10\x01*\"\n\tAgentType\x12\t\n\x05THIEF\x10\x00\x12\n\n\x06POLICE\x10\x01*4\n\nGameStatus\x12\x0b\n\x07PENDING\x10\x00\x12\x0b\n\x07ONGOING\x10\x01\x12\x0c\n\x08\x46INISHED\x10\x02*C\n\nGameResult\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nFIRST_WINS\x10\x01\x12\x0f\n\x0bSECOND_WINS\x10\x02\x12\x07\n\x03TIE\x10\x03\x32\x8a\x03\n\x0bGameHandler\x12g\n\x10\x44\x65\x63lareReadiness\x12;.ir.sharif.aic.hideandseek.api.grpc.DeclareReadinessCommand\x1a\x16.google.protobuf.Empty\x12i\n\x05Watch\x12\x30.ir.sharif.aic.hideandseek.api.grpc.WatchCommand\x1a,.ir.sharif.aic.hideandseek.api.grpc.GameView0\x01\x12O\n\x04Move\x12/.ir.sharif.aic.hideandseek.api.grpc.MoveCommand\x1a\x16.google.protobuf.Empty\x12V\n\x0bSendMessage\x12/.ir.sharif.aic.hideandseek.api.grpc.ChatCommand\x1a\x16.google.protobuf.Emptyb\x06proto3')

_TEAM = DESCRIPTOR.enum_types_by_name['Team']
Team = enum_type_wrapper.EnumTypeWrapper(_TEAM)
_TURNTYPE = DESCRIPTOR.enum_types_by_name['TurnType']
TurnType = enum_type_wrapper.EnumTypeWrapper(_TURNTYPE)
_AGENTTYPE = DESCRIPTOR.enum_types_by_name['AgentType']
AgentType = enum_type_wrapper.EnumTypeWrapper(_AGENTTYPE)
_GAMESTATUS = DESCRIPTOR.enum_types_by_name['GameStatus']
GameStatus = enum_type_wrapper.EnumTypeWrapper(_GAMESTATUS)
_GAMERESULT = DESCRIPTOR.enum_types_by_name['GameResult']
GameResult = enum_type_wrapper.EnumTypeWrapper(_GAMERESULT)
FIRST = 0
SECOND = 1
THIEF_TURN = 0
POLICE_TURN = 1
THIEF = 0
POLICE = 1
PENDING = 0
ONGOING = 1
FINISHED = 2
UNKNOWN = 0
FIRST_WINS = 1
SECOND_WINS = 2
TIE = 3


_TURN = DESCRIPTOR.message_types_by_name['Turn']
_AGENT = DESCRIPTOR.message_types_by_name['Agent']
_NODE = DESCRIPTOR.message_types_by_name['Node']
_PATH = DESCRIPTOR.message_types_by_name['Path']
_GRAPH = DESCRIPTOR.message_types_by_name['Graph']
_INCOMESETTINGS = DESCRIPTOR.message_types_by_name['IncomeSettings']
_TURNSETTINGS = DESCRIPTOR.message_types_by_name['TurnSettings']
_CHATSETTINGS = DESCRIPTOR.message_types_by_name['ChatSettings']
_GAMECONFIG = DESCRIPTOR.message_types_by_name['GameConfig']
_DECLAREREADINESSCOMMAND = DESCRIPTOR.message_types_by_name['DeclareReadinessCommand']
_MOVECOMMAND = DESCRIPTOR.message_types_by_name['MoveCommand']
_WATCHCOMMAND = DESCRIPTOR.message_types_by_name['WatchCommand']
_GAMEVIEW = DESCRIPTOR.message_types_by_name['GameView']
_CHATCOMMAND = DESCRIPTOR.message_types_by_name['ChatCommand']
_CHAT = DESCRIPTOR.message_types_by_name['Chat']
Turn = _reflection.GeneratedProtocolMessageType('Turn', (_message.Message,), {
  'DESCRIPTOR' : _TURN,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.Turn)
  })
_sym_db.RegisterMessage(Turn)

Agent = _reflection.GeneratedProtocolMessageType('Agent', (_message.Message,), {
  'DESCRIPTOR' : _AGENT,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.Agent)
  })
_sym_db.RegisterMessage(Agent)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.Node)
  })
_sym_db.RegisterMessage(Node)

Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), {
  'DESCRIPTOR' : _PATH,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.Path)
  })
_sym_db.RegisterMessage(Path)

Graph = _reflection.GeneratedProtocolMessageType('Graph', (_message.Message,), {
  'DESCRIPTOR' : _GRAPH,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.Graph)
  })
_sym_db.RegisterMessage(Graph)

IncomeSettings = _reflection.GeneratedProtocolMessageType('IncomeSettings', (_message.Message,), {
  'DESCRIPTOR' : _INCOMESETTINGS,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.IncomeSettings)
  })
_sym_db.RegisterMessage(IncomeSettings)

TurnSettings = _reflection.GeneratedProtocolMessageType('TurnSettings', (_message.Message,), {
  'DESCRIPTOR' : _TURNSETTINGS,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.TurnSettings)
  })
_sym_db.RegisterMessage(TurnSettings)

ChatSettings = _reflection.GeneratedProtocolMessageType('ChatSettings', (_message.Message,), {
  'DESCRIPTOR' : _CHATSETTINGS,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.ChatSettings)
  })
_sym_db.RegisterMessage(ChatSettings)

GameConfig = _reflection.GeneratedProtocolMessageType('GameConfig', (_message.Message,), {
  'DESCRIPTOR' : _GAMECONFIG,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.GameConfig)
  })
_sym_db.RegisterMessage(GameConfig)

DeclareReadinessCommand = _reflection.GeneratedProtocolMessageType('DeclareReadinessCommand', (_message.Message,), {
  'DESCRIPTOR' : _DECLAREREADINESSCOMMAND,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.DeclareReadinessCommand)
  })
_sym_db.RegisterMessage(DeclareReadinessCommand)

MoveCommand = _reflection.GeneratedProtocolMessageType('MoveCommand', (_message.Message,), {
  'DESCRIPTOR' : _MOVECOMMAND,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.MoveCommand)
  })
_sym_db.RegisterMessage(MoveCommand)

WatchCommand = _reflection.GeneratedProtocolMessageType('WatchCommand', (_message.Message,), {
  'DESCRIPTOR' : _WATCHCOMMAND,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.WatchCommand)
  })
_sym_db.RegisterMessage(WatchCommand)

GameView = _reflection.GeneratedProtocolMessageType('GameView', (_message.Message,), {
  'DESCRIPTOR' : _GAMEVIEW,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.GameView)
  })
_sym_db.RegisterMessage(GameView)

ChatCommand = _reflection.GeneratedProtocolMessageType('ChatCommand', (_message.Message,), {
  'DESCRIPTOR' : _CHATCOMMAND,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.ChatCommand)
  })
_sym_db.RegisterMessage(ChatCommand)

Chat = _reflection.GeneratedProtocolMessageType('Chat', (_message.Message,), {
  'DESCRIPTOR' : _CHAT,
  '__module__' : 'hide_and_seek_pb2'
  # @@protoc_insertion_point(class_scope:ir.sharif.aic.hideandseek.api.grpc.Chat)
  })
_sym_db.RegisterMessage(Chat)

_GAMEHANDLER = DESCRIPTOR.services_by_name['GameHandler']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TEAM._serialized_start=1860
  _TEAM._serialized_end=1889
  _TURNTYPE._serialized_start=1891
  _TURNTYPE._serialized_end=1934
  _AGENTTYPE._serialized_start=1936
  _AGENTTYPE._serialized_end=1970
  _GAMESTATUS._serialized_start=1972
  _GAMESTATUS._serialized_end=2024
  _GAMERESULT._serialized_start=2026
  _GAMERESULT._serialized_end=2093
  _TURN._serialized_start=121
  _TURN._serialized_end=211
  _AGENT._serialized_start=214
  _AGENT._serialized_end=384
  _NODE._serialized_start=386
  _NODE._serialized_end=404
  _PATH._serialized_start=406
  _PATH._serialized_end=486
  _GRAPH._serialized_start=488
  _GRAPH._serialized_end=609
  _INCOMESETTINGS._serialized_start=611
  _INCOMESETTINGS._serialized_end=688
  _TURNSETTINGS._serialized_start=690
  _TURNSETTINGS._serialized_end=744
  _CHATSETTINGS._serialized_start=746
  _CHATSETTINGS._serialized_end=814
  _GAMECONFIG._serialized_start=817
  _GAMECONFIG._serialized_end=1107
  _DECLAREREADINESSCOMMAND._serialized_start=1109
  _DECLAREREADINESSCOMMAND._serialized_end=1170
  _MOVECOMMAND._serialized_start=1172
  _MOVECOMMAND._serialized_end=1218
  _WATCHCOMMAND._serialized_start=1220
  _WATCHCOMMAND._serialized_end=1249
  _GAMEVIEW._serialized_start=1252
  _GAMEVIEW._serialized_end=1712
  _CHATCOMMAND._serialized_start=1714
  _CHATCOMMAND._serialized_end=1756
  _CHAT._serialized_start=1758
  _CHAT._serialized_end=1858
  _GAMEHANDLER._serialized_start=2096
  _GAMEHANDLER._serialized_end=2490
# @@protoc_insertion_point(module_scope)
