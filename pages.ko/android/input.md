# input

> Android 기기에 이벤트 코드 또는 터치스크린 동작 보내기.
> 이 명령은 `adb shell`을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- 단일 문자의 이벤트 코드를 Android 기기로 보내기:

`input keyevent {{이벤트_코드}}`

- Android 기기로 문자 보내기 (`%s`는 공백을 나타냅니다):

`input text "{{텍스트}}"`

- Android 기기에 탭 한 번 보내기:

`input tap {{x축_위치}} {{y축_위치}}`

- Android 기기에 스와이프 동작 보내기:

`input swipe {{x축_시작}} {{y축_시작}} {{x축_끝}} {{y축_끝}} {{지속 시간(밀리초)}}`

- 스와이프 동작을 사용하여 Android 기기에 길게 누르기 보내기:

`input swipe {{x축_위치}} {{y축_위치}} {{x축_위치}} {{y축_위치}} {{지속 시간(밀리초)}}`
