# kdesrc-build

> KDE 구성 요소를 소스 저장소에서 손쉽게 빌드.
> 더 많은 정보: <https://docs.kde.org/trunk5/en/kdesrc-build/kdesrc-build/index.html>.

- `kdesrc-build` 초기화:

`kdesrc-build --initial-setup`

- KDE 구성 요소와 그 의존성을 소스에서 컴파일:

`kdesrc-build {{구성_요소_이름}}`

- 로컬 코드 업데이트 없이, 의존성 컴파일 없이 구성 요소 컴파일:

`kdesrc-build --no-src --no-include-dependencies {{구성_요소_이름}}`

- 컴파일 전에 빌드 디렉토리 새로고침:

`kdesrc-build --refresh-build {{구성_요소_이름}}`

- 특정 의존성에서 컴파일 재개:

`kdesrc-build --resume-from {{의존성_구성_요소}} {{구성_요소_이름}}`

- 지정된 실행 파일 이름으로 구성 요소 실행:

`kdesrc-build --run --exec {{실행_파일_이름}} {{구성_요소_이름}}`

- 모든 구성된 구성 요소 빌드:

`kdesrc-build`

- 빌드 실패 시 구성 요소 대신 시스템 라이브러리 사용:

`kdesrc-build --no-stop-on-failure {{구성_요소_이름}}`
