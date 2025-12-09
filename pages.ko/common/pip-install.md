# pip install

> Python 패키지 설치.
> 더 많은 정보: <https://pip.pypa.io/en/stable/cli/pip_install/>.

- 패키지 설치:

`pip install {{패키지}}`

- 특정 버전의 패키지 설치:

`pip install {{패키지}}=={{버전}}`

- 파일에 나열된 패키지 설치:

`pip install {{[-r|--requirement]}} {{경로/대상/requirements.txt}}`

- URL 또는 로컬 파일 아카이브(.tar.gz | .whl)에서 패키지 설치:

`pip install {{[-f|--find-links]}} {{url|경로/대상/파일}}`

- 현재 디렉토리에 있는 로컬 패키지를 개발(수정 가능) 모드로 설치:

`pip install {{[-e|--editable]}} .`
