# git bulk

> 여러 Git 저장소에서 작업을 실행.
> `git-extras`의 일부.
> 더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-bulk>.

- 현재 디렉토리를 작업 공간으로 등록:

`git bulk --addcurrent {{작업_공간_이름}}`

- 대량 작업을 위한 작업 공간 등록:

`git bulk --addworkspace {{작업_공간_이름}} {{/절대/경로/대상/저장소}}`

- 특정 디렉토리 내에 저장소를 클론하고, 작업 공간으로 등록:

`git bulk --addworkspace {{작업_공간_이름}} {{/절대/경로/대상/부모_디렉토리}} --from {{원격_저장소_위치}}`

- 원격 위치의 새 줄로 구분된 목록에서 저장소를 클론하고, 작업 공간으로 등록:

`git bulk --addworkspace {{작업_공간_이름}} {{/경로/대상/루트_디렉토리}} --from {{/경로/대상/파일}}`

- 등록된 모든 작업 공간 나열:

`git bulk --listall`

- 현재 작업 공간의 저장소에서 Git 명령 실행:

`git bulk {{명령}} {{명령_인수}}`

- 특정 작업 공간 제거:

`git bulk --removeworkspace {{작업_공간_이름}}`

- 모든 작업 공간 제거:

`git bulk --purge`
