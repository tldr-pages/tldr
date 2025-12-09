# androguard

> 파이썬으로 작성된 안드로이드 애플리케이션 용 리버스 엔지니어링 도구입니다.
> 더 많은 정보: <https://github.com/androguard/androguard>.

- Android 앱 매니페스트 표시:

`androguard axml {{경로/대상/앱.apk}}`

- 앱 메타데이터(버전 및 앱 아이디) 표시:

`androguard apkid {{경로/대상/앱.apk}}`

- 앱에서 자바 코드를 디컴파일:

`androguard decompile {{경로/대상/앱.apk}} --output {{경로/대상/디렉터리}}`
