# cs install

> `cs`를 설치할 때 구성된 디렉터리에 애플리케이션 설치 (바이너리를 로드하려면 `.bash_profile`에 `$ eval "$(cs install --env)"` 명령을 추가).
> 더 많은 정보: <https://get-coursier.io/docs/cli-install>.

- 특정 애플리케이션 설치:

`cs install {{애플리케이션_이름}}`

- 특정 버전의 애플리케이션을 설치:

`cs install {{애플리케이션_이름}}:{{애플리케이션_버전}}`

- 특정 이름으로 애플리케이션 검색:

`cs search {{부분_애플리케이션_이름}}`

- 가능한 경우 특정 애플리케이션을 업데이트:

`cs update {{애플리케이션_이름}}`

- 설치된 모든 애플리케이션을 업데이트:

`cs update`

- 특정 애플리케이션 제거:

`cs uninstall {{애플리케이션_이름}}`

- 설치된 모든 애플리케이션 나열:

`cs list`

- 설치된 애플리케이션에 특정 Java 옵션을 전달:

`{{애플리케이션_이름}} {{-Jjava_option_name1=value1 -Jjava_option_name2=value2 ...}}`
