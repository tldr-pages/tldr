# rename

> 여러 파일의 이름을 변경합니다.
> 참고: 이 페이지는 `perl-rename` Arch Linux 패키지의 명령어에 대한 것입니다.
> 더 많은 정보: <https://manned.org/rename>.

- Perl 정규표현식을 사용해 파일 이름 변경 ('foo'를 'bar'로 변경):

`rename {{'s/foo/bar/'}} {{*}}`

- 실행 없이 변경 사항 미리 보기:

`rename -n {{'s/foo/bar/'}} {{*}}`

- 기존 대상 파일을 덮어쓰면서 강제 이름 변경:

`rename -f {{'s/foo/bar/'}} {{*}}`

- 파일명을 소문자로 변환 (대소문자 구분 없는 파일 시스템에서는 "이미 존재" 오류 방지를 위해 `-f` 사용):

`rename 'y/A-Z/a-z/' {{*}}`

- 공백을 밑줄로 대체:

`rename 's/\s+/_/g' {{*}}`
