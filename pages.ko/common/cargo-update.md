# cargo update

> `Cargo.lock`에 기록된 종속성을 업데이트.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-update.html>.

- `Cargo.lock`의 종속성을 가능한 최신버전으로 업데이트함:

`cargo update`

- 업데이트될 내용을 표시하지만, 실제로 잠금 파일을 작성하지는 않음:

`cargo update --dry-run`

- 지정된 종속성만 업데이트함:

`cargo update --package {{의존성1}} --package {{의존성2}} --package {{의존성3}}`

- 특정 버전에 대한 특정 종속성을 설정:

`cargo update --package {{의존성}} --precise {{1.2.3}}`
