# choom

> OOM(Out-Of-Memory) 킬러 점수를 표시하고 변경.
> 더 많은 정보: <https://manned.org/choom>.

- 특정 프로세스 ID의 OOM-킬러 점수 표시:

`choom -p {{프로세스_ID}}`

- 특정 프로세스의 OOM-킬러 점수 변경:

`choom -p {{프로세스_ID}} -n {{-1000..+1000}}`

- 특정 OOM-킬러 점수로 명령 실행:

`choom -n {{-1000..+1000}} {{명령어}} {{인수1 인수2 ...}}`
