# VBoxManage showvminfo

> 등록된 가상 머신에 대한 정보 표시.
> 더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-showvminfo>.

- 특정 가상 머신에 대한 정보 표시:

`VBoxManage showvminfo {{vm_이름|uuid}}`

- 특정 가상 머신에 대한 더 자세한 정보 표시:

`VBoxManage showvminfo --details {{vm_이름|uuid}}`

- 기계 판독 형식으로 정보 표시:

`VBoxManage showvminfo --machinereadable {{vm_이름|uuid}}`

- 가상 머신이 암호화된 경우 암호 ID 지정:

`VBoxManage showvminfo --password-id {{암호_id}} {{vm_이름|uuid}}`

- 가상 머신이 암호화된 경우 암호 파일 지정:

`VBoxManage showvminfo --password {{경로/대상/패스워드_파일}} {{vm_이름|uuid}}`

- 특정 가상 머신의 로그 표시:

`VBoxManage showvminfo --log {{vm_이름|uuid}}`
