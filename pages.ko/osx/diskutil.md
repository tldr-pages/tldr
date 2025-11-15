# diskutil

> 로컬 디스크 및 볼륨을 관리하는 유틸리티.
> `partitiondisk`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- 현재 사용 가능한 모든 디스크, 파티션 및 마운트된 볼륨 나열:

`diskutil list`

- 볼륨의 파일 시스템 데이터 구조 복구:

`diskutil repairVolume {{/dev/디스크_장치}}`

- 볼륨 마운트 해제:

`diskutil unmountDisk {{/dev/디스크_장치}}`

- CD/DVD 꺼내기 (먼저 마운트 해제 필요):

`diskutil eject {{/dev/디스크_장치1}}`
