# dep

> Go 프로젝트에서 종속성 관리를 위한 툴.
> 더 많은 정보: <https://deployer.org>.

- 현재 디렉토리를 Go 프로젝트의 루트 디렉토리로 초기화:

`dep init`

- 누락된 종속성 설치(Gopkg.toml 과 .go 파일들 스캔):

`dep ensure`

- 프로젝트의 종속성의 상태 보고:

`dep status`

- 프로젝트에 종속성 추가:

`dep ensure -add {{패키지_url}}`

- 모든 종속성들의 잠긴 버전 업데이트:

`dep ensure -update`
