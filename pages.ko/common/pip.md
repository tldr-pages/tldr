# pip

> Python 패키지 관리자.
> `install`와 같은 일부 하위 명령어는 별도의 사용 문서가 존재.
> 더 많은 정보: <https://pip.pypa.io/en/stable/cli/pip/>.

- 패키지 설치 (더 많은 설치 예시는 `pip install`를 참고):

`pip install {{패키지}}`

- 시스템 전체 기본 위치 대신 사용자 디렉터리에 패키지 설치:

`pip install --user {{패키지}}`

- 패키지 업그레이드:

`pip install {{[-U|--upgrade]}} {{패키지}}`

- 패키지 제거:

`pip uninstall {{패키지}}`

- 설치된 패키지 목록을 파일로 저장:

`pip freeze > {{requirements.txt}}`

- 설치된 패키지 목록 표시:

`pip list`

- 설치된 패키지 정보 표시:

`pip show {{패키지}}`

- 파일에 정의된 패키지 설치:

`pip install {{[-r|--requirement]}} {{requirements.txt}}`
