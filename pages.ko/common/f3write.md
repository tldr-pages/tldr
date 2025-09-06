# f3write

> 실제 용량을 테스트하려면, 드라이브를 .h2w 파일로 채우기.
> 참고: `f3read`, `f3probe`, `f3fix`.
> 더 많은 정보: <https://oss.digirati.com.br/f3/>.

- 지정된 디렉터리에 테스트 파일을 작성하여 드라이브를 채움:

`f3write {{경로/대상/마운트_포인트}}`

- 쓰기 속도 제한을 둠:

`f3write --max-write-rate={{초당_kb}} {{경로/대상/마운트_포인트}}`
