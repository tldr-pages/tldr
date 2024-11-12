# idea

> JetBrains Java 및 Kotlin IDE.
> 더 많은 정보: <https://www.jetbrains.com/help/idea/working-with-the-ide-features-from-command-line.html>.

- IntelliJ IDEA에서 현재 디렉터리를 열기:

`idea {{경로/대상/디렉터리}}`

- IntelliJ IDEA에서 특정 파일이나 디렉터리를 열기:

`idea {{경로/대상/파일_또는_디렉터리}}`

- diff 뷰어를 열어 최대 3개의 파일을 비교해보기:

`idea diff {{경로/대상/파일1 경로/대상/파일2 경로/대상/선택적_파일3}}`

- 양방향 파일 병합을 수행하려면, 병합 대화상자를 열기:

`idea merge {{경로/대상/파일1}} {{경로/대상/파일2}} {{경로/대상/출력}}`

- 프로젝트에서 코드 검사를 실행:

`idea inspect {{경로/대상/프로젝트_디렉터리}} {{경로/대상/조사_프로파일}} {{경로/대상/출력}}`
