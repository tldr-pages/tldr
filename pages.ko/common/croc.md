# croc

> 모든 네트워크를 통해 쉽고 안전하게 파일을 보내고 받을 수 있음.
> 더 많은 정보: <https://github.com/schollz/croc>.

- 파일 또는 디렉터리 전송:

`croc send {{경로/대상/파일_또는_디렉터리}}`

- 특정 암호를 사용하여 파일이나 디렉터리를 전송:

`croc send --code {{암호}} {{경로/대상/파일_또는_디렉터리}}`

- 수신 시스템에서 파일 또는 디렉터리 수신:

`croc {{암호}}`

- 맞춤형 릴레이를 통해 전송 및 연결:

`croc --relay {{ip_to_relay}} send {{경로/대상/파일_또는_디렉터리}}`

- 맞춤형 릴레이를 통해 수신 및 연결:

`croc --relay {{ip_to_relay}} {{암호}}`

- 기본 포트에서 croc 릴레이를 호스팅:

`croc relay`

- croc 명령에 대한 매개변수 및 옵션 표시:

`croc {{send|relay}} --help`
