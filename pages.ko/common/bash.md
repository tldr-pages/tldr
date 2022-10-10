# bash

> Bourne-Again SHell, an `sh`- 호환 명령 행 인터프리터.
> 참조 : `zsh`, `histexpand` (history expansion).
> 더 많은 정보:: <https://gnu.org/software/bash/>.

- 대화형 쉘 시작하기:

`bash`

- 설정 파일 로딩 없이 대화형 쉘 시작하기:

`bash --norc`

- 특정 명령어([c]ommands) 실행하기:

`bash -c "{{echo 'bash가 실행되었습니다'}}"`

- 특정 스크립트 실행하기:

`bash {{경로/대상/script.sh}}`

- 각 명령어 실행 전 명령어 인쇄하며 특정 스크립트 실행하기:

`bash -x {{경로/대상/script.sh}}`

- 첫 번째 에러([e]rror)가 발생하면 중지되도록 하며 특정 스크립트 실행하기:

`bash -e {{경로/대상/script.sh}}`

- stdin에서 bash 실행하기:

`{{echo "echo 'bash가 실행되었습니다'"}} | bash`
