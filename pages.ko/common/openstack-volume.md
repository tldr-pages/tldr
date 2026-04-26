# openstack volume

> OpenStack 볼륨 관리.
> OpenStack Block Storage 서비스(OpenStack Cinder)는 Nova VM, Ironic 베어매탈 호스트, 컨테이너 등에 볼륨을 제공합니다.
> 더 많은 정보:<https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/volume.html>.

- 모든 프로젝트의 볼륨 목록 출력:

`openstack volume list --all-projects`

- 볼륨 상세 정보 출력:

`openstack volume show {{볼륨_아이디}}`

- 새로운 볼륨 생성:

`openstack volume create --size {{size_in_GB}} --image {{이미지_아이디}} --snapshot {{snapshot_id}} {{--bootable|--non-bootable}} {{volume_name}}`

- 볼륨 삭제:

`openstack volume delete {{볼륨_아이디1 볼륨_아이디2 ...}}`

- 볼륨을 다른 호스트로 마이그레이션:

`openstack volume migrate --host {{host_hostname}} {{instance_id}}`

- 볼륨 속성 설정:

`openstack volume set --name {{새로운_볼륨_이름}} --size {{새로운_볼륨_크기}} {{--attached|--detached}} {{--bootable|--non-bootable}} {{볼륨_아이디}}`
