# fprintd-enroll

> 지문을 데이터베이스에 등록합니다.
> 더 많은 정보: <https://manned.org/fprintd-enroll>.

- 현재 사용자의 오른손 검지 지문 등록:

`fprintd-enroll`

- 현재 사용자의 특정 손가락 지문 등록:

`fprintd-enroll --finger {{왼쪽-엄지|왼쪽-검지|왼쪽-중지|왼쪽-약지|왼쪽-새끼|오른쪽-엄지|오른쪽-검지|오른쪽-중지|오른쪽-약지|오른쪽-새끼}}`

- 특정 사용자의 오른손 검지 지문 등록:

`fprintd-enroll {{사용자명}}`

- 특정 사용자의 특정 손가락 지문 등록:

`fprintd-enroll --finger {{손가락_이름}} {{사용자명}}`

- 도움말 표시:

`fprintd-enroll --help`
