# bundletool

> Android 애플리케이션 번들을 조작.
> `validate`와 같은 일부 하위 명0령에는 자체적인 사용법 문서가 존재.
> 더 많은 정보: <https://developer.android.com/tools/bundletool>.

- 하위 명령어에 대한 도움말 표시:

`bundletool help {{하위명령어}}`

- 애플리케이션 번들에서 APK를 생성 (키 저장소 비밀번호를 묻는 메시지 표시):

`bundletool build-apks --bundle {{경로/대상/bundle.aab}} --ks {{경로/대상/key.keystore}} --ks-key-alias {{key_alias}} --output {{경로/대상/file.apks}}`

- 키스토어 비밀번호를 제공하는 애플리케이션 번들에서 APK를 생성:

`bundletool build-apks --bundle {{경로/대상/bundle.aab}} --ks {{경로/대상/key.keystore}} --ks-key-alias {{key_alias}} --ks-pass {{pass:the_password}} --output {{경로/대상/file.apks}}`

- 보편적인 사용을 위해 단 하나의 단일 APK를 포함하는 APK 생성:

`bundletool build-apks --bundle {{경로/대상/bundle.aab}} --mode {{universal}} --ks {{경로/대상/key.keystore}} --ks-key-alias {{key_alias}} --output {{경로/대상/file.apks}}`

- 에뮬레이터나 기기에 올바른 APK 조합을 설치:

`bundletool install-apks --apks {{경로/대상/file.apks}}`

- 애플리케이션의 다운로드 크기를 측정:

`bundletool get-size total --apks {{경로/대상/file.apks}}`

- 에뮬레이터 또는 장치에 대한 장치 사양 JSON 파일을 생성:

`bundletool get-device-spec --output {{경로/대상/file.json}}`

- 번들을 확인하고 이에 대한 자세한 정보를 표시:

`bundletool validate --bundle {{경로/대상/bundle.aab}}`
