# echo

> 주어진 인자들을 출력한다.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/echo>.

- 텍스트 메시지를 출력한다. 참고: 따옴표는 선택 사항:

`echo "{{Hello World}}"`

- 환경 변수가 있는 메시지 출력하기:

`echo "{{My path is $PATH}}"`

- 끝에 줄바꿈 없이 메시지 출력하기:

`echo -n "{{Hello World}}"`

- 파일에 메시지 추가하기:

`echo "{{Hello World}}" >> {{file.txt}}`

- 백슬래시 이스케이프 (특수문자)의 해석을 가능하게 하기:

`echo -e "{{Column 1\tColumn 2}}"`
