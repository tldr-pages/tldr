# qm

> QEMU/KVM 가상 머신 관리자.
> `list`, `start`, `stop`, `clone` 등의 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 모든 가상 머신 나열:

`qm list`

- 로컬 스토리지에 업로드된 ISO 파일을 사용하여 `local-lvm` 스토리지에 4 GB IDE 디스크와 ID가 100인 가상 머신 생성:

`qm create {{100}} -ide0 {{local-lvm:4}} -net0 {{e1000}} -cdrom {{local:iso/proxmox-mailgateway_2.1.iso}}`

- 가상 머신의 ID를 지정하여 구성 보기:

`qm config {{100}}`

- 특정 가상 머신 시작:

`qm start {{100}}`

- 종료 요청을 보내고, 가상 머신이 중지될 때까지 대기:

`qm shutdown {{100}} && qm wait {{100}}`

- 가상 머신을 제거하고 모든 관련 리소스 삭제:

`qm destroy {{100}} --purge`
