# colima

> 최소한의 설정으로 macOS 및 Linux용 컨테이너 런타임을 제공.
> 더 많은 정보: <https://github.com/abiosoft/colima>.

- 백그라운드에서 데몬을 시작:

`colima start`

- 구성 파일을 생성하고 사용:

`colima start --edit`

- containerd 시작 및 설정 (`nerdctl`을 통해 containerd를 사용하려면 `nerdctl` 설치):

`colima start --runtime containerd`

- Kubernetes로 시작 (`kubectl`이 필요):

`colima start --kubernetes`

- CPU 수, RAM 메모리 및 디스크 공간(GiB 단위)을 사용자 정의:

`colima start --cpu {{숫자}} --memory {{메모리}} --disk {{저장_공간}}`

- Colima를 통해 Docker 사용 (Docker가 필요함):

`colima start`

- 정보 및 상태와 함께 컨테이너를 나열:

`colima list`

- 런타임 상태 표시:

`colima status`
