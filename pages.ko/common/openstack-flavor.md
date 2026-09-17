# openstack flavor

> OpenStack 인스턴스 flavor(가상 하드웨어 템플릿)를 관리하는 명령어.
> 더 많은 정보: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/flavor.html>.

- 모든 flavor 목록 출력:

`openstack flavor list`

- 특정 flavor 상세 정보 출력:

`openstack flavor show {{flavor_아이디_또는_이름}}`

- vCPU 2개, 4GB RAM, 20GB 디스크 flavor 생성:

`openstack flavor create {{flavor_이름}} --vcpus 2 --ram 4096 --disk 20`

- flavor 삭제:

`openstack flavor delete {{flavor_아이디_또는_이름}}`

- 임시 디스크 10GB, 512MB 스왑 공간을 포함한 flavor 생성:

`openstack flavor create {{flavor_이름}} --vcpus 4 --ram 8192 --disk 40 --ephemeral 10 --swap 512`
