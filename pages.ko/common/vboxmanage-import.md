# VBoxManage import

> 이전에 내보낸 가상 머신(VM)을 가져오기.
> 더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-import>.

- OVF 또는 OVA 파일에서 VM 가져오기:

`VBoxManage import {{경로/대상/파일.ovf}}`

- 가져온 VM의 이름 설정:

`VBoxManage import {{경로/대상/파일.ovf}} --name {{vm_이름}}`

- 가져온 VM의 구성 파일이 저장될 폴더 지정:

`VBoxManage import {{경로/대상/파일.ovf}} --basefolder {{경로/대상/폴더}}`

- VirtualBox에 가져온 VM 등록:

`VBoxManage import {{경로/대상/파일.ovf}} --register`

- 실제로 가져오지 않고 가져오기를 확인하는 드라이런 수행:

`VBoxManage import {{경로/대상/파일.ovf}} --dry-run`

- 가져온 VM의 게스트 OS 유형 설정 (`VBoxManage list ostypes` 중 하나):

`VBoxManage import {{경로/대상/파일.ovf}} --ostype={{os유형}}`

- 가져온 VM의 메모리 크기 설정 (메가바이트 단위):

`VBoxManage import {{경로/대상/파일.ovf}} --memory={{1}}`

- 가져온 VM의 CPU 개수 설정:

`VBoxManage import {{경로/대상/파일.ovf}} --cpus={{1}}`
