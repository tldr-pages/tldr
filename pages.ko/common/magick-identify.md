# magick identify

> 이미지 파일의 형식과 특성을 설명합니다.
> 같이 보기: `magick`.
> 더 많은 정보: <https://imagemagick.org/script/identify.php>.

- 이미지의 형식과 기본 특성 설명:

`magick identify {{경로/대상/이미지}}`

- 이미지의 형식과 자세한 특성 설명:

`magick identify -verbose {{경로/대상/이미지}}`

- 현재 디렉토리의 모든 JPEG 파일의 크기를 수집하여 CSV 파일에 저장:

`magick identify -format "{{%f,%w,%h\n}}" {{*.jpg}} > {{경로/대상/파일목록.csv}}`
