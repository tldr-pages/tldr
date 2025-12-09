# protoc

> Google Protobuf `.proto` 파일을 파싱하고 지정된 언어로 출력을 생성.
> 더 많은 정보: <https://developers.google.com/protocol-buffers>.

- `.proto` 파일에서 Python 코드를 생성:

`protoc --python_out={{경로/대상/출력_폴더}} {{입력_파일.proto}}`

- 다른 `.proto` 파일을 가져오는 `.proto` 파일에서 Java 코드를 생성:

`protoc --java_out={{경로/대상/출력_폴더}} --proto_path={{경로/대상/가져오기_탐색_경로}} {{입력_파일.proto}}`

- 여러 언어에 대한 코드 생성:

`protoc --csharp_out={{경로/대상/c#_출력_폴더}} --js_out={{경로/대상/js_출력_폴더}} {{입력_파일.proto}}`
