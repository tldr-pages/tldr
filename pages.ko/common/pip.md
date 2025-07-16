# pip

> Python 패키지 관리자.
> `install`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://pip.pypa.io>.

- 패키지 설치 (`pip install`에서 더 많은 설치 예시 확인 가능):

`pip install {{패키지}}`

- 시스템 전역 기본 위치 대신 사용자 디렉토리에 패키지 설치:

`pip install --user {{패키지}}`

- 패키지 업그레이드:

`pip install {{[-U|--upgrade]}} {{패키지}}`

- 패키지 제거:

`pip uninstall {{패키지}}`

- 설치된 패키지를 파일에 저장:

`pip freeze > {{requirements.txt}}`

- 설치된 패키지 정보 표시:

`pip show {{패키지}}`

- 파일에서 패키지 설치:

`pip install {{[-r|--requirement]}} {{requirements.txt}}`
