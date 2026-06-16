# openstack port

> OpenStack 네트워크 포트 (가상 네트워크 인터페이스)를 관리하는 명령어.
> 더 많은 정보: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/port.html>.

- 모든 포트 목록 출력:

`openstack port list`

- 특정 포트 상세 정보 출력:

`openstack port show {{포트_아이디_또는_이름}}`

- 특정 네트워크에 포트 생성:

`openstack port create --network {{네트워크_아이디_또는_이름}} {{포트_이름}}`

- 고정 IP `192.168.1.50`를 지정해 포트 생성:

`openstack port create --network {{네트워크_아이디}} --fixed-ip subnet={{서브넷_아이디}},ip-address=192.168.1.50 {{포트_이름}}`

- 포트 삭제:

`openstack port delete {{포트_아이디_또는_이름}}`
