# svn changelist

> 파일 세트에 변경 목록을 연결.
> 더 많은 정보: <https://svnbook.red-bean.com/en/1.7/svn-book.html#svn.ref.svn.c.changelist>.

- 파일을 변경 목록에 추가하며, 변경 목록이 존재하지 않을 경우 생성:

`svn changelist {{변경목록_이름}} {{경로/대상/파일1}} {{경로/대상/파일2}}`

- 파일을 변경 목록에서 제거:

`svn changelist --remove {{경로/대상/파일1}} {{경로/대상/파일2}}`

- 전체 변경 목록을 한 번에 제거:

`svn changelist --remove --recursive --changelist {{변경목록_이름}} .`

- 공백으로 구분된 디렉토리 목록의 내용을 변경 목록에 추가:

`svn changelist --recursive {{변경목록_이름}} {{경로/대상/폴더1 경로/대상/폴더2 ...}}`

- 변경 목록 커밋:

`svn commit --changelist {{변경목록_이름}}`
