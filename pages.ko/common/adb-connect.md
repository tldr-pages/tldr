# adb connect

> Android 기기에 무선으로 연결.
> 더 많은 정보: <https://developer.android.com/tools/adb>.

- Android 기기와 페어링 (IP 주소와 페어링 코드는 개발자 옵션에서 확인 가능):

`adb pair {{ip_주소}}:{{포트}}`

- Android 기기에 연결 (포트는 페어링 시 사용한 포트와 다름):

`adb connect {{ip_주소}}:{{포트}}`

- 기기 연결 해제:

`adb disconnect {{ip_주소}}:{{포트}}`
