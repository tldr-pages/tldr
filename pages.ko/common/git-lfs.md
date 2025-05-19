# git lfs

> Git 저장소에서 대용량 파일을 다루기 위한 도구.
> 더 많은 정보: <https://github.com/git-lfs/git-lfs/tree/main/docs>.

- Git LFS 초기화:

`git lfs install`

- 특정 패턴의 파일 추적:

`git lfs track '{{*.bin}}'`

- Git LFS 엔드포인트 URL 변경 (LFS 서버가 Git 서버와 분리된 경우 유용):

`git config {{[-f|--file]}} .lfsconfig lfs.url {{lfs_endpoint_url}}`

- 추적된 패턴 나열:

`git lfs track`

- 커밋된 추적 파일 나열:

`git lfs ls-files`

- 모든 Git LFS 객체를 원격 서버에 푸시 (오류 발생 시 유용):

`git lfs push --all {{remote_name}} {{branch_name}}`

- 모든 Git LFS 객체 가져오기:

`git lfs fetch`

- 모든 Git LFS 객체 체크아웃:

`git lfs checkout`
