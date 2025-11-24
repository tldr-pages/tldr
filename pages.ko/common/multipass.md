# multipass

> 네이티브 하이퍼바이저를 사용하여 Ubuntu 가상 머신을 관리.
> 더 많은 정보: <https://documentation.ubuntu.com/multipass/en/latest/reference/command-line-interface/>.

- 인스턴스를 시작할 때 사용할 수 있는 별칭 나열:

`multipass find`

- 새 인스턴스를 시작하고 이름을 설정하고 클라우드-초기화 설정 파일 사용:

`multipass launch -n {{인스턴스_이름}} --cloud-init {{설정_파일}}`

- 생성된 모든 인스턴스와 일부 속성 나열:

`multipass list`

- 특정 이름의 인스턴스 시작:

`multipass start {{인스턴스_이름}}`

- 인스턴스의 속성 표시:

`multipass info {{인스턴스_이름}}`

- 특정 이름의 인스턴스에서 셸 프롬프트 열기:

`multipass shell {{인스턴스_이름}}`

- 이름으로 인스턴스 삭제:

`multipass delete {{인스턴스_이름}}`

- 특정 인스턴스에 디렉토리 마운트:

`multipass mount {{경로/대상/로컬/디렉토리}} {{인스턴스_이름}}:{{경로/대상/대상/디렉토리}}`
