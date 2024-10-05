# cargo fetch

> 네트워크에서 패키지의 종속성을 가져옴.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-fetch.html>.

- `Cargo.lock`에 지정된 종속성 가져오기 (모든 대상에 대해):

`cargo fetch`

- 지정된 대상에 대한 종속성을 가져옴:

`cargo fetch --target {{타겟_아키텍처_정보}}`
