# qm clone

> QEMU/KVM 가상 머신 관리자의 가상 머신 복사 생성.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 가상 머신 복사:

`qm copy {{vm_id}} {{new_vm_id}}`

- 특정 이름을 사용하여 가상 머신 복사:

`qm copy {{vm_id}} {{new_vm_id}} --name {{이름}}`

- 특정 설명을 사용하여 가상 머신 복사:

`qm copy {{vm_id}} {{new_vm_id}} --description {{설명}}`

- 모든 디스크의 전체 복사본을 생성하여 가상 머신 복사:

`qm copy {{vm_id}} {{new_vm_id}} --full`

- 파일 저장소에 특정 형식을 사용하여 가상 머신 복사 (`--full` 필요):

`qm copy {{vm_id}} {{new_vm_id}} --full --format {{qcow2|raw|vmdk}}`

- 특정 풀에 추가하여 가상 머신 복사:

`qm copy {{vm_id}} {{new_vm_id}} --pool {{풀_이름}}`
