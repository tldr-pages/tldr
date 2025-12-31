# git remote

> 원격 저장소(remote repositories)를 관리하는 명령어입니다.
> 더 많은 정보: <https://git-scm.com/docs/git-remote>.

- 이름과 URL을 포함한 기존 원격 저장소 목록 보기:

`git remote {{[-v|--verbose]}}`

- 특정 원격 저장소에 대한 정보 표시:

`git remote show {{원격_저장소_이름}}`

- 원격 저장소 추가:

`git remote add {{원격_저장소_이름}} {{원격_저장소_URL}}`

- 원격 저장소의 URL 변경 (기존 URL을 유지하려면 --add 사용):

`git remote set-url {{원격_저장소_이름}} {{새_URL}}`

- 원격 저장소의 URL 표시:

`git remote get-url {{원격_저장소_이름}}`

- 원격 저장소 제거:

`git remote remove {{원격_저장소_이름}}`

- 원격 저장소 이름 변경:

`git remote rename {{이전_이름}} {{새_이름}}`
