# kitex

> Go RPC 프레임워크 Kitex에서 제공하는 코드 생성 도구.
> Kitex는 thrift와 protobuf IDL을 모두 수용하며, 서버 측 프로젝트의 스켈레톤을 생성하는 것을 지원합니다.
> 더 많은 정보: <https://www.cloudwego.io>.

- 프로젝트가 `$GOPATH`에 있을 때 클라이언트 코드 생성:

`kitex {{경로/대상/IDL_파일.thrift}}`

- 프로젝트가 `$GOPATH`에 없을 때 클라이언트 코드 생성:

`kitex -module {{github.com/xx-org/xx-name}} {{경로/대상/IDL_파일.thrift}}`

- protobuf IDL로 클라이언트 코드 생성:

`kitex -type protobuf {{경로/대상/IDL_파일.proto}}`

- 서버 코드 생성:

`kitex -service {{서비스_이름}} {{경로/대상/IDL_파일.thrift}}`
