# rexec

> 원격 호스트에서 명령을 실행합니다.
> 참고: `rexec`는 데이터를 일반 텍스트로 전송하므로 주의해서 사용하세요. 암호화된 통신을 위해 SSH와 같은 보안 대안을 고려하세요.
> 더 많은 정보: <https://www.gnu.org/software/inetutils/manual/html_node/rexec-invocation.html>.

- 원격 [h]호스트에서 명령 실행:

`rexec -h={{원격_호스트}} {{ls -l}}`

- 원격 [h]호스트에서 원격 [u]사용자명을 지정:

`rexec -username={{사용자명}} -h={{원격_호스트}} {{ps aux}}`

- 원격 [h]호스트에서 `stdin`을 `/dev/null`로 리디렉션:

`rexec --no-err -h={{원격_호스트}} {{ls -l}}`

- 원격 [h]호스트에서 원격 [P]포트를 지정:

`rexec -P={{1234}} -h={{원격_호스트}} {{ls -l}}`
