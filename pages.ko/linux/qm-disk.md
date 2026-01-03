# qm disk

> 디스크 이미지 관리.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_disk_import>.

- 가상 디스크에 `n` 기가바이트 추가:

`qm {{[di|disk]}} {{[resi|resize]}} {{가상_머신_ID}} {{디스크_이름}} +{{n}}G`

- 가상 디스크 이동:

`qm {{[di|disk]}} {{[m|move]}} {{가상_머신_ID}} {{대상}} {{색인}}`

- 이전 가상 디스크 복사본 삭제:

`qm {{[di|disk]}} {{[m|move]}} --delete {{가상_머신_ID}} {{대상}} {{색인}}`

- 특정 스토리지 이름을 사용하여 VMDK/`.qcow2`/raw 디스크 이미지 가져오기:

`qm {{[di|disk]}} {{[i|import]}} {{가상_머신_ID}} {{경로/대상/디스크}} {{저장소_이름}} --format {{qcow2|raw|vmdk}}`

- Rescan all storages and update disk sizes and unused disk images:

`qm {{[di|disk]}} {{[resc|rescan]}}`

- Perform a dry-run of a rescan and do not write any changes to configurations:

`qm {{[di|disk]}} {{[resc|rescan]}} --dryrun`

- Specify a virtual machine by its ID:

`qm {{[di|disk]}} {{[resc|rescan]}} --vmid {{100}}`
