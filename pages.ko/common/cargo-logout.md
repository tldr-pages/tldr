# cargo logout

> 레지스트리에서 로컬로 API 토큰을 제거.
> 토큰은 패키지 레지스트리를 인증하는 데 사용됨. `cargo login`을 사용하여 다시 추가할 수 있음.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-logout.html>.

- 로컬 자격 증명 저장소 (`$CARGO_HOME/credentials.toml`에 위치)에서 API 토큰을 제거:

`cargo logout`

- 지정된 레지스트리를 사용 (레지스트리 이름은 구성에서 정의할 수 있음 - 기본값은 <https://crates.io>):

`cargo logout --registry {{이름}}`