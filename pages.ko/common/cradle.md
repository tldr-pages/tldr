# cradle

> Cradle PHP 프레임워크.
> `install`, `package`와 같은 일부 하위 명령어는 별도의 사용법 문서를 제공.
> 더 많은 정보: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html>.

- Cradle 구성 요소를 설치 (추가 정보를 입력하라는 메시지가 표시됨):

`cradle install`

- 강제로 설치하고 기존 파일을 덮어씀:

`cradle install {{[-f|--force]}}`

- 원격 서버에 연결 (`config/deploy.php` 참조):

`cradle connect {{서버_이름}}`

- 현재 Cradle 설정을 표시:

`cradle config show`

- 현재 Cradle 인스턴스에 패키지를 설치:

`cradle package install {{패키지_이름}}`

- 설치된 패키지 목록 표시:

`cradle package list`

- 도움말 표시:

`cradle help`

- 버전 표시:

`cradle --version`
