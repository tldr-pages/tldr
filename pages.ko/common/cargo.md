# cargo

> Rust 프로젝트 및 모듈 종속성(크레이트)을 관리.
> `build`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://doc.rust-lang.org/cargo>.

- 크레이트 검색:

`cargo search {{검색할_문자열}}`

- 바이너리 크레이트 설치:

`cargo install {{크레이트_이름}}`

- 설치된 바이너리 크레이트 나열:

`cargo install --list`

- 지정된 디렉터리(기본값은 현재 작업 디렉터리)에 새 바이너리 또는 라이브러리 Rust 프로젝트 생성:

`cargo init --{{bin|lib}} {{경로/대상/폴더}}`

- 현재 디렉터리의 `Cargo.toml`에 종속성 추가:

`cargo add {{종속성}}`

- 현재 디렉터리의 Rust 프로젝트를 릴리스 프로파일로 빌드:

`cargo {{[b|build]}} {{[-r|--release]}}`

- 야간 컴파일러를 사용하여 현재 디렉터리의 Rust 프로젝트 빌드 (`rustup` 필요):

`cargo +nightly {{[b|build]}}`

- 특정 스레드 수를 사용하여 빌드 (기본값은 논리적 CPU 수):

`cargo {{[b|build]}} --jobs {{스레드_수}}`
