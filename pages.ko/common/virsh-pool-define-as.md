# virsh pool-define-as

> 제공된 인수를 사용하여 영구 가상 머신 스토리지 풀에 대한 `/etc/libvirt/storage`에 구성 파일을 생성합니다.
> 같이 보기: `virsh`, `virsh-pool-build`, `virsh-pool-start`.
> 더 많은 정보: <https://manned.org/virsh>.

- 기본 스토리지 시스템으로 `/var/vms`를 사용하여 pool_name이라는 스토리지 풀에 대한 구성 파일을 생성:

`virsh pool-define-as --name {{풀_이름}} --type {{dir}} --target {{/var/vms}}`
