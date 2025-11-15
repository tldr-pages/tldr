# VBoxManage unregistervm

> 가상 머신(VM)을 등록 해제.
> 더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-unregistervm>.

- 기존 VM 등록 해제:

`VBoxManage unregistervm {{uuid|vm_이름}}`

- 하드 디스크 이미지 파일, 모든 저장된 상태 파일, VM 로그 및 XML VM 머신 파일 삭제:

`VBoxManage unregistervm {{uuid|vm_이름}} --delete`

- VM의 모든 파일 삭제:

`VBoxManage unregistervm {{uuid|vm_이름}} --delete-all`
