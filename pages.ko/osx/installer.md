# installer

> 시스템 소프트웨어와 패키지를 지정한 도메인 또는 볼륨에 설치.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/installer.8.html>.

- 자세한 출력을 표시하고 Python 패키지를 루트 볼륨에 설치:

`sudo installer -verbose {{[-pkg|-package]}} {{경로/대상/python-버전.pkg}} {{[-tgt|-target]}} /`

- 대상 볼륨에 설치할 수 있는 패키지 목록 표시(`.mpkg`의 경우에는 하위 패키지) :

`installer -pkginfo {{[-pkg|-package]}} {{경로/대상/패키지.pkg}}`

- 패키지를 설치할 수 있는 볼륨 목록 표시:

`installer -volinfo {{[-pkg|-package]}} {{경로/대상/패키지.pkg}}`

- 패키지를 설치할 수 있는 도메인 목록 표시:

`installer -dominfo {{[-pkg|-package]}} {{경로/대상/패키지.pkg}}`

- 패키지의 설치 선택 사항을 XML로 생성:

`installer {{[-pkg|-package]}} {{경로/대상/패키지.pkg}} -showChoiceChangesXML`

- 명령줄 매개변수 대신 XML 설정 파일을 사용하여 패키지 설치:

`sudo installer {{[-pkg|-package]}} {{경로/대상/패키지.pkg}} -file {{경로/대상/설정-파일}}`
