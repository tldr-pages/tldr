# helmfile

> Helm 릴리스와 관련 Kubernetes 매니페스트를 선언하고 고나리.
> 더 많은 정보: <https://helmfile.readthedocs.io>.

- 필요한 Helm 플러그인 설치:

`helmfile init`

- 클러스터에 적용될 변경 사항 미리 보기:

`helmfile diff`

- `helmfile.yaml`에 정의된 릴리스를 클러스터에 적용:

`helmfile apply`

- 클러스터를 원하는 상태와 동기화하고, 필요한 경우 강제로 다시 생성:

`helmfile sync`

- 지정한 환경의 릴리스를 적용:

`helmfile {{[-e|--environment]}} {{dev|production|staging}} apply`

- `helmfile.yaml`에 정의된 모든 릴리스 삭제:

`helmfile destroy`

- 도움말 표시:

`helmfile {{[-h|--help]}}`

- 버전 정보 표시:

`helmfile version`
