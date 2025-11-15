# steghide

> JPEG, BMP, WAV 및 AU 파일 형식을 위한 스테가노그래피 도구.
> 더 많은 정보: <https://manned.org/steghide>.

- PNG에 데이터를 삽입하고 암호 구문을 입력받기:

`steghide embed {{[-cf|--coverfile]}} {{경로/대상/이미지.png}} {{[-ef|--embedfile]}} {{경로/대상/데이터.txt}}`

- WAV 오디오 파일에서 데이터 추출:

`steghide extract {{[-sf|--stegofile]}} {{경로/대상/소리.wav}}`

- 파일 정보 표시 및 삽입된 파일 탐지 시도:

`steghide info {{경로/대상/파일.jpg}}`

- JPEG 이미지에 최대 압축으로 데이터 삽입:

`steghide embed {{[-cf|--coverfile]}} {{경로/대상/이미지.jpg}} {{[-ef|--embedfile]}} {{경로/대상/데이터.txt}} {{[-z|--compress]}} {{9}}`

- 지원되는 암호화 알고리즘 및 모드 목록 확인:

`steghide encinfo`

- 예를 들어 Blowfish CBC 모드로 JPEG 이미지에 암호화된 데이터 삽입:

`steghide embed {{[-cf|--coverfile]}} {{경로/대상/이미지.jpg}} {{[-ef|--embedfile]}} {{경로/대상/데이터.txt}} {{[-e|--encryption]}} {{blowfish|...}} {{cbc|...}}`
