# tart

> Apple Silicon에서 macOS 및 Linux 가상 머신(VM)을 빌드, 실행 및 관리.
> 더 많은 정보: <https://github.com/cirruslabs/tart>.

- 원격 VM 이미지 가져오기:

`tart pull {{acme.io/org/name:tag}}`

- 로컬 또는 원격 이미지 소스에서 VM 복제:

`tart clone {{소스-VM}} {{VM-이름}}`

- 특정 ipsw 파일에서 새로운 Mac VM 생성:

`tart create --from-ipsw={{latest|경로/대상/파일.ipsw}} {{VM-이름}}`

- 기존 VM 실행:

`tart run {{VM-이름}}`

- 특정 폴더를 마운트하여 기존 VM 실행:

`tart run --dir={{경로/대상/폴더}}:{{/경로/대상/로컬_폴더}} {{VM-이름}}`

- VM 목록 나열:

`tart list`

- 실행 중인 VM의 IP 주소 확인:

`tart ip {{VM-이름}}`

- VM의 디스플레이 해상도 변경:

`tart set {{VM-이름}} --display {{640}}x{{400}}`
