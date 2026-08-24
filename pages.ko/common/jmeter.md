# jmeter

> 기능적 동작의 부하 테스트 및 성능 측정을 위해 설계된 오픈 소스 Java 애플리케이션.
> 더 많은 정보: <https://jmeter.apache.org/usermanual/get-started.html#options>.

- GUI 없이 특정 테스트 플랜 실행:

`jmeter {{[-n|--nongui]}} {{[-t|--testfile]}} {{경로/대상/파일.jmx}}`

- 특정 로그 파일을 사용하여 GUI 없이 테스트 플랜 실행:

`jmeter {{[-n|--nongui]}} {{[-t|--testfile]}} {{경로/대상/파일.jmx}} {{[-l|--logfile]}} {{경로/대상/로그파일.jtl}}`

- 특정 프록시를 사용하여 GUI 없이 테스트 플랜 실행:

`jmeter {{[-n|--nongui]}} {{[-t|--testfile]}} {{경로/대상/파일.jmx}} {{[-H-|--proxyHost]}} {{127.0.0.1}} {{[-P|--proxyPort]}} {{8888}}`

- 특정 JMeter 속성을 사용하여 GUI 없이 테스트 플랜 실행:

`jmeter {{[-n|--nongui]}} {{[-t|--testfile]}} {{경로/대상/파일.jmx}} {{[-J|--jmeterproperty]}} {{키}}='{{값}}'`
