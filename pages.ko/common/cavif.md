# cavif

> PNG/JPEG 이미지를 AVIF로 변환함. Rust로 작성됨.
> 참고: `convert`.
> 더 많은 정보: <https://github.com/kornelski/cavif-rs>.

- JPEG 파일을 AVIF로 변환하여, `file.avif`에 저장:

`cavif {{경로/대상/image.jpg}}`

- 이미지를 품질을 조정하고 PNG 파일을 AVIF로 변환:

`cavif --quality {{1..100}} {{경로/대상/image.png}}`

- 출력 위치를 지정:

`cavif {{경로/대상/image.jpg}} --output {{경로/대상/output.avif}}`

- 이미 존재하는 경우, 대상 파일을 덮어씀:

`cavif --overwrite {{경로/대상/image.jpg}}`
