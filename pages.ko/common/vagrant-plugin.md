# vagrant plugin

> Vagrant 플러그인을 관리.
> 관련 항목: `vagrant`.
> 더 많은 정보: <https://developer.hashicorp.com/vagrant/docs/cli/plugin>.

- 현재 설치된 모든 플러그인 목록 표시:

`vagrant plugin list`

- 원격 저장소에서 플러그인 설치 (일반적으로 RubyGems):

`vagrant plugin install {{vagrant_vbguest}}`

- 로컬 파일에서 플러그인 설치:

`vagrant plugin install {{경로/대상/자신의_플러그인.gem}}`

- 설치된 모든 플러그인을 최신 버전으로 업데이트:

`vagrant plugin update`

- 지정한 플러그인을 최신 버전으로 업데이트:

`vagrant plugin update {{vagrant_vbguest}}`

- 지정한 플러그인 제거:

`vagrant plugin uninstall {{vagrant_vbguest}}`
