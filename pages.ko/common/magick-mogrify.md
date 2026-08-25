# magick mogrify

> 여러 이미지에 대해 크기 조정, 자르기, 뒤집기, 효과 적용 등 작업 수행.
> 변경 사항이 원본 파일에 직접 적용됨.
> 관련 항목: `magick`.
> 더 많은 정보: <https://imagemagick.org/script/mogrify.php>.

- 디렉터리 내 모든 JPEG 이미지를 원본 크기의 50%로 축소:

`magick mogrify -resize {{50%}} {{*.jpg}}`

- `DSC`로 시작하는 모든 이미지를 800x600 크기로 조정:

`magick mogrify -resize {{800x600}} {{DSC*}}`

- 디렉터리 내 모든 PNG를 JPEG로 변환:

`magick mogrify -format {{jpg}} {{*.png}}`

- 현재 디렉터리의 모든 이미지 채도를 절반으로 감소:

`magick mogrify -modulate {{100,50}} {{*}}`

- 현재 디렉터리의 모든 이미지 밝기를 2배로 증가:

`magick mogrify -modulate {{200}} {{*}}`

- GIF 이미지 품질을 낮춰 파일 크기를 감소:

`magick mogrify -layers 'optimize' -fuzz {{7%}} {{*.gif}}`

- 도움말 표시:

`magick mogrify -help`
