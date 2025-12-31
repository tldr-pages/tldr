# winicontopam

> Windows ICO 파일을 PAM 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/winicontopam.html>.

- ICO 파일을 읽고 그 안에 포함된 최고 품질의 이미지를 PAM 형식으로 변환:

`winicontopam {{경로/대상/입력_파일.ico}} > {{경로/대상/출력.pam}}`

- 입력 파일의 모든 이미지를 PAM으로 변환:

`winicontopam {{[-al|-allimages]}} {{경로/대상/입력_파일.ico}} > {{경로/대상/출력.pam}}`

- 입력 파일의 n번째 이미지를 PAM으로 변환:

`winicontopam {{[-i|-image]}} {{n}} {{경로/대상/입력_파일.ico}} > {{경로/대상/출력.pam}}`

- 추출할 이미지가 그라데이션 투명 데이터와 AND 마스크를 포함하는 경우, 출력 PAM 파일의 다섯 번째 채널에 AND 마스크를 작성:

`winicontopam {{[-an|-andmasks]}} {{경로/대상/입력_파일.ico}} > {{경로/대상/출력.pam}}`
