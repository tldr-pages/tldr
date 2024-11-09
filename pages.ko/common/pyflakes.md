# pyflakes

> Python 소스 코드 파일에서 오류를 검사.
> 더 많은 정보: <https://pypi.org/project/pyflakes>.

- 단일 Python 파일 검사:

`pyflakes check {{경로/대상/파일.py}}`

- 특정 폴더 내 Python 파일 검사:

`pyflakes checkPath {{경로/대상/폴더}}`

- 폴더 내의 Python 파일을 재귀적으로 검사:

`pyflakes checkRecursive {{경로/대상/폴더}}`

- 여러 폴더에서 발견된 모든 Python 파일 검사:

`pyflakes iterSourceCode {{경로/대상/폴더_1}} {{경로/대상/폴더_2}}`
