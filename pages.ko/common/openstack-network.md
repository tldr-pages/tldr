# openstack network

> OpenStack 네트워크 리소스를 관리하는 명령어.
> 더 많은 정보: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/network.html>.

- 모든 네트워크 목록 출력:

`openstack network list`

- 특정 네트워크 상세 정보 출력:

`openstack network show {{네트워크_아이디_또는_이름}}`

- 주어진 이름으로 새로운 네트워크 생성:

`openstack network create {{네트워크_이름}}`

- 네트워크 삭제:

`openstack network delete {{네트워크_아이디_또는_이름}}`

- 네트워크 활성화:

`openstack network set --enable {{네트워크_아이디_또는_이름}}`

- 네트워크 비활성화:

`openstack network set --disable {{네트워크_아이디_또는_이름}}`
