# gdisk

> GPT (GUID Partition Table) 디스크 파티션 관리 도구.
> 관련 항목: `cfdisk`, `fdisk`, `parted`.
> 더 많은 정보: <https://manned.org/gdisk>.

- 파티션 목록 표시:

`sudo gdisk {{[-l|--list]}}`

- 대화형 파티션 관리 도구 시작:

`sudo gdisk {{/dev/sdX}}`

- 도움말 메뉴 열기:

`<?>`

- 파티션([p]artition) 테이블 출력:

`<p>`

- 새로운([n]ew) 파티션 추가:

`<n>`

- 삭제할([d]elete) 파티션 선택:

`<d>`

- 파티션 테이블을 디스크에 저장([w]rite)하고 종료:

`<w>`

- 변경 사항을 저장하지 않고 종료([q]uit):

`<q>`
