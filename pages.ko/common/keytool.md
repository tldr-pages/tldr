# keytool

> Java에 포함된 인증서 관리 도구.
> 더 많은 정보: <https://docs.oracle.com/en/java/javase/25/docs/specs/man/keytool.html>.

- 키스토어 생성:

`keytool -genkeypair -v -keystore {{경로/대상/파일.keystore}} -alias {{키_이름}}`

- 키스토어 비밀번호 변경:

`keytool -storepasswd -keystore {{경로/대상/파일.keystore}}`

- 특정 키스토어 내 키의 비밀번호 변경:

`keytool -keypasswd -alias {{키_이름}} -keystore {{경로/대상/파일.keystore}}`
