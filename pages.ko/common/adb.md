# adb

> 안드로이드 디버그 브릿지: 안드로이드 에뮬레이터 객체 또는 연결된 안드로이드 장치와 통신.
> 더 많은 정보: <https://developer.android.com/studio/command-line/adb>.

- adb 서버 프로세스가 실행되고 있고, 시작하는지 확인:

`adb start-server`

- adb 서버 프로세스 종료:

`adb kill-server`

- 대상 에뮬레이터/장치 객체에서 원격 쉘 시작:

`adb shell`

- 안드로이드 애플리케이션을 에뮬레이터/장치로 푸쉬:

`adb install -r {{path/to/file.apk}}`

- 대상 장치에서부터 파일/디렉토리를 복사:

`adb pull {{path/to/device_file_or_directory}} {{path/to/local_destination_directory}}`

- 대상 장치로 파일/디렉토리 복사:

`adb push {{path/to/local_file_or_directory}} {{path/to/device_destination_directory}}`

- 연결된 장치들의 목록 가져오기:

`adb devices`
