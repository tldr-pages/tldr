# virsh

> virsh 게스트 도메인을 관리합니다. (NOTE: 'guest_id'는 게스트의 아이디, 이름 또는 UUID일 수 있습니다).
> `virsh list`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://libvirt.org/virshcmdref.html>.

- 하이퍼아비저 세션에 연결:

`virsh connect {{qemu:///system}}`

- 모든 도메인 나열:

`virsh list --all`

- 게스트 구성 파일 덤프:

`virsh dumpxml {{게스트 아이디}} > {{경로/대상/게스트 구성 파일.xml}}`

- 구성 파일에서 게스트 만들기:

`virsh create {{경로/대상/구성 파일.xml}}`

- 게스트의 구성 파일 편집 (편집기는 $EDITOR로 변경할 수 있음):

`virsh edit {{게스트_아이디}}`

- 게스트 시작/재부팅/종료/일시 중지/재개:

`virsh {{명령어}} {{게스트_아이디}}`

- 게스트의 현재 상태를 파일에 저장:

`virsh save {{게스트_아이디}} {{파일이름}}`

- 실행 중인 게스트 삭제:

`virsh destroy {{게스트_아이디}} && virsh undefine {{게스트_아이디}}`
