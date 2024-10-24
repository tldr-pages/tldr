# flutter pub

> Flutter 패키지 매니저.
> 참고: 패키지는 <https://pub.dev>에서 사용 가능. 참조: `flutter`.
> 더 많은 정보: <https://docs.flutter.dev/packages-and-plugins/using-packages>.

- `pubspec.yaml`에 지정된 모든 패키지를 다운로드/업데이트:

`flutter pub get`

- 앱에 패키지 종속성을 추가:

`flutter pub add {{패키지1 패키지2 ...}}`

- 앱에 패키지 종속성을 제거:

`flutter pub remove {{패키지1 패키지2 ...}}`

- `pubspec.yaml`에서 허용하는 가장 높은 버전의 패키지로 업그레이드:

`flutter pub upgrade {{패키지}}`
