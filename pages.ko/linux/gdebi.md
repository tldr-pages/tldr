# gdebi

> `.deb` 파일을 쉽게 설치합니다.
> 더 많은 정보: <https://manned.org/gdebi>.

- 로컬 `.deb` 패키지를 설치하고 의존성을 해결하여 설치:

`gdebi {{경로/대상/패키지.deb}}`

- 진행 정보를 표시하지 않음:

`gdebi {{경로/대상/패키지.deb}} --quiet`

- APT 구성 옵션 설정:

`gdebi {{경로/대상/패키지.deb}} --option={{APT_옵션}}`

- 대체 루트 디렉토리 사용:

`gdebi {{경로/대상/패키지.deb}} --root={{경로/대상/루트_폴더}}`

- 버전 표시:

`gdebi --version`
