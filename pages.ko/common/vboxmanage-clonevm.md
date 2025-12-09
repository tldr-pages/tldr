# VBoxManage clonevm

> 기존 가상 머신(VM)의 복제본 생성.
> 더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-clonevm>.

- 지정된 VM 복제:

`VBoxManage clonevm {{vm_이름}}`

- 새로운 VM에 대한 새 이름 지정:

`VBoxManage clonevm {{vm_이름}} --name {{새_vm_이름}}`

- 새 VM 구성 파일이 저장될 폴더 지정:

`VBoxManage clonevm {{vm_이름}} --basefolder {{경로/대상/폴더}}`

- VirtualBox에 복제된 VM 등록:

`VBoxManage clonevm {{vm_이름}} --register`
