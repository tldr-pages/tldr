# eget

> GitHub에서 사전 구축된 바이너리를 쉽게 설치 가능.
> 더 많은 정보: <https://github.com/zyedidia/eget>.

- GitHub 저장소에서 현재 시스템에 대해 사전 빌드된 바이너리를 다운로드:

`eget {{zyedidia/micro}}`

- URL부터 다운로드:

`eget {{https://go.dev/dl/go1.17.5.linux-amd64.tar.gz}}`

- 다운로드한 파일을 저장할 위치를 지정:

`eget {{zyedidia/micro}} --to={{경로/대상/디렉터리}}`

- 최신 버전을 사용하는 대신 Git 태그를 지정:

`eget {{zyedidia/micro}} --tag={{v2.0.10}}`

- 최신 안정 버전 대신 최신 시험판을 설치:

`eget {{zyedidia/micro}} --pre-release`

- 추출을 건너뛰고, 리소스만 다운로드:

`eget {{zyedidia/micro}} --download-only`

- 현재 다운로드한 버전보다 회신 버전이 있는 경우에만 다운로드:

`eget {{zyedidia/micro}} --upgrade-only`
