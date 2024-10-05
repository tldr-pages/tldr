# cargo yank

> 색인에서 밀린 상자를 제거, 이 방법은 실수로 심하게 파손된 크레이트를 놓은 경우에만 사용해야 함.
> 참고: 데이터를 제거하지 않음. 크레이트는 가져온 후에도 여전히 존재, 새 프로젝트에서 상자를 사용하는 것을 방해할 뿐.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-yank.html>.

- 정해진 버전의 상자를 꺼냄:

`cargo yank {{크레이트}}@{{버전}}`

- 꺼내는 실행 취소 (i.e. 다시 다운로드 허용):

`cargo yank --undo {{크레이트}}@{{버전}}`

- 지정된 레지스트리를 사용 (레지스트리 이름은 구성에서 정의할 수 있음 - 기본값은 <https://crates.io>):

`cargo yank --registry {{이름}} {{크레이트}}@{{버전}}`