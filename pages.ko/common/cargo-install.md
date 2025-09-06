# cargo install

> Rust 바이너리를 빌드하고 설치.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-install.html>.

- <https://crates.io>에서 패키지를 설치 (버전은 선택사항 - 기본적으로 최신버전):

`cargo install {{패키지}}@{{버전}}`

- 지정된 Git 저장소에서 패키지를 설치:

`cargo install --git {{레포지토리_주소}}`

- Git 저장소에서 설치할 떄 지정된 분기/태그/커밋에서 빌드:

`cargo install --git {{레포지토리_주소}} --{{branch|tag|rev}} {{브랜치_이름|태그|커밋_해시}}`

- 설치된 모든 패키지와 해당 버전을 나열:

`cargo install --list`
