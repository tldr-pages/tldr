# screenkey

> 키 입력을 화면에 표시하는 스크린캐스트 도구.
> 더 많은 정보: <https://www.thregr.org/~wavexx/software/screenkey/>.

- 현재 눌린 키를 화면에 표시:

`screenkey`

- 현재 눌린 키와 마우스 버튼을 화면에 표시:

`screenkey --mouse`

- screenkey의 설정 메뉴 실행:

`screenkey --show-settings`

- 특정 위치에 screenkey 실행:

`screenkey --position {{top|center|bottom|fixed}}`

- 화면에 표시되는 키 수정자의 형식 변경:

`screenkey --mods-mode {{normal|emacs|mac|win|tux}}`

- screenkey의 외관 변경:

`screenkey --bg-color "{{#a1b2c3}}" --font {{Hack}} --font-color {{yellow}} --opacity {{0.8}}`

- 화면에서 창을 드래그하여 screenkey 표시 위치 선택:

`screenkey --position fixed --geometry {{$(slop -n -f '%g')}}`
