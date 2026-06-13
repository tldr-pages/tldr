# dockdiver

> Docker 레지스트리와 상호작용하기 위한 도구로, 저장소 목록 조회 및 덤프 기능을 제공.
> 더 많은 정보: <https://github.com/MachiavelliII/dockdiver#instructions>.

- Docker 레지스트리의 모든 저장소 목록 조회:

`dockdiver -url {{https://example.com}} -list`

- 특정 저장소를 기본 출력 디렉터리(docker_dump)로 덤프:

`dockdiver -url {{https://example.com}} -dump {{저장소_이름}}`

- 기본 인증을 사용하여 모든 저장소 덤프:

`dockdiver -url {{https://example.com}} -dump-all -username {{사용자명}} -password {{비밀번호}}`

- 요청 속도 제한 및 사용자 지정 포트(기본 포트는 `5000`)를 설정하여 저장소 덤프:

`dockdiver -url {{https://example.com}} -dump {{저장소_이름}} -port {{port}} -rate {{초_당_요청}} -dir {{경로/대상/출력_디렉토리}}`

- 인증을 위해 Bearer Token을 사용하여 모든 저장소 덤프:

`dockdiver -url {{https://example.com}} -dump-all -bearer {{bearer_token}}`

- 사용자 정의 헤더를 JSON 형태로 추가(예: '{"X-Custom": "Value"}'):

`dockdiver -url {{https://example.com}} -list -headers '{{{"X-Custom": "Value"}}}'`
