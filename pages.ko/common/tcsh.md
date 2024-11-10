# tcsh

> 파일 이름 자동 완성과 명령 줄 편집 기능을 제공하는 C 셸.
> 같이 보기: `csh`.
> 더 많은 정보: <https://manned.org/tcsh>.

- 상호작용 셸 세션 시작:

`tcsh`

- 시작 구성 파일을 로드하지 않고 상호작용 셸 세션 시작:

`tcsh -f`

- 특정 [c]명령 실행:

`tcsh -c "{{echo 'tcsh is executed'}}"`

- 특정 스크립트 실행:

`tcsh {{경로/대상/스크립트.tcsh}}`

- 특정 스크립트의 구문 오류 검사:

`tcsh -n {{경로/대상/스크립트.tcsh}}`

- `stdin`에서 특정 명령 실행:

`{{echo "echo 'tcsh is executed'"}} | tcsh`
