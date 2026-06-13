# ufraw-batch

> 카메라의 RAW 파일을 표준 이미지 파일로 변환.
> 더 많은 정보: <https://manned.org/ufraw-batch>.

- RAW 파일을 JPEG로 변환:

`ufraw-batch --out-type=jpg {{입력_파일(들)}}`

- RAW 파일을 PNG로 변환:

`ufraw-batch --out-type=png {{입력_파일(들)}}`

- RAW 파일에서 미리보기 이미지 추출:

`ufraw-batch --embedded-image {{입력_파일(들)}}`

- 파일을 최대 크기 MAX1 및 MAX2로 저장:

`ufraw-batch --size=MAX1,MAX2 {{입력_파일(들)}}`
