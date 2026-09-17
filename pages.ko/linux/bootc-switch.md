# bootc switch

> 부팅에 사용할 새로운 컨테이너 이미지 참조로 전환하는 명령어.
> 더 많은 정보: <https://manned.org/bootc-switch>.

- 레지스트리의 컨테이너 이미지로 OS 베이스 변경:

`sudo bootc switch {{이미지}}`

- root 사용자의 로컬 이미지 저장소에서 컨테이너 이미지로 OS 베이스를  변경:

`sudo bootc switch --transport containers-storage {{이미지}}`

- tarball에 저장된 컨테이너 이미지로 OS 베이스를 변경:

`sudo bootc switch --transport oci-archive {{경로/대상/이미지.tar.gz}}`
