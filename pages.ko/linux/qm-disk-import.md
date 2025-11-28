# qm disk import

> 디스크 이미지를 가상 머신에 비사용 디스크로 가져오기.
> `qemu-img`에서 지원하는 이미지 형식(raw, qcow2, qed, vdi, vmdk, vhd)을 사용해야 함.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_disk_import>.

- 특정 스토리지 이름을 사용하여 VMDK/qcow2/raw 디스크 이미지 가져오기:

`qm disk import {{가상_머신_ID}} {{경로/대상/디스크}} {{저장소_이름}} --format {{qcow2|raw|vmdk}}`
