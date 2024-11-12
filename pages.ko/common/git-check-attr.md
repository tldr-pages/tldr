# git check-attr

> 각 경로명에 대해 해당 경로명에 대한 gitattribute로 지정되지 않았는지, 설정되었는지 또는 해제되었는지 속성을 나열합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-check-attr>.

- 파일의 모든 속성 값을 확인:

`git check-attr --all {{경로/대상/파일}}`

- 파일의 특정 속성 값을 확인:

`git check-attr {{속성}} {{경로/대상/파일}}`

- 특정 파일들의 모든 속성 값을 확인:

`git check-attr --all {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 하나 이상의 파일에 대한 특정 속성 값을 확인:

`git check-attr {{속성}} {{경로/대상/파일1 경로/대상/파일2 ...}}`
