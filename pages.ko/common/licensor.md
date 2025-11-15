# licensor

> 라이선스를 `stdout`에 출력.
> 더 많은 정보: <https://github.com/raftario/licensor>.

- MIT 라이선스를 `LICENSE`라는 이름의 파일에 작성:

`licensor {{MIT}} > {{LICENSE}}`

- [p]laceholder 저작권 공지를 포함하여 MIT 라이선스를 `LICENSE`라는 이름의 파일에 작성:

`licensor -p {{MIT}} > {{LICENSE}}`

- Bobby Tables라는 저작권자를 지정:

`licensor {{MIT}} "{{Bobby Tables}}" > {{LICENSE}}`

- WITH 표현을 사용하여 라이선스 예외사항 지정:

`licensor "{{Apache-2.0 WITH LLVM-exception}}" > {{LICENSE}}`

- 사용 가능한 모든 라이선스 목록:

`licensor --licenses`

- 사용 가능한 모든 예외사항 목록:

`licensor --exceptions`
