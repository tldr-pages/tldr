# git for-each-repo

> 여러 저장소에서 Git 명령을 실행.
> 참고: 이 명령은 실험적이며 변경될 수 있습니다.
> 더 많은 정보: <https://git-scm.com/docs/git-for-each-repo>.

- `maintenance.repo` 사용자 구성 변수에 저장된 목록의 각 저장소에서 유지 관리를 실행:

`git for-each-repo --config={{maintenance.repo}} {{maintenance run}}`

- 글로벌 구성 변수에 나열된 각 저장소에서 `git pull` 실행:

`git for-each-repo --config={{global_configuration_variable}} {{pull}}`
