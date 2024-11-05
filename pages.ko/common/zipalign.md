# zipalign

> Zip 아카이브 정렬 도구.
> Android SDK 빌드 도구의 일부.
> 더 많은 정보: <https://developer.android.com/tools/zipalign>.

- Zip 파일의 데이터를 4바이트 경계에 맞춰 정렬:

`zipalign {{4}} {{경로/대상/입력.zip}} {{경로/대상/출력.zip}}`

- Zip 파일이 4바이트 경계에 맞게 올바르게 정렬되었는지 확인하고 결과를 자세히 표시:

`zipalign -v -c {{4}} {{경로/대상/입력.zip}}`
