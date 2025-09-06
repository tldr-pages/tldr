# git config

> Git 저장소의 사용자 지정 설정 옵션을 관리합니다.
> 이러한 설정은 개별 (현재 저장소) 또는 전역 (현재 사용자)용일 수 있습니다.
> 더 많은 정보: <https://git-scm.com/docs/git-config>.

- 전역으로 이름이나 이메일을 설정 (이 정보는 저장소에 커밋하는 데 필요하며 모든 커밋에 포함):

`git config --global {{user.name|user.email}} "{{유저_이름|email@example.com}}"`

- 개별 저장소 또는 전역 설정 항목을 나열:

`git config {{[-l|--list]}} --{{local|global}}`

- 시스템 설정 항목만 나열하고(저장 위치: `/etc/gitconfig`), 파일 위치를 표시:

`git config {{[-l|--list]}} --system --show-origin`

- 주어진 설정 항목의 값을 가져오기:

`git config alias.unstage`

- 주어진 설정 항목의 전역 값을 설정:

`git config --global alias.unstage "reset HEAD --"`

- 전역 설정 항목을 기본값으로 되돌리기:

`git config --global --unset alias.unstage`

- 개별 저장소의 Git 설정(`.git/config`)을 기본 편집기에서 편집:

`git config {{[-e|--edit]}}`

- 전역 Git 설정(기본적으로 `~/.gitconfig` 또는 `$XDG_CONFIG_HOME/git/config` 파일이 존재하는 경우)을 기본 편집기에서 편집:

`git config --global {{[-e|--edit]}}`
