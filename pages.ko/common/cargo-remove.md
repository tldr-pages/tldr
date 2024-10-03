# cargo remove

> Rust 프로젝트의 `Cargo.toml` 매니페스트에서 종속성을 제거.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-remove.html>.

- 현재 프로젝트에서 종속성을 제거:

`cargo remove {{종속성}}`

- 개발 또는 빌드 종속성을 제거:

`cargo remove --{{dev|build}} {{종속성}}`

- 특정 대상 플랫폼의 종속성을 제거:

`cargo remove --target {{타겟}} {{종속성}}`
