# git annotate

> 파일의 각 줄에 커밋 해시와 마지막 작성자를 표시합니다.
> `git blame`을 참조하세요, `git annotate`보다 선호됩니다.
> `git annotate`는 다른 버전 관리 시스템에 익숙한 사람들을 위해 제공됩니다.
> 더 많은 정보: <https://git-scm.com/docs/git-annotate>.

- 각 줄에 작성자 이름과 커밋 해시를 추가하여 파일 출력:

`git annotate {{경로/대상/파일}}`

- 각 줄에 작성자 이메일과 커밋 해시를 추가하여 파일 출력:

`git annotate {{[-e|--show-email]}} {{경로/대상/파일}}`

- 정규 표현식과 일치하는 줄만 출력:

`git annotate -L :{{정규식}} {{경로/대상/파일}}`
