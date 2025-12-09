# cargo generate-lockfile

> 현재 패키지에 대한 `Cargo.lock` 파일을 생성. `cargo update`와 유사하지만, 옵션이 더 적음.
> 잠금 파일이 이미 존재하는 경우, 모든 패키지의 최신 버전으로 다시 빌드됨.
> 더 많은 정보: <https://doc.rust-lang.org/stable/cargo/commands/cargo-generate-lockfile.html>.

- 모든 패키지의 최신 버전으로 `Cargo.lock` 파일을 생성:

`cargo generate-lockfile`
