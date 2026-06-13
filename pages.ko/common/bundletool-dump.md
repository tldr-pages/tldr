# bundletool dump

> Android 애플리케이션 번들을 조작.
> 더 많은 정보: <https://developer.android.com/tools/bundletool>.

- 기본 모듈의 `AndroidManifest.xml`을 표시:

`bundletool dump manifest --bundle {{경로/대상/bundle.aab}}`

- XPath를 사용해 `AndroidManifest.xml`의 특정 값을 표시:

`bundletool dump manifest --bundle {{경로/대상/bundle.aab}} --xpath {{/manifest/@android:versionCode}}`

- 특정 모듈의 `AndroidManifest.xml`을 표시:

`bundletool dump manifest --bundle {{경로/대상/bundle.aab}} --module {{이름}}`

- 애플리케이션 번들의 모든 리소스를 표시:

`bundletool dump resources --bundle {{경로/대상/bundle.aab}}`

- 특정 리소스에 대한 구성을 표시:

`bundletool dump resources --bundle {{경로/대상/bundle.aab}} --resource {{type/name}}`

- ID를 사용하여 특정 리소스에 대한 구성 및 값을 표시:

`bundletool dump resources --bundle {{경로/대상/bundle.aab}} --resource {{0x7f0e013a}} --values`

- 번들 구성 파일의 내용을 표시:

`bundletool dump config --bundle {{경로/대상/bundle.aab}}`
