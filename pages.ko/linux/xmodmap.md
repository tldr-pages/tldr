# xmodmap

> X에서 키맵과 포인터 버튼 매핑을 수정하는 유틸리티.
> 더 많은 정보: <https://manned.org/xmodmap>.

- 포인터에서 `<LeftClick>`과 `<RightCLick>` 교체:

`xmodmap -e 'pointer = 3 2 1'`

- 키보드의 키를 다른 키로 재할당:

`xmodmap -e 'keycode {{키코드}} = {{키이름}}'`

- 키보드의 키 비활성화:

`xmodmap -e 'keycode {{키코드}} ='`

- 지정된 파일에 있는 모든 xmodmap 표현 실행:

`xmodmap {{경로/대상/파일}}`
