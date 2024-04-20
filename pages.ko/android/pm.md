# pm

> Android 기기의 앱에 대한 정보 표시.
> 더 많은 정보: <https://developer.android.com/tools/adb#pm>.

- 설치된 모든 앱 나열:

`pm list packages`

- 설치된 모든 시스템 앱 나열:

`pm list packages -s`

- 설치된 모든 타사 앱 나열:

`pm list packages -3`

- 특정 키워드와 일치하는 앱 나열:

`pm list packages {{키워드1 키워드2 ...}}`

- 특정 앱의 APK 경로 표시:

`pm path {{애플리케이션}}`
