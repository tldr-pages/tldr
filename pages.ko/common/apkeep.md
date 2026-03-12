# apkeep

> 다양한 소스에서 APK 파일을 다운로드.
> 더 많은 정보: <https://github.com/EFForg/apkeep/blob/master/USAGE>.

- 지정한 디렉터리에 APK 파일을 다운로드:

`apkeep {{[-a|--app]}} {{com.example.application}} {{경로/대상/디렉토리}}`

- 다운로드 가능한 모든 버전을 표시:

`apkeep {{[-a|--app]}} {{com.example.application}} {{[-l|--list-versions]}} {{경로/대상/디렉토리}}`

- 다운로드할 스토어를 지정:

`apkeep {{[-a|--app]}} {{com.example.application}} {{[-d|--download-source]}} {{apk-pure|google-play|f-droid|huawei-app-gallery}} {{경로/대상/디렉토리}}`
