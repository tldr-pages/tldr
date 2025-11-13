# alias

> 명령 문자열로 대체되는 단어인 별칭 -- 작성.
> 별칭은 셀의 구성 파일에 정의되어 있지 않으면 현재 쉘 세션으로 만료됩니다, 예 : `~/.bashrc`.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-alias>.

- 모든 별칭 리스트:

`alias`

- 일반 별칭 생성:

`alias {{단어}}="{{명령어}}"`

- 주어진 별칭에 연관된 명령어:

`alias {{단어}}`

- 별칭 명령어 제거:

`unalias {{단어}}`

- `rm` 을 대화형 명령어로 전환:

`alias {{rm}}="{{rm -i}}"`

- `ls -a`의 지름길인 `la`생성:

`alias {{la}}="{{ls -a}}"`
