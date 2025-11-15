# tlmgr check

> TeX Live 설치의 일관성을 검사.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#check-option...-depends-executes-files-runfiles-texmfdbs-all>.

- 전체 TeX Live 설치의 일관성을 검사:

`tlmgr check all`

- 전체 TeX Live 정보의 일관성을 자세한 모드로 검사:

`tlmgr check all -v`

- 누락된 의존성 검사:

`tlmgr check depends`

- 모든 TeX Live 실행 파일이 존재하는지 검사:

`tlmgr check executes`

- 로컬 TLPDB에 나열된 모든 파일이 존재하는지 검사:

`tlmgr check files`

- 실행 파일 섹션에서 중복된 파일 이름 검사:

`tlmgr check runfiles`
