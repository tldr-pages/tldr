# b4 prep

> 메일링 리스트에 제출할 새로운 패치 시리즈를 준비.
> 더 많은 정보: <https://b4.docs.kernel.org/en/latest/contributor/prep.html>.

- 지정한 기준점에서 분기된 새로운 패치 시리즈 브랜치 생성:

`b4 prep {{[-n|--new]}} {{시리즈_이름}} {{[-f|--fork-point]}} {{fork_포인트}}`

- 현재 패치 시리즈의 커버 레터(cover letter) 편집:

`b4 prep --edit-cover`

- 커밋 트레일러와 maintainer 파일을 기반으로 커버 레터(cover letter)의 수신자를 자동으로 채움:

`b4 prep {{[-c|--auto-to-cc]}}`

- 패치 시리즈에 대해 로컬 검사 (예: `checkpatch.pl`) 수행:

`b4 prep --check`

- 기존 브랜치를 b4-prep 관리 대상 브랜치로 등록:

`b4 prep {{[-e|--enroll]}} {{기존_브랜치}}`

- 더 이상 사용하지 않는 b4-prep 관리 브랜치를 정리하고 보관:

`b4 prep --cleanup {{브랜치_이름}}`
