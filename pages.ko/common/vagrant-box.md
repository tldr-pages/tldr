# vagrant box

> Vagrant box (가상 머신 이미지)를 관리.
> 관련 항목: `vagrant`.
> 더 많은 정보: <https://developer.hashicorp.com/vagrant/docs/cli/box>.

- 모든 설치된 box 목록 표시:

`vagrant box list`

- 새로운 box 추가:

`vagrant box add {{hashicorp/bionic64}}`

- 사용자 지정 URL에서 box 추가:

`vagrant box add {{자신의-box}} {{https://example.com/my-box.box}}`

- 설치된 box 제거:

`vagrant box remove {{hashicorp/bionic64}}`

- 현재 Vagrant 환경에서 사용 중인 모든 box 업데이트:

`vagrant box update`

- 지정한 box 업데이트:

`vagrant box update --box {{bento/debian-12}}`

- 현재 사용 중인 box의 새로운 버전이 있는지 확인:

`vagrant box outdated`

- 설치된 box의 이전 버전 정리:

`vagrant box prune`
