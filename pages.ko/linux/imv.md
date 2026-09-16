# imv

> wayland와 X11을 지원하는 CLI 이미지 뷰어, tiling window manager에 최적화되어 있음.
> Photoshop (PSD)을 포함한 다양한 이미지 형식을 지원.
> 더 많은 정보: <https://sr.ht/~exec64/imv/>.

- 여러 이미지 보기:

`imv {{경로/대상/이미지1.ext 경로/대상/이미지2.ext ...}}`

- 전체 화면 모드로 이미지 보기:

`imv -f {{경로/대상/이미지.ext}}`

- 지정한 디렉터리의 이미지를 재귀적으로([r]ecursively) 탐색하여 슬라이드 쇼 실행:

`imv -r --slideshow {{경로/대상/디렉터리}}`

- `stdin`으로 전달된 여러 이미지 보기:

`find . -type f -name "{{*.svg}}" | imv`

- 디렉터리의 이미지를 10초 간격으로 슬라이드 쇼 실행:

`imv -t 10 {{경로/대상/디렉터리}}`

- 웹의 여러 이미지 보기:

`curl {{[-Osw|--remote-name --silent --write-out]}} '%{filename_effective}\n' '{{http://www.example.com/[1-10].jpg}}' | imv`
