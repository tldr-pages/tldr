# fdroidcl

> ADB를 통해 연결된 장치의 F-Droid 앱을 관리.
> 더 많은 정보: <https://github.com/mvdan/fdroidcl>.

- F-Droid 색인을 가져옴:

`fdroidcl update`

- 애플리케이션에 대한 정보 표시:

`fdroidcl show {{앱_아이디}}`

- 애플리케이션의 APK 파일을 다운로드:

`fdroidcl download {{앱_아이디}}`

- 색인에서 앱 검색:

`fdroidcl search {{검색_패턴}}`

- 연결된 장치에 앱 설치:

`fdroidcl install {{앱_아이디}}`

- 저장소 추가:

`fdroidcl repo add {{저장소_이름}} {{url}}`

- 저장소 제거, 활성화 또는 비활성화:

`fdroidcl repo {{remove|enable|disable}} {{저장소_이름}}`
