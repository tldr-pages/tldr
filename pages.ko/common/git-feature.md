# git feature

> 기능 브랜치를 생성하거나 병합.
> 기능 브랜치는 feature/<이름> 형식을 따릅니다.
> 더 많은 정보: <https://manned.org/git-feature>.

- 새 기능 브랜치를 생성하고 전환:

`git feature {{기능_브랜치}}`

- 기능 브랜치를 병합 커밋을 생성하며 현재 브랜치에 병합:

`git feature finish {{기능_브랜치}}`

- 기능 브랜치를 하나의 커밋으로 합쳐서 현재 브랜치에 병합:

`git feature finish --squash {{기능_브랜치}}`

- 특정 기능 브랜치의 변경 사항을 원격 대응 브랜치로 전송:

`git feature {{기능_브랜치}} {{[-r|--remote]}} {{원격_이름}}`
