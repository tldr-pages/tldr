# dart

> Dart 프로젝트 관리.
> 더 많은 정보: <https://dart.dev/tools/dart-tool>.

- 같은 이름의 디렉터리에서 새로운 Dart 프로젝트를 초기화:

`dart create {{프로젝트_이름}}`

- Dart 파일 실행:

`dart run {{경로/대상/파일.dart}}`

- 현재 프로젝트에 대한 종속성을 다운로드:

`dart pub get`

- 현재 프로젝트에 대한 단위 테스트를 실행:

`dart test`

- null 안정성을 지원하도록 오래된 프로젝트의 의존성을 업데이트:

`dart pub upgrade --null-safety`

- Dart 파일을 기본 바이너리로 컴파일:

`dart compile exe {{경로/대상/파일.dart}}`

- 현재 프로젝트에 자동 수정 사항을 적용:

`dart fix --apply`
