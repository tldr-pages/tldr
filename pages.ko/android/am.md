# am

> Android 활동 관리자.
> 더 많은 정보: <https://developer.android.com/studio/command-line/adb#am>.

- 특정 활동 시작:

`am start -n {{com.android.settings/.Settings}}`

- 데이터와 함께 특정 활동 시작:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- 특정 액션과 카테고리와 일치하는 활동 시작:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- intent를 URI로 변환:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
