# ascii-image-converter

> 이미지를 ASCII 문자로 변환하는 도구.
> 더 많은 정보: <https://github.com/TheZoraiz/ascii-image-converter#cli-usage>.

- 이미지를 ASCII로 변환:

`ascii-image-converter {{경로/대상/이미지|주소}}`

- 출력에 색상 적용:

`ascii-image-converter {{[-C|--color]}} {{경로/대상/이미지|주소}}`

- braille를 사용하여 임계값 기반 이미지 생성 (이미지가 잘 보이지 않으면, 터미널 폰트 변경 시도) (braille - 시각장애인을 위한 점자 문자 체계):

`ascii-image-converter {{[-b|--braille]}} {{경로/대상/이미지|주소}}`

- braille를 사용해 dithering된 이미지 생성 (이미지가 잘 보이지 않으면, 터미널 폰트 변경 시도) (dithering - 표현할 수 없는 색상이나 밝기를 작은 점 패턴으로 흉내내는 기법, braille - 시각장애인을 위한 점자 문자 체계):

`ascii-image-converter {{[-b|--braille]}} --dither {{경로/대상/이미지|주소}}`

- 이미지 색상을 반전하여 표시:

`ascii-image-converter {{[-Cn|--color --negative]}} {{경로/대상/이미지|주소}}`

- 더 다양한 문자 집합을 사용하여 이미지 표시 (정확도 향상 가능):

`ascii-image-converter {{[-c|--complex]}} {{경로/대상/이미지|주소}}`
