# cargo run

> 현재 Cargo 패키지를 실행.
> 참고: 실행된 바이너리의 작업 디렉터리는 현재 작업 디렉터리로 설정됨.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-run.html>.

- 기본 바이너리 타겟을 실행:

`cargo {{[r|run]}}`

- 지정된 바이너리를 실행:

`cargo {{[r|run]}} --bin {{이름}}`

- 지정된 예제를 실행:

`cargo {{[r|run]}} --example {{이름}}`

- 공백 또는 쉼표로 구분된 기능 목록을 활성화:

`cargo {{[r|run]}} {{[-F|--features]}} "{{기능1 기능2 ...}}"`

- 기본 기능을 비활성화:

`cargo {{[r|run]}} --no-default-features`

- 사용 가능한 모든 기능을 활성화:

`cargo {{[r|run]}} --all-features`

- 주어진 프로필로 실행:

`cargo {{[r|run]}} --profile {{이름}}`
