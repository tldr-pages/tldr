# mirrord

> 로컬 코드를 Kubernetes 클러스터의 Pod에서 실행하는 것처럼 실행.
> 실제 서비스를 대상으로 기능을 개발하거나 버그를 수정 시 빌드-푸시-배포 과정 생략 가능.
> 더 많은 정보: <https://metalbear.com/mirrord/docs/getting-started/quick-start#cli>.

- 원격 Pod에 연결하여 로컬 바이너리 실행:

`mirrord exec {{[-t|--target]}} pod/{{pod_name}} -- {{명령어}} {{argument1 argument2 ...}}`

- 지정한 네임스페이스의 deployment를 대상으로 로컬 명령 실행:

`mirrord exec {{[-t|--target]}} deployment/{{deployment_name}} {{[-n|--target-namespace]}} {{네임스페이스}} -- {{명령어}}`

- 설정 파일을 사용하여 로컬 명령 실행:

`mirrord exec {{[-f|--config-file]}} {{path/to/mirrord.json}} -- {{명령어}}`

- 로컬 포트를 클러스터 내부에서 접근 가능한 호스트의 포트로 포워딩:

`mirrord port-forward {{[-t|--target]}} pod/{{pod_이름}} --port-mapping {{로컬_포트}}:{{원격_포트}}`

- 원격 대상의 지정한 포트로 들어오는 TCP 트래픽 출력:

`mirrord dump {{[-t|--target]}} pod/{{pod_이름}} {{[-p|--ports]}} {{8080}}`

- 대화형 설정 마법사 실행:

`mirrord wizard`

- mirrord 설정 및 클러스터 연결 상태 진단:

`mirrord diagnose`
