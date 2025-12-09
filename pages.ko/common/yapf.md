# yapf

> Python 스타일 가이드 검사기.
> 더 많은 정보: <https://github.com/google/yapf#usage>.

- 변경 사항을 적용하지 않고 변경 사항의 차이를 표시 (드라이런):

`yapf --diff {{경로/대상/파일}}`

- 파일을 제자리에서 포맷하고 변경 사항의 차이를 표시:

`yapf --diff --in-place {{경로/대상/파일}}`

- 디렉토리 내의 모든 Python 파일을 재귀적으로 동시에 포맷:

`yapf --recursive --in-place --style {{pep8}} --parallel {{경로/대상/폴더}}`
