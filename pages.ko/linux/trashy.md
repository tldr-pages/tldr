# trashy

> Rust로 작성된 `rm` 및 `trash-cli`의 대안.
> 더 많은 정보: <https://github.com/oberblastmeister/trashy#usage>.

- 특정 파일을 휴지통으로 이동:

`trash {{경로/대상/파일}}`

- 특정 파일들을 휴지통으로 이동:

`trash {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 휴지통의 항목 나열:

`trash list`

- 휴지통에서 특정 파일 복원:

`trash restore {{파일}}`

- 휴지통에서 특정 파일 제거:

`trash empty {{파일}}`

- 휴지통에서 모든 파일 복원:

`trash restore --all`

- 휴지통에서 모든 파일 제거:

`trash empty --all`
