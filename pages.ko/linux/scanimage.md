# scanimage

> Scanner Access Now Easy API를 사용하여 이미지를 스캔.
> 더 많은 정보: <http://sane-project.org/man/scanimage.1.html>.

- 사용 가능한 스캐너를 나열하여 대상 장치가 연결되고 인식되었는지 확인:

`scanimage -L`

- 이미지를 스캔하여 파일로 저장:

`scanimage --format={{pnm|tiff|png|jpeg}} > {{경로/대상/새_이미지}}`
