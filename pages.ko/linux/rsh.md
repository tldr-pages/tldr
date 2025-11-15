# rsh

> 원격 호스트에서 명령을 실행합니다.
> 더 많은 정보: <https://www.gnu.org/software/inetutils/manual/inetutils.html#rsh-invocation>.

- 원격 호스트에서 명령 실행:

`rsh {{원격_호스트}} {{ls -l}}`

- 특정 사용자명으로 원격 호스트에서 명령 실행:

`rsh {{원격_호스트}} {{[-l|--user]}} {{사용자명}} {{ls -l}}`

- 원격 호스트에서 명령을 실행할 때 `stdin`을 `/dev/null`로 리다이렉트:

`rsh {{원격_호스트}} --no-err {{ls -l}}`
