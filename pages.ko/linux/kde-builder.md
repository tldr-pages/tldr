# kde-builder

> 소스 저장소에서 KDE 구성 요소를 쉽게 빌드.
> `kdesrc-build`의 대체 도구.
> 더 많은 정보: <https://kde-builder.kde.org/en/cmdline/supported-cmdline-params.html>.

- `kde-builder` 초기 설정:

`kde-builder --initial-setup`

- KDE 구성 요소 및 의존성을 소스에서 컴파일:

`kde-builder {{구성_요소_이름}}`

- 로컬 코드를 업데이트하지 않고 의존성을 컴파일하지 않으며 구성 요소 컴파일:

`kde-builder --no-src --no-include-dependencies {{구성_요소_이름}}`

- 컴파일 전 빌드 디렉토리 [r]efresh:

`kde-builder --refresh-build {{구성_요소_이름}}`

- 특정 의존성부터 컴파일 재개:

`kde-builder --resume-from={{의존성_구성_요소}} {{구성_요소_이름}}`

- 지정된 실행 파일 이름으로 구성 요소 실행:

`kde-builder --run {{실행_파일_이름}}`

- 모든 구성된 구성 요소 빌드:

`kde-builder`

- 빌드 실패 시 구성 요소 대신 시스템 라이브러리 사용:

`kde-builder --no-stop-on-failure {{구성_요소_이름}}`
