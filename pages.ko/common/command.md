# command

> Command 명령은 쉘이 프로그램을 실행하고 동일한 이름의 기능, 빌드인 및 별칭을 무시하도록 합니다.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-command>.

- ls 별칭이 존재하더라도 문자 그대로 `ls` 프로그램을 실행:

`command ls`

- 기본`$PATH`(`/bin:/usr/bin:/sbin:/usr/sbin:/etc:/usr/etc`)(모든 표준 유틸리티를 찾을 수 있도록 보장)를 사용해 명령을 찾고 실행:

`command -p {{명령어_이름}}`

- 특정 명령의 실행 파일 경로나 별칭 정의를 표시:

`command -v {{명령어_이름}}`
