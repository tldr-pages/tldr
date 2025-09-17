# pip3

> Python 패키지 관리자.
> 더 많은 정보: <https://pip.pypa.io>.

- 패키지 설치:

`pip3 install {{패키지}}`

- 특정 버전의 패키지 설치:

`pip3 install {{패키지}}=={{버전}}`

- 패키지 업그레이드:

`pip3 install {{[-U|--upgrade]}} {{패키지}}`

- 패키지 제거:

`pip3 uninstall {{패키지}}`

- 설치된 패키지 목록을 파일에 저장:

`pip3 freeze > {{requirements.txt}}`

- 파일에서 패키지 설치:

`pip3 install {{[-r|--requirement]}} {{requirements.txt}}`

- 설치된 패키지 정보 표시:

`pip3 show {{패키지}}`
