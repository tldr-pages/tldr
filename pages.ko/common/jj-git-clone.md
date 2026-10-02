# jj git clone

> Git 저장소를 복제하여 Git 백엔드를 사용하는 새로운 저장소를 생성.
> 참고: `--colocate` 옵션을 사용하지 않으면, 유효한 Git 저장소가 아니므로 `git` 명령을 사용할 수 없음.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-git-clone>.

- Git 저장소를 복제하여 새 디렉터리에 저장소 생성 (기본 디렉터리 이름은 저장소 이름):

`jj git clone {{소스}} {{path/to/directory}}`

- 지정한 이름으로 새 원격 저장소를 생성하며 저장소 복제:

`jj git clone --remote {{원격_저장소_이름}} {{소스}}`

- 최근 10개의 커밋만 가져와 Git 저장소 복제:

`jj git clone --depth {{10}} {{소스}}`

- Jujutsu 저장소를 Git 저장소와 동일한 디렉터리에 함께 배치하여 복제 (`jj`와 `git`명령을 모두 같은 디렉터리에 사용할 수 있음):

`jj git clone --colocate {{소스}}`
