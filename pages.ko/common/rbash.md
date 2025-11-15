# rbash

> 제한된 Bash 셸로, `bash --restricted`와 동등합니다.
> 작업 디렉토리 변경, 명령 출력 리디렉션, 환경 변수 수정 등을 허용하지 않습니다.
> 히스토리 확장을 위해 `histexpand`도 참조하세요.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#The-Restricted-Shell>.

- 대화형 셸 세션 시작:

`rbash`

- 명령을 실행한 후 종료:

`rbash -c "{{명령}}"`

- 스크립트 실행:

`rbash {{경로/대상/스크립트.sh}}`

- 각 명령을 실행 전에 출력하며 스크립트 실행:

`rbash -x {{경로/대상/스크립트.sh}}`

- 스크립트에서 명령을 읽고 첫 번째 오류에서 중지:

`rbash -e {{경로/대상/스크립트.sh}}`

- `stdin`에서 명령을 읽고 실행:

`rbash -s`
