# dvc config

> DVC 저장소의 사용자 정의 구성 옵션을 관리하는 저수준 명령어입니다.
> 이러한 구성은 프로젝트, 로컬, 글로벌 또는 시스템 수준에서 가능합니다.
> 더 많은 정보: <https://dvc.org/doc/command-reference/config>.

- 기본 원격 저장소의 이름 확인:

`dvc config core.remote`

- 프로젝트의 기본 원격 저장소 설정:

`dvc config core.remote {{원격_이름}}`

- 프로젝트의 기본 원격 저장소 설정 해제:

`dvc config --unset core.remote`

- 현재 프로젝트에 대해 지정된 키의 구성 값 확인:

`dvc config {{키}}`

- 프로젝트 수준에서 키의 구성 값 설정:

`dvc config {{키}} {{값}}`

- 주어진 키에 대한 프로젝트 수준 구성 값 설정 해제:

`dvc config --unset {{키}}`

- 로컬, 글로벌 또는 시스템 수준에서 구성 값 설정:

`dvc config --{{local|global|system}} {{키}} {{값}}`
