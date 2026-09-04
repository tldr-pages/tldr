# vagrant port

> 게스트 머신과 호스트 간 포트 매핑을 표시.
> 관련 항목: `vagrant`.
> 더 많은 정보: <https://developer.hashicorp.com/vagrant/docs/cli/port>.

- 현재 디렉터리에서 실행중인 machine의 모든 포트 매핑 표시:

`vagrant port`

- 특정 machine의 포트 매핑 표시 (`Vagrantfile`이 여러 머신을 정의한 경우):

`vagrant port {{machine_이름}}`

- 지정한 게스트 포트의 매핑 정보 표시:

`vagrant port --guest {{포트_번호}}`

- machine이 처리하기 쉬운 형식으로 출력:

`vagrant port --machine-readable`
