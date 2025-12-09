# git rscp

> Reverse `git scp` - 원격 저장소의 작업 디렉터리에서 현재 작업 트리로 파일을 복사.
> `git-extras`의 일부.
> 더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-scp>.

- 원격에서 특정 파일 복사:

`git rscp {{remote_name}} {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 원격에서 특정 디렉터리 복사:

`git rscp {{remote_name}} {{경로/대상/폴더}}`
