# trash

> 휴지통/재활용통 관리.
> 더 많은 정보: <https://github.com/andreafrancia/trash-cli>.

- 파일을 휴지통으로 보내기:

`trash {{경로/대상/파일}}`

- 휴지통에 있는 모든 파일 나열:

`trash-list`

- 휴지통에서 파일을 상호작용하며 복원:

`trash-restore`

- 휴지통 비우기:

`trash-empty`

- 휴지통에서 10일 이상 된 모든 파일을 영구 삭제:

`trash-empty 10`

- 특정 블롭 패턴과 일치하는 휴지통의 모든 파일 제거:

`trash-rm "{{*.o}}"`

- 특정 원래 위치의 모든 파일 제거:

`trash-rm {{/경로/대상/파일_또는_폴더}}`
