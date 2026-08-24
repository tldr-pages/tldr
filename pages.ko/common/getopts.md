# getopts

> 인자로부터 쉘 옵션 파싱.
> 참고: 이 명령은 긴 형식의 옵션을 지원하지 않아 `getopt` 사용이 권장됨.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-getopts>.

- 현재 컨텍스트에서 옵션이 첫 번째로 설정된 옵션인지 확인:

`getopts {{x}} {{옵션}}; echo ${{옵션}}`

- 문자열 내에서 옵션이 설정되어 있는지 확인 (지정한 옵션은 문자열의 첫 번째 요소여야 함):

`getopts {{x}} {{옵션}} "{{string text}}"; echo ${{옵션}}`

- 인자가 필요한 옵션을 설정하고 출력:

`getopts {{x}}: {{옵션}}; echo ${{옵션}} $OPTARG`

- 여러 옵션을 확인:

`while getopts {{xyz}} {{옵션}}; do case ${{옵션}} in x) {{echo x is set}};; y) {{echo y is set}};; z) {{echo z is set}};; esac; done`

- `getopts`을 무음 모드로 설정하고 옵션 오류 처리:

`while getopts :{{x:}} {{옵션}}; do case ${{옵션}} in x) ;; :) {{echo "Argument required"}};; ?) {{echo "Invalid argument"}} esac;; done`

- `getopts` 초기화:

`OPTIND=1`
