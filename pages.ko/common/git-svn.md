# git svn

> Subversion 저장소와 Git 간의 양방향 작업.
> 더 많은 정보: <https://git-scm.com/docs/git-svn>.

- SVN 저장소 클론:

`git svn clone {{https://example.com/subversion_repo}} {{local_dir}}`

- 특정 리비전 번호에서 시작하여 SVN 저장소 클론:

`git svn clone {{[-r|--revision]}} {{1234}}:HEAD {{https://svn.example.net/subversion/repo}} {{local_dir}}`

- 원격 SVN 저장소에서 로컬 클론 업데이트:

`git svn rebase`

- Git HEAD를 변경하지 않고 원격 SVN 저장소에서 업데이트 가져오기:

`git svn fetch`

- SVN 저장소에 커밋:

`git svn commit`
