# serialver

> 클래스의 serialVersionUID를 반환.
> 기본적으로 보안 관리자를 설정하지 않습니다.
> 더 많은 정보: <https://docs.oracle.com/en/java/javase/25/docs/specs/man/serialver.html>.

- 클래스의 serialVersionUID 표시:

`serialver {{클래스_이름들}}`

- 콜론으로 구분된 클래스 및 리소스 목록의 serialVersionUID 표시:

`serialver -classpath {{경로/대상/폴더}} {{클래스_이름1:클래스_이름2:...}}`

- Java 애플리케이션 런처의 참조 페이지에서 Java 가상 머신으로 특정 옵션 사용:

`serialver -Joption {{클래스_이름들}}`
