# openstack subnet

> OpenStack 서브넷(네트워크 내 IP 주소 범위)을 관리하는 명령어.
> 더 많은 정보: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/subnet.html>.

- 모든 서브넷 목록 출력:

`openstack subnet list`

- 특정 서브넷 상세 정보 출력:

`openstack subnet show {{서브넷_아이디_또는_이름}}`

- 특정 네트워크에 속한 서브넷 목록 출력:

`openstack subnet list --network {{네트워크_아이디_또는_이름}}`

- 지정한 네트워크에 `192.168.0.0/24` 범위의 서브넷 생성:

`openstack subnet create --network {{네트워크_아이디_또는_이름}} --subnet-range 192.168.0.0/24 {{서브넷_이름}}`

- 서브넷 삭제:

`openstack subnet delete {{서브넷_아이디_또는_이름}}`

- DNS `8.8.8.8` 설정 및 이름 변경:

`openstack subnet set --dns-nameserver 8.8.8.8 --name {{새로운_서브넷_이름}} {{서브넷_아이디}}`
