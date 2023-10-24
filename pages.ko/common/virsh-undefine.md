# virsh-undefine

> 가상 머신을 삭제합니다.
> 더 많은 정보: <https://manned.org/virsh>.

- 가상 머신 구성 파일만 삭제:

`virsh undefine --domain {{가상머신_이름}}`

- 구성 파일 및 모든 관련 스토리지 불륨을 삭제:

`virsh undefine --domain {{가상머신_이름}} --remove-all-storage`

- 대상 이름 또는 소스 이름 (`virsh domblklist` 명령에서 얻은 이름)을 사용하여 구성 파일과 지정된 스토리지 볼륨을 삭제:

`virsh undefine --domain {{가상머신_이름}} --storage {{sda,경로/대상/소스}}`
