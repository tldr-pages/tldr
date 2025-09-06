# catimg

> 터미널에서 이미지 인쇄.
> 참고: `pixterm`, `chafa`.
> 더 많은 정보: <https://manned.org/catimg>.

- 터미널에 JPEG, PNG, GIF를 인쇄:

`catimg {{경로/대상/파일}}`

- 이미지 해상도([r]esolution)를 두 배로 늘림:

`catimg -r 2 {{경로/대상/파일}}`

- 더 나은 터미널([t]erminal) 지원을 위해 24비트 색상을 비활성화:

`catimg -t {{경로/대상/파일}}`

- 사용자 정의 너비([w]idth) 또는 높이([H]eight)를 지정:

`catimg {{-w|-H}} {{40}} {{경로/대상/파일}}`
