# VBoxManage createvm

> 새 가상 머신 생성.
> 더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-createvm>.

- 기본 설정으로 새 VM 생성:

`VBoxManage createvm --name {{vm_이름}}`

- VM 구성 파일이 저장될 기본 폴더 설정:

`VBoxManage createvm --name {{vm_이름}} --basefolder {{경로/대상/폴더}}`

- 가져온 VM의 게스트 OS 유형 설정 (`VBoxManage list ostypes` 중 하나):

`VBoxManage createvm --name {{vm_이름}} --ostype {{os유형}}`

- 생성된 VM을 VirtualBox에 등록:

`VBoxManage createvm --name {{vm_이름}} --register`

- VM을 지정된 그룹에 설정:

`VBoxManage createvm --name {{vm_이름}} --group {{그룹1,그룹2,...}}`

- VM의 전역 고유 식별자(UUID) 설정:

`VBoxManage createvm --name {{vm_이름}} --uuid {{uuid}}`

- 암호화에 사용할 암호화 방식 설정:

`VBoxManage createvm --name {{vm_이름}} --cipher {{AES-128|AES-256}}`
