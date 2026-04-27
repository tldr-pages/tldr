# openstack image

> OpenStack Image 서비스(OpenStack Glance)를 관리하는 명령어이며, 다른 서비스에서 사용하는 데이터 자산을 업로드 및 조회할 수 있습니다.
> 더 많은 정보: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/image-v2.html>.

- 사용 가능한 이미지 목록 출력:

`openstack image list {{--private|--shared|--all}}`

- 이미지 상세 정보 출력:

`openstack image show --human-readable {{이미지_아이디}}`

- 이미지 생성/업로드:

`openstack image create --file {{path/to/file}} {{--private|--shared|--all}} {{이미지_아이디}}`

- 이미지 삭제:

`openstack image delete {{이미지_아이디1 이미지_아이디2 ...}}`

- 이미지를 로컬 파일로 저장:

`openstack image save --file {{파일이름}} {{이미지_아이디}}`
