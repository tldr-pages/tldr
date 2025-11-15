# VBoxManage export

> 가상 머신을 가상 어플라이언스(ISO) 또는 클라우드 서비스로 내보내기.
> 더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-export>.

- 대상 OVA 파일 지정:

`VBoxManage export --output {{경로/대상/파일이름.ova}}`

- OVF 0.9 레거시 모드로 내보내기:

`VBoxManage export --legacy09`

- OVF (0.9|1.0|2.0) 형식으로 내보내기:

`VBoxManage export --{{ovf09|ovf10|ovf20}}`

- 내보낸 파일의 매니페스트 생성:

`VBoxManage export --manifest`

- VM 설명 지정:

`VBoxManage export --description "{{vm_설명}}"`
