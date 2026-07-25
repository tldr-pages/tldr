# fsadm

> 장치 파일 시스템을 검사하거나 크기를 조정.
> 더 많은 정보: <https://manned.org/fsadm>.

- 파일 시스템 오류 검사:

`fsadm check {{/dev/vg_name/lv_name}}`

- 지정한 크기로 파일 시스템 크기 조정을 dry-run으로 수행 (실제 변경은 없음):

`fsadm {{[-n|--dry-run]}} resize {{/dev/vg_이름/lv_이름}} {{10G}}`

- 파일 시스템을 장치 전체 크기로 확장 (크기 지정 생략):

`fsadm resize {{/dev/vg_이름/lv_이름}}`

- 파일 시스템과 기반 논리 볼륨을 함께 크기 조정:

`fsadm {{[-l|--lvresize]}} resize {{/dev/vg_이름/lv_이름}} {{100G}}`

- ext2/3/4 파일 시스템을 오프라인 상태(마운트 해제)에서 크기 조정:

`fsadm {{[-e|--ext-offline]}} resize {{/dev/vg_이름/lv_이름}} {{20G}}`