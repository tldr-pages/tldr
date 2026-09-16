# passage

> 비밀번호 또는 기타 민감한 데이터를 저장하고 있음.
> 참고: 모든 데이터는 age로 암호화됨 (`pass`에서 사용하는 GPG와 다름).
> 관련 항목: `pass`.
> 더 많은 정보: <https://github.com/FiloSottile/passage>.

- 새로운 비밀번호 입력 (`<Ctrl d>`를 새로운 줄에서 눌러 입력을 완료):

`passage insert {{[-m|--multiline]}} {{경로/대상/데이터}}`

- `stdin`에서 새로운 비밀번호 입력:

`echo "{{비밀번호}}" | passage insert {{[-e|--echo]}} {{경로/대상/데이터}}`

- 비밀번호 표시:

`passage {{경로/대상/데이터}}`

- 비밀번호를 클립보드에 복사:

`passage {{[-c|--clip]}} {{경로/대상/데이터}}`

- 전체 저장소 트리 표시:

`passage ls`

- 지정한 길이의 무작위 비밀번호 생성:

`passage generate {{경로/대상/데이터}} {{길이}}`

- 항목 편집:

`passage edit {{경로/대상/데이터}}`

- 항목 삭제:

`passage rm {{경로/대상/데이터}}`
