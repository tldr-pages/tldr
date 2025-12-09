# cargo search

> <https://crates.io>에서 패키지를 검색.
> 크레이트는 설명과 함께 `Cargo.toml`에 복사하기에 적합한 TOML 형식으로 표시됨.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-search.html>.

- 패키지 검색:

`cargo search {{쿼리}}`

- `n` 결과 표시 (기본값: 10, 최댓값: 100):

`cargo search --limit {{n}} {{쿼리}}`
