# installpkg

> Install a Slackware 패키지 설치.
> 더 많은 정보: <https://www.slackbook.org/html/book.html#PACKAGE-MANAGEMENT-PACKAGE-UTILITIES-INSTALLPKG>.

- 패키지 설치:

`sudo installpkg {{경로/대상/패키지.tgz}}`

- 설치를 시뮬레이션하고 결과를 `stdout`으로 출력:

`installpkg -warn {{경로/대상/패키지.tgz}}`

- 현재 디렉터리와 하위 디렉터리의 내용으로 패키지 생성:

`installpkg -m {{패키지_이름.tgz}}`

- 현재 디렉터리와 하위 디렉터리의 내용을 지정한 이름의 패키지로 설치:

`sudo installpkg -r {{패키지_이름.tgz}}`
