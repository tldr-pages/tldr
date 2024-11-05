# rage

> 간단하고 안전하며 현대적인 파일 암호화 도구(Rust 라이브러리 포함)로, 작은 명시적 키, 설정 옵션 없음, UNIX 스타일의 구성 가능성을 제공합니다.
> `age`의 Rust 구현.
> 더 많은 정보: <https://github.com/str4d/rage>.

- `user`를 위한 파일을 암호화하고 `message.age`로 저장:

`echo "{{당신의 비밀 메시지}}" | rage --encrypt --recipient {{user}} --output {{경로/대상/message.age}}`

- `identity_file`로 파일을 복호화하고 `message`로 저장:

`rage --decrypt --identity {{경로/대상/identity_file}} --output {{message}}`
