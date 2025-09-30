# dconf write

> dconf 데이터베이스에 키 값을 작성합니다.
> 같이 보기: `dconf`.
> 더 많은 정보: <https://manned.org/dconf>.

- 특정 키 값 작성:

`dconf write {{/경로/대상/키}} "{{값}}"`

- 특정 문자열 키 값 작성:

`dconf write {{/경로/대상/키}} "'{{문자열}}'"`

- 특정 정수 키 값 작성:

`dconf write {{/경로/대상/키}} "{{5}}"`

- 특정 불리언 키 값 작성:

`dconf write {{/경로/대상/키}} "{{true|false}}"`

- 특정 배열 키 값 작성:

`dconf write {{/경로/대상/키}} "[{{'첫번째', '두번째', ...}}]"`

- 특정 빈 배열 키 값 작성:

`dconf write {{/경로/대상/키}} "@as []"`
