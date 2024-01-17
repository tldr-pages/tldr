# git clone

> 이미 존재하는 레포지토리를 복제.
> 더 많은 정보: <https://git-scm.com/docs/git-clone>.

- 이미 존재하는 레포지토리를 특정 디렉토리에 복제:

`git clone {{원격_레포지토리_경로}} {{경로/대상/디렉터리}}`

- 이미 존재하는 레포지토리를 그 서브모듈을 복제:

`git clone --recursive {{원격_레포지토리_경로}}`

- 기존 저장소의 `.git` 디렉토리를 복제:

`git clone --no-checkout {{원격_레포지토리_경로}}`

- 로컬 레포지토리를 복제:

`git clone --local {{경로/대상/로컬/레포지토리}}`

- 출력 없이 복제:

`git clone --quiet {{원격_레포지토리_경로}}`

- 이미 존재하는 레포지토리를 최근 커밋 10개만 복제 (시간 절약에 좋음):

`git clone --depth {{10}} {{원격_레포지토리_경로}}`

- 이미 존재하는 레포지토리의 특정 브랜치만 복제:

`git clone --branch {{브랜치_이름}} --single-branch {{원격_레포지토리_경로}}`

- 특정 SSH 명령어를 사용하여 이미 존재하는 레포지토리 복제:

`git clone --config core.sshCommand="{{ssh -i 경로/대상/개인_ssh_key}}" {{원격_레포지토리_경로}}`
