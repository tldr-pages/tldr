# e2freefrag

> ext2/ext3/ext4 파일시스템의 여유 공간 조각화 정보를 출력합니다.
> 더 많은 정보: <https://manned.org/e2freefrag>.

- 연속적이고 정렬된 여유 공간으로 존재하는 여유 블록 수 확인:

`e2freefrag {{/dev/sdXN}}`

- 청크 크기를 킬로바이트 단위로 지정하여 사용 가능한 여유 청크 수 출력:

`e2freefrag -c {{청크_크기_kb}} {{/dev/sdXN}}`
