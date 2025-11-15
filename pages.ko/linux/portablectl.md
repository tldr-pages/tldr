# portablectl

> Linux 시스템에서 포터블 서비스 이미지를 관리하고 배포하기 위한 systemd 유틸리티.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/portablectl.html>.

- 포터블 이미지 검색 경로에서 발견된 사용 가능한 포터블 서비스 이미지 나열:

`portablectl list`

- 호스트 시스템에 포터블 서비스 이미지 연결:

`portablectl attach {{경로/대상/이미지}}`

- 호스트 시스템에서 포터블 서비스 이미지 연결 해제:

`portablectl detach {{경로/대상/이미지|이미지_이름}}`

- 지정된 포터블 서비스 이미지의 세부 정보 및 메타데이터 표시:

`portablectl inspect {{경로/대상/이미지}}`

- 포터블 서비스 이미지가 호스트 시스템에 연결되어 있는지 확인:

`portablectl is-attached {{경로/대상/이미지|이미지_이름}}`
