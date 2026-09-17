# cmus-remote

> `cmus`를 제어.
> 관련 항목: `playerctl`.
> 더 많은 정보: <https://manned.org/cmus-remote>.

- 플레이어 상태 정보를 조회([Q]uery):

`cmus-remote -Q`

- 재생을 일시 정지/재개:

`cmus-remote {{[-u|--pause]}}`

- 다음 곡으로 이동:

`cmus-remote {{[-n|--next]}}`

- 이전 곡으로 이동:

`cmus-remote {{[-r|--prev]}}`

- `cmus` 명령을 실행:

`cmus-remote {{[-C|--raw]}} "{{set repeat?}}"`
