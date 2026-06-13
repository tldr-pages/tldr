# tune2fs

> ext2, ext3 또는 ext4 파일 시스템의 매개변수를 조정합니다.
> 마운트된 파일 시스템에서도 사용할 수 있습니다.
> 더 많은 정보: <https://manned.org/tune2fs>.

- 파일 시스템이 검사되기 전 최대 횟수를 2로 설정:

`tune2fs -c {{2}} {{/dev/sdXN}}`

- 파일 시스템 레이블을 MY_LABEL로 설정:

`tune2fs -L {{'MY_LABEL'}} {{/dev/sdXN}}`

- 파일 시스템에 대해 디스카드 및 사용자 지정 확장 속성을 활성화:

`tune2fs -o {{discard,user_xattr}} {{/dev/sdXN}}`

- 파일 시스템에 저널링 활성화:

`tune2fs -o^{{nobarrier}} {{/dev/sdXN}}`
