# qm cloud init

> Proxmox Virtual Environment (PVE)에서 관리하는 가상 머신에 대한 cloudinit 설정 구성.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 특정 사용자에 대한 cloudinit 설정 구성 및 사용자 비밀번호 설정:

`qm cloud-init {{가상_머신_ID}} -user={{사용자}} -password={{비밀번호}}`

- 특정 사용자에 대한 cloudinit 설정 구성 및 특정 SSH 키로 사용자 비밀번호 설정:

`qm cloud-init {{가상_머신_ID}} -user={{사용자}} -password={{비밀번호}} -sshkey={{ssh_키}}`

- 특정 가상 머신의 호스트네임 설정:

`qm cloud-init {{가상_머신_ID}} -hostname={{호스트네임}}`

- 특정 가상 머신의 네트워크 인터페이스 설정 구성:

`qm cloud-init {{가상_머신_ID}} -ipconfig {{ipconfig}}`

- 가상 머신에서 `cloud-init`이 실행되기 전에 수행할 셸 스크립트 구성:

`qm cloud-init {{가상_머신_ID}} -pre {{스크립트}}`
