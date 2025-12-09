# IFS

> IFS (Internal Field Separator)는 Unix쉘에서 단어 분할에 사용되는 구분 기호를 정의하는 특수 환경 변수.
> IFS의 기본값은 공백, 탭 및 줄바꿈. 세 문자는 구분 기호 역할을 함.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Word-Splitting>.

- 현재 IFS 값 보기:

`echo "$IFS"`

- IFS 값 변경:

`IFS="{{:}}"`

- IFS를 기본값으로 재설정:

`IFS=$' \t\n'`

- 서브셸에서 IFS 값을 일시적으로 변경:

`(IFS="{{:}}"; echo "{{one:two:three}}")`
