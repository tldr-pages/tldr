# blahaj

> lolcat과 유사한 출력 컬러라이저, 다양한 플래그와 알록달록한 상어(blahaj)를 출력.
> 더 많은 정보: <https://codeberg.org/GeopJr/BLAHAJ>.

- 사용 가능한 플래그/색상 목록 확인:

`blahaj --flags`

- 기본 트랜스 색상으로 상어(blahaj) 출력:

`blahaj {{[-s|--shark]}}`

- 랜덤 플래그를 2배 크기로 출력:

`blahaj {{[-f|--flag]}} {{[-r|--random]}} {{[-m|--multiplier]}} 2`

- 텍스트 출력 명령 결과를 lesbian 색상으로 표시:

`{{cowsay "Hello, world"}} | blahaj {{[-c|--colors]}} lesbian`

- 텍스트를 문자 단위로 색상 적용하여 출력:

`echo "{{Hello, world}}" | blahaj {{[-i|--individual]}}`

- 텍스트 파일 내용을 단어 단위로, 배경 색상을 적용하여 출력:

`blahaj {{[-w|--words]}} {{[-b|--background]}} {{경로/대상/파일}}`
