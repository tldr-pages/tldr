# aapt

> Android Asset Packaging Tool.
> 안드로이드 앱의 소스를 컴파일하고 패키징합니다.
> 더 많은 정보: <https://elinux.org/Android_aapt>.

- APK 아카이브에 포함된 파일 나열:

`aapt list {{경로/app.apk}}`

- 앱의 메타데이타 출력 (버전, 권한, 등등...):

`aapt dump badging {{경로/app.apk}}`

- 지정된 디렉토리에 새 APK 아카이브 생성:

`aapt package -F {{경로/app.apk}} {{디렉토리/의/경로}}`
