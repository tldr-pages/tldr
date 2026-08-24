# pypy

> 빠르고 호환성 있는 Python 언어의 대체 구현체.
> 더 많은 정보: <https://manned.org/pypy>.

- REPL(대화형 셸) 시작:

`pypy`

- 주어진 Python 파일에서 스크립트 실행:

`pypy {{경로/대상/파일.py}}`

- 대화형 셸의 일부로 스크립트 실행:

`pypy -i {{경로/대상/파일.py}}`

- Python 표현식 실행:

`pypy -c "{{표현식}}"`

- 라이브러리 모듈을 스크립트로 실행 (옵션 목록 종료):

`pypy -m {{모듈}} {{인수}}`

- pip를 사용하여 패키지 설치:

`pypy -m pip install {{패키지}}`

- Python 스크립트를 대화형으로 디버깅:

`pypy -m pdb {{경로/대상/파일.py}}`
