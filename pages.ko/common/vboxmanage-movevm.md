# VBoxManage movevm

> 가상 머신(VM)을 호스트 시스템의 새로운 위치로 이동.
> 더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-movevm>.

- 지정한 가상 머신을 현재 위치로 이동:

`VBoxManage movevm {{vm_이름}}`

- 가상 머신의 새 위치(전체 또는 상대 경로)를 지정:

`VBoxManage movevm {{vm_이름}} --folder {{경로/대상/새로운_위치}}`
