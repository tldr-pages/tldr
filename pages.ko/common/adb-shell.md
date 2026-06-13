# adb shell

> 안드로이드 디버그 브릿지 쉘: 안드로이드 에뮬레이터 인스턴스 또는 연결된 안드로이드 장치에서 원격 쉘 명령을 실행.
> 더 많은 정보: <https://developer.android.com/tools/adb>.

- 에뮬레이터 또는 장치에서 원격 대화형 셸을 시작:

`adb shell`

- 에뮬레이터 또는 장치에서 모든 속성을 가져옴:

`adb shell getprop`

- 모든 런타임 권한을 기본 값으로 복구:

`adb shell pm reset-permissions`

- 애플리케이션에 대한 위험한 권한 취소:

`adb shell pm revoke {{패키지}} {{권한}}`

- 키보드 이벤트 트리거:

`adb shell input keyevent {{키코드}}`

- 에뮬레이터 또는 장치에서 애플리케이션 데이터 지우기:

`adb shell pm clear {{패키지}}`

- 에뮬레이터 또는 장치에서 액티비티 컴포넌트 시작:

`adb shell am start -n {{패키지}}/{{활동}}`

- 에뮬레이터 또는 기기에서 홈 액티비티 컴포넌트 시작:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
