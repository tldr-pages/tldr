# cargo owner

> 레지스트리에서 크레이트의 소유자를 관리.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-owner.html>.

- 특정 사용자나 팀을 소유자로 초대:

`cargo owner --add {{사용자명|github:조직_이름:팀_이름}} {{크레이트}}`

- 지정된 사용자 또는 팀을 소유자로 제거:

`cargo owner --remove {{사용자명|github:조직_이름:팀_이름}} {{크레이트}}`

- 크레이트 소유자 목록:

`cargo owner --list {{크레이트}}`

- 지정된 레지스트리를 사용 (레지스트리 이름은 구성에서 정의할 수 있음 - 기본값은 <https://crates.io>):

`cargo owner --registry {{이름}}`
