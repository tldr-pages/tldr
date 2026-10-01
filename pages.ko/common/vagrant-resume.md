# vagrant resume

> 이전에 일시 중지된 Vagrant 관리 machine의 실행을 재개.
> 더 많은 정보: <https://developer.hashicorp.com/vagrant/docs/cli/resume>.

- 이름 또는 id를 지정해 machine 실행 재개:

`vagrant resume {{이름|id}}`

- 실행 재개 후 설정된 모든 provisioner 실행:

`vagrant resume {{이름|id}} --provision`

- 실행 재개 후 지정한 provisioner만 다시 실행:

`vagrant resume {{이름|id}} --provision-with {{provisioner}}`
