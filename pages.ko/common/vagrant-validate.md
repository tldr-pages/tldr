# vagrant validate

> Vagrantfile의 유효성을 검사.
> 관련 항목: `vagrant`, `vagrant box`, `vagrant plugin`.
> 더 많은 정보: <https://developer.hashicorp.com/vagrant/docs/cli/validate>.

- Vagrantfile의 구문과 구조가 올바르고 오류 없는지 검사:

`vagrant validate`

- 지정한 provider의 설정 옵션을 무시하며 Vagrantfile의 구조가 올바른지 검사:

`vagrant validate {{[-p|--ignore-provider]}} {{docker|hypervlibvirt|parallels|qemu|virtualbox|vmware_desktop}}`
