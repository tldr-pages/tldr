# adb install

> 안드로이드 디버그 브릿지 설치: 안드로이드 에뮬레이터 인스턴스 또는 연결된 안드로이드 장치에 패키지를 삽입.
> 더 많은 정보: <https://developer.android.com/tools/adb>.

- 에뮬레이터/장치에 안드로이드 애플리케이션 삽입:

`adb install {{경로/대상/파일.apk}}`

- 특정 에뮬레이터/장치에 안드로이드 애플리케이션 삽입 ( `$ANDROID_SERIAL`를 재정의):

`adb -s {{시리얼_번호}} install {{경로/대상/파일.apk}}`

- 데이터를 유지하면서, 기존 앱을 다시 설치([r]einstall):

`adb install -r {{경로/대상/파일.apk}}`

- 버전 코드 다운그레이드([d]owngrade)를 허용하는 안드로이드 애플리케이션 삽입(디버깅 가능한 패키지만 해당):

`adb install -d {{경로/대상/파일.apk}}`

- 애플리케이션 매니페스트에 나열된 모든 권한을 부여([g]rant):

`adb install -g {{경로/대상/파일.apk}}`

- 변경된 APK 부분만 업데이트하여, 설치된 패키지를 빠르게 업데이트:

`adb install --fastdeploy {{경로/대상/파일.apk}}`
