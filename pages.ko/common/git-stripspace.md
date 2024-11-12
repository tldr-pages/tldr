# git stripspace

> 텍스트(예: 커밋 메시지, 노트, 태그 및 브랜치 설명)를 `stdin`에서 읽고 Git에서 사용하는 방식으로 정리합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-stripspace>.

- 파일에서 공백 제거:

`cat {{경로/대상/파일}} | git stripspace`

- 파일에서 공백 및 Git 주석 제거:

`cat {{경로/대상/파일}} | git stripspace --strip-comments`

- 파일의 모든 줄을 Git 주석으로 변환:

`git stripspace --comment-lines < {{경로/대상/파일}}`
