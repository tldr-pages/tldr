# lpmove

> 작업 또는 모든 작업을 다른 프린터로 이동.
> 같이 보기: `cancel`, `lp`, `lpr`, `lprm`.
> 더 많은 정보: <https://openprinting.github.io/cups/doc/man-lpmove.html>.

- 특정 작업을 `new_printer`로 이동:

`lpmove {{작업_ID}} {{new_printer}}`

- `old_printer`에서 `new_printer`로 작업 이동:

`lpmove {{old_printer}}-{{작업_ID}} {{new_printer}}`

- `old_printer`에서 `new_printer`로 모든 작업 이동:

`lpmove {{old_printer}} {{new_printer}}`

- 특정 서버에서 `new_printer`로 특정 작업 이동:

`lpmove -h {{서버}} {{작업_ID}} {{new_printer}}`
