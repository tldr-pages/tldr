# filebrowser

> 파일 또는 디렉터리를 관리할 수 있는 간단한 HTTP 웹 서버.
> 더 많은 정보: <https://filebrowser.org/cli/filebrowser.html>.

- 현재 디렉터리를 기준으로 서버 실행:

`filebrowser`

- 특정 디렉터리를 기준으로 서버 실행:

`filebrowser {{[-r|--root]}} {{경로/대상/디렉터리}}`

- 호스트 주소 (기본값: `127.0.0.1`)와 포트(기본값: `8080`) 지정:

`filebrowser {{[-a|--address]}} {{host}} {{[-p|--port]}} {{port}} {{[-r|--root]}} {{경로/대상/디렉터리}}`

- 설정 파일과 데이터베이스 위치를 지정 (기본값: 현재 디렉터리의  `filebrowser.db`파일):

`filebrowser {{[-c|--config]}} {{경로/대상/파일}} {{[-d|--database]}} {{경로/대상/데이터베이스.db}} {{[-r|--root]}} {{경로/대상/디렉터리}}`

- 초기 관리자 계정의 사용자명 및 비밀번호 설정 (기본값: `admin`):

`filebrowser --username {{사용자명}} --password {{비밀번호}} {{[-r|--root]}} {{경로/대상/디렉터리}}`

- 이미지 썸네일 생성 시 사용할 프로세서 수 설정 (기본값: `4`):

`filebrowser --img-processors {{4}} {{[-r|--root]}} {{경로/대상/디렉터리}}`

- 이미지 썸네일 생성과 Command Runner 기능을 비활성화하여, 애플리케이션 내부에서 호스팅된 스크립트 파일 실행을 제한:

`filebrowser --disable-exec --disable-thumbnails {{[-r|--root]}} {{경로/대상/디렉터리}}`

- 이미지 미리보기 리사이즈 및 파일 헤더 기반 타입 감지 비활성화:

`filebrowser --disable-preview-resize --disable-type-detection-by-header {{[-r|--root]}} {{경로/대상/디렉터리}}`
