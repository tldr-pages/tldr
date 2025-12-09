# limactl

> Linux 게스트용 가상 머신 관리자로, 여러 VM 템플릿을 제공합니다.
> macOS에서 컨테이너 실행에 사용할 수 있으며, macOS 및 Linux 호스트에서 일반적인 가상 머신 사용 사례에도 적합합니다.
> 더 많은 정보: <https://github.com/lima-vm/lima>.

- VM 목록 보기:

`limactl list`

- 기본 설정을 사용하여 VM 생성(선택적으로 이름 및/또는 템플릿 제공 가능, 사용 가능한 템플릿은 `limactl create --list-templates` 참조):

`limactl create --name {{vm_이름}} template://{{debian|fedora|ubuntu|...}}`

- VM 시작(일부 의존성이 설치될 수 있으며 몇 분이 소요될 수 있음):

`limactl start {{vm_이름}}`

- VM 내부에서 원격 셸 열기:

`limactl shell {{vm_이름}}`

- VM 내부에서 명령 실행:

`limactl shell {{vm_이름}} {{명령어}}`

- VM 중지/종료:

`limactl stop {{vm_이름}}`

- VM 삭제:

`limactl remove {{vm_이름}}`
