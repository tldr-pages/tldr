# rename

> 여러 파일 이름 변경.
> 참고: 이 페이지는 `rename` Debian 패키지의 명령을 설명합니다.
> 더 많은 정보: <https://manned.org/file-rename>.

- Perl 공통 정규 표현식을 사용하여 파일 이름 변경 ('foo'를 'bar'로 대체):

`rename {{'s/foo/bar/'}} {{*}}`

- 실행하지 않고 변경될 파일 이름 표시 (드라이런):

`rename -n {{'s/foo/bar/'}} {{*}}`

- 기존 대상 파일이 제거될 수 있어도 강제로 이름 변경:

`rename -f {{'s/foo/bar/'}} {{*}}`

- 파일명을 소문자로 변환 (`-f`를 대소문자 구분 없는 파일 시스템에서 사용하여 "이미 존재" 오류 방지):

`rename 'y/A-Z/a-z/' {{*}}`

- 공백을 밑줄로 대체:

`rename 's/\s+/_/g' {{*}}`
