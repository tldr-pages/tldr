# growpart

> 디스크 또는 디스크 이미지의 파티션을 확장해 사용 가능한 공간을 모두 활용.
> 더 많은 정보: <https://github.com/canonical/cloud-utils>.

- `sdX`의 `n`번 파티션을 디스크의 끝 또는 다음 파티션 시작 지점까지 확장:

`growpart {{/dev/sdX}} {{n}}`

- 디스크 이미지의 `n`번 파티션을 확장할 때 적용될 변경 사항을 dry-run으로 표시:

`growpart {{[-N|--dry-run]}} /{{경로/대상/디스크.img}} {{n}}`
