# vagrant init

> `Vagrantfile`을 생성하여 현재 디렉터리에 Vagrant 환경을 초기화.
> 관련 항목: `vagrant`.
> 더 많은 정보: <https://developer.hashicorp.com/vagrant/docs/cli/init>.

- `Vagrantfile` 생성:

`vagrant init`

- 안내 주석 없이 최소 구성의 `Vagrantfile` 생성:

`vagrant init {{[-m|--minimal]}}`

- box 이름과 URL을 지정하여 생성:

`vagrant init {{box_이름}} {{box_주소}}`

- 특정 box 버전을 지정하여 `Vagrantfile` 생성:

`vagrant init --box-version {{버전}} {{box_이름}}`

- `Vagrantfile`을 `stdout`으로 출력:

`vagrant init {{[-o|--output]}} -`

- 기존 `Vagrantfile` 덮어쓰기:

`vagrant init {{[-f|--force]}}`

- 사용자 지정 ERB 템플릿을 사용하여 `Vagrantfile` 생성:

`vagrant init --template {{경로/대상/파일.erb}}`
