# cargo

> Rust 패키지 관리프로그램.
> Rust 프로젝트 및 해당 모듈 종속성(크레이트) 관리.
> 더 많은 정보: <https://doc.rust-lang.org/cargo>.

- 크레이트 검색:

`cargo search {{검색할_문자열}}`

- 크레이트 설치:

`cargo install {{크레이트_이름}}`

- 설치된 크레이트 목록:

`cargo install --list`

- 현재 디렉토리에 새 이진 또는 라이브러리 Rust 프로젝트 생성:

`cargo init --{{bin|lib}}`

- 지정된 디렉토리에 새 이진 또는 라이브러리 Rust 프로젝트 생성:

`cargo new {{경로/디렉토리}} --{{bin|lib}}`

- 현재 디렉토리에 Rust 프로젝트 구축:

`cargo build`

- 특정 쓰레드 수를 사용하여 구축(기본값은 CPU 코어 수):

`cargo build --jobs {{작업}}`
