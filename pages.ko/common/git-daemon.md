# git daemon

> Git 저장소를 위한 매우 간단한 서버.
> 더 많은 정보: <https://git-scm.com/docs/git-daemon>.

- 허용된 디렉토리 집합으로 Git 데몬 실행:

`git daemon --export-all {{경로/대상/폴더1}} {{경로/대상/폴더2}}`

- 특정 기본 디렉토리로 Git 데몬 실행하고 Git 저장소처럼 보이는 모든 하위 디렉토리에서 조회 허용:

`git daemon --base-path={{경로/대상/폴더}} --export-all --reuseaddr`

- 지정된 디렉토리에서 Git 데몬을 실행하여 로그 메시지를 자세히 출력하고 Git 클라이언트가 쓸 수 있도록 허용:

`git daemon {{경로/대상/폴더}} --enable=receive-pack --informative-errors --verbose`
