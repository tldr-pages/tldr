# adb shell pm

> Android 패키지 관리자 도구.
> 더 많은 정보: <https://developer.android.com/tools/adb>.

- 설치된 패키지 목록 출력:

`adb shell pm list packages`

- 지정한 경로의 app 패키지 설치:

`adb shell pm install /{{경로/대상/앱}}.apk`

- 기기에서 패키지 삭제:

`adb shell pm uninstall {{패키지}}`

- 특정 패키지의 모든 앱 데이터 삭제:

`adb shell pm clear {{패키지}}`

- 패키지 또는 컴포넌트 활성화:

`adb shell pm enable {{패키지_또는_클래스}}`

- 패키지 또는 컴포넌트 비활성화:

`adb shell pm disable-user {{패키지_또는_클래스}}`

- 애플리케이션에 권한 부여:

`adb shell pm grant {{패키지}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`

- 애플리케이션에서 권한 제거:

`adb shell pm revoke {{패키지}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`
