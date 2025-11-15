# dvc diff

> DVC로 추적된 파일과 디렉토리의 변경 사항을 표시.
> 더 많은 정보: <https://dvc.org/doc/command-reference/diff>.

- 다른 Git 커밋, 태그, 브랜치와 현재 작업 공간을 기준으로 DVC로 추적된 파일 비교:

`dvc diff {{커밋_해시/태그/브랜치}}`

- 한 Git 커밋에서 다른 커밋으로의 DVC로 추적된 파일의 변경 사항 비교:

`dvc diff {{리비전1}} {{리비전2}}`

- DVC로 추적된 파일을 최신 해시와 함께 비교:

`dvc diff --show-hash {{커밋}}`

- DVC로 추적된 파일을 JSON 형식으로 출력하여 비교:

`dvc diff --show-json --show-hash {{커밋}}`

- DVC로 추적된 파일을 Markdown 형식으로 출력하여 비교:

`dvc diff --show-md --show-hash {{커밋}}`
