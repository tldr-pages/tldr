# cargo bench

> 벤치마크를 컴파일하고 실행.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-bench.html>.

- 패키지의 모든 벤치마크를 실행:

`cargo bench`

- 벤치마크가 실패하더라도 중단하지 않음:

`cargo bench --no-fail-fast`

- 컴파일하지만, 벤치마크를 실행하지 않음:

`cargo bench --no-run`

- 지정된 벤치마크를 벤치마킹:

`cargo bench --bench {{벤치마크}}`

- 주어진 프로필을 사용한 벤치마크 (기본값: `bench`):

`cargo bench --profile {{프로필}}`

- 모든 예시 타겟을 벤치마킹:

`cargo bench --examples`

- 모든 바이너리 타겟을 벤치마킹:

`cargo bench --bins`

- 패키지 라이브러리를 벤치마킹:

`cargo bench --lib`
