# resticprofile

> restic 백업을 위한 설정 프로필을 관리.
> 관련 항목: `restic`, `resticprofile-schedule`, `resticprofile-unschedule`.
> 더 많은 정보: <https://creativeprojects.github.io/resticprofile/configuration/getting_started/index.html#write-your-first-configuration-file>.

- 저장된 모든 스냅샷 목록 표시:

`resticprofile`

- 기본 프로필로 백업을 실행:

`resticprofile backup`

- 지정한 프로필로 백업 실행 (기본 프로필 이름은 "default"):

`resticprofile {{[-n|--name]}} "{{프로필_이름}}" backup`

- dry-run 모드로 실행하고 내부적으로 실행될 restic 명령 표시:

`resticprofile --dry-run backup`

- 설정 파일에 정의된 모든 프로필 이름 표시:

`resticprofile profiles`

- 쉘 자동 완성 스크립트 생성:

`resticprofile generate {{--bash-completion|--zsh-completion}}`

- 지정한 프로필의 모든 세부 정보 표시:

`resticprofile show {{[-n|--name]}} "{{프로필_이름}}"`
