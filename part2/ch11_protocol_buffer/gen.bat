:: Creates interface code for protocol buffer
.\protoc.exe --proto_path=.\ --python_out=.\ .\simple_message.proto
.\protoc.exe --proto_path=.\ --python_out=.\ .\oneof_message.proto
.\protoc.exe --proto_path=.\ --python_out=.\ .\pbuf_message.proto
