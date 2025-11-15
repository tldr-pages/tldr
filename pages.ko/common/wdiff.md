# wdiff

> 텍스트 파일 간의 단어 차이를 표시.
> 더 많은 정보: <https://www.gnu.org/software/wdiff/manual/wdiff.html#wdiff-invocation>.

- 두 파일 비교:

`wdiff {{경로/대상/파일1}} {{경로/대상/파일2}}`

- 대소문자를 무시하고 비교:

`wdiff --ignore-case {{경로/대상/파일1}} {{경로/대상/파일2}}`

- 삭제, 삽입 또는 교체된 단어 수 표시:

`wdiff --statistics {{경로/대상/파일1}} {{경로/대상/파일2}}`
