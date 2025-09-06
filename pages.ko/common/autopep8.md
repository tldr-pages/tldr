# autopep8

> PEP 8 스타일 가이드에 따라 Python 코드 형식을 지정.
> 더 많은 정보: <https://github.com/hhatto/autopep8>.

- 사용자 정의 최대 줄 길이를 사용해, 파일을 `stdout`로 포맷:

`autopep8 {{경로/대상/파일.py}} --max-line-length {{길이}}`

- 변경 사항의 차이점을 표시하여, 파일을 포맷을 함:

`autopep8 --diff {{경로/대상/파일}}`

- 파일을 제자리에서, 포맷하고 변경 사항을 저장함:

`autopep8 --in-place {{경로/대상/파일.py}}`

- 디렉토리의 모든 파일을 재귀적으로 포맷하고, 변경 사항을 저장:

`autopep8 --in-place --recursive {{경로/대상/디렉토리}}`
