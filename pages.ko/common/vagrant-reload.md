# vagrant reload

> `halt`를 실행한 후 `up`을 실행하는 것과 동일.
> 일반적으로 Vagrantfile의 변경 사항을 적용하려면 다시 로드해야 함.
> 관련 항목: `vagrant`.
> 더 많은 정보: <https://developer.hashicorp.com/vagrant/docs/cli/reload>.

- 현재 실행중인 machine 다시 로드:

`vagrant reload`

- 이름 또는 ID를 지정해 machine 다시 로드:

`vagrant reload {{이름|id}}`

- provisioner를 강제로 실행해 다시 로드:

`vagrant reload --provision`
