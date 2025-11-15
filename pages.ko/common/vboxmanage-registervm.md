# VBoxManage registervm

> 가상 머신(VM) 등록.
> 더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-registervm>.

- 기존 VM 등록:

`VBoxManage registervm {{경로/대상/파일이름.vbox}}`

- VM의 암호화 비밀번호 파일 제공:

`VBoxManage registervm {{경로/대상/파일이름.vbox}} --password {{경로/대상/비밀번호_파일}}`

- 명령줄에서 암호화 비밀번호 입력 요청:

`VBoxManage registervm {{경로/대상/파일이름.vbox}} --password -`
