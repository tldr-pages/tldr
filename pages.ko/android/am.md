# am

> Android 활동 관리자.
> 더 많은 정보: <https://developer.android.com/tools/adb#am>.

- 특정 패키지 이름([n]ame)과 컴포넌트를 지정해 액티비티 시작:

`am start -n {{com.android.settings/.Settings}}`

- 특정 인텐트 액션([a]ction)을 실행하고 데이터([d]ata) 전달:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- 특정 액션([a]ction)과 카테고리([c]ategory)에 일치하는 액티비티 시작:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- 인텐트를 URI 형식으로 변환:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- 에뮬레이터 또는 기기에서 홈 액티비티 시작:

`am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
