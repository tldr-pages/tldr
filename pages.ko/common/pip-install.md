# pip install

> Python 패키지 설치.
> 더 많은 정보: <https://pip.pypa.io/en/stable/cli/pip_install/>.

- 하나 이상의 패키지 설치:

`pip install {{패키지1 패키지2 ...}}`

- 지정한 모든 패키지를 최신 버전으로 업그레이드하며, 설치되지 않은 패키지는 새로 설치:

`pip install {{패키지1 패키지2 ...}} {{[-U|--upgrade]}}`

- 특정 버전의 패키지 설치:

`pip install {{패키지}}=={{버전}}`

- 파일에 정의된 패키지 설치:

`pip install {{[-r|--requirement]}} {{경로/대상/requirements.txt}}`

- 로컬 아카이브 또는 디렉터리로부터 패키지 설치:

`pip install {{경로/대상/파일.whl|경로/대상/파일.tar.gz|경로/대상/디렉터리}}`

- Git 저장소로부터 패키지 설치:

`pip install git+https://{{example.com}}/{{사용자}}/{{저장소}}.git`

- PyPI 대신 대체소스(URL 또는 디렉터리)에서 패키지 설치 :

`pip install {{[-f|--find-links]}} {{url|경로/대상/디렉터리}} {{패키지}}`

- 현재 디렉터리의 로컬 패키지를 개발 (editable) 모드로 설치:

`pip install {{[-e|--editable]}} .`
