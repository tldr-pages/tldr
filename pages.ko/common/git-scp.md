# git scp

> 현재 작업 트리에서 원격 저장소의 작업 디렉토리로 파일을 복사합니다.
> `git-extras`의 일부입니다. 파일 전송에는 `rsync`를 사용합니다.
> 더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-scp>.

- 스테이지되지 않은 파일을 특정 원격으로 복사:

`git scp {{remote_name}}`

- 스테이지된 파일과 스테이지되지 않은 파일을 원격으로 복사:

`git scp {{remote_name}} HEAD`

- 마지막 커밋에서 변경된 파일 및 모든 스테이지된 또는 스테이지되지 않은 파일을 원격으로 복사:

`git scp {{remote_name}} HEAD~1`

- 특정 파일을 원격으로 복사:

`git scp {{remote_name}} {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 특정 디렉토리를 원격으로 복사:

`git scp {{remote_name}} {{경로/대상/폴더}}`
