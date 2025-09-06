# magick mogrify

> 여러 이미지에 대한 크기 조정, 자르기, 뒤집기, 효과 추가와 같은 작업 수행.
> 변경 사항은 원본 파일에 직접 적용됩니다.
> 같이 보기: `magick`.
> 더 많은 정보: <https://imagemagick.org/script/mogrify.php>.

- 디렉토리 내 모든 JPEG 이미지를 원래 크기의 50%로 조정:

`magick mogrify -resize {{50%}} {{*.jpg}}`

- `DSC`로 시작하는 모든 이미지를 800x600으로 조정:

`magick mogrify -resize {{800x600}} {{DSC*}}`

- 디렉토리 내 모든 PNG를 JPEG로 변환:

`magick mogrify -format {{jpg}} {{*.png}}`

- 현재 디렉토리의 모든 이미지 파일의 채도를 절반으로 줄이기:

`magick mogrify -modulate {{100,50}} {{*}}`

- 현재 디렉토리의 모든 이미지 파일의 밝기를 두 배로 증가:

`magick mogrify -modulate {{200}} {{*}}`
