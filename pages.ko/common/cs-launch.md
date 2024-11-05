# cs launch

> 설치할 필요 없이 Maven 종속성에서 직접 이름으로 애플리케이션을 실행.
> 더 많은 정보: <https://get-coursier.io/docs/cli-launch>.

- 인수를 사용하여 특정 애플리케이션을 시작:

`cs launch {{애플리케이션_이름}} -- {{인수1 인수2 ...}}`

- 인수를 사용하여 특정 애플리케이션 버전을 시작:

`cs launch {{애플리케이션_이름}}:{{애플리케이션_버전}} -- {{인수1 인수2 ...}}`

- 주요 파일이 무엇인지 지정하는 애플리케이션의 특정 버전인 specLaunch를 실행, 인수를 사용하여 특정 애플리케이션 버전을 지정:

`cs launch {{그룹_아이디}}:{{아티팩트_아이디}}:{{아티팩트_버전}} --main-class {{경로/대상/메인_클래스_파일}}`

- 특정 Java 옵션 및 JVM 메모리 옵션을 사용하여 애플리케이션을 시작:

`cs launch --java-opt {{-Doption_name1:option_value1 -Doption_name2:option_value2 ...}} --java-opt {{-Xjvm_option1 -Xjvm_option2 ...}} {{애플리케이션_이름}}`
