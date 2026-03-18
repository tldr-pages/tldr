# alr

> Ada 퍄키지 관리자.
> Ada 툴체인, 의존성, 도구 및 라이브러리를 관리.
> 더 많은 정보: <https://alire.ada.dev/docs/#first-steps>.

- 바이너리 또는 라이브러리 프로젝트를 생성:

`alr init {{--bin|--lib}} {{프로젝트_이름}}`

- 프로젝트에 의존성 추가:

`alr add {{크레이트}}`

- 컴파일된 바이너리 실행 (`build`를 먼저 실행할 필요 없음):

`alr run`

- 프로젝트 컴파일:

`alr build {{--release|--development|--validation}}`
