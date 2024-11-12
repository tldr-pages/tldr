# git clone

> 기존 저장소를 복제합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-clone>.

- 기존 저장소를 새 디렉토리로 복제 (기본 디렉토리는 저장소 이름):

`git clone {{원격_저장소_위치}} {{경로/대상/폴더}}`

- 기존 저장소 및 그 하위 모듈 복제:

`git clone --recursive {{원격_저장소_위치}}`

- 기존 저장소의 `.git` 디렉토리만 복제:

`git clone --no-checkout {{원격_저장소_위치}}`

- 로컬 저장소 복제:

`git clone --local {{경로/대상/로컬/저장소}}`

- 조용히 복제:

`git clone --quiet {{원격_저장소_위치}}`

- 기존 저장소를 기본 브랜치에서 최근 커밋 10개만 복제 (시간 절약에 좋음):

`git clone --depth {{10}} {{원격_저장소_위치}}`

- 기존 저장소의 특정 브랜치만 복제:

`git clone --branch {{이름}} --single-branch {{원격_저장소_위치}}`

- 특정 SSH 명령을 사용하여 기존 저장소 복제:

`git clone --config core.sshCommand="{{ssh -i path/to/private_ssh_key}}" {{원격_저장소_위치}}`
