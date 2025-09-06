# f3fix

> 가짜 플래시 드라이브의 파티션 테이블 편집.
> 참고: `f3probe`, `f3write`, `f3read`.
> 더 많은 정보: <https://oss.digirati.com.br/f3/>.

- 실제 용량과 일치하는 단일 파티션으로 가짜 플래시 드라이브를 채우기:

`sudo f3fix {{/dev/장치_이름}}`

- 파티션을 부팅 가능한 것으로 표시:

`sudo f3fix --boot {{/dev/장치_이름}}`

- 파일 시스템을 지정:

`sudo f3fix --fs-type={{파일시스템_타입}} {{/dev/장치_이름}}`
