# pamcomp

> 두 개의 PAM 이미지를 오버레이.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamcomp.html>.

- 오버레이가 아래 부분을 가리도록 두 이미지를 오버레이:

`pamcomp {{경로/대상/오버레이.pam}} {{경로/대상/언더레이.pam}} > {{경로/대상/출력.pam}}`

- 오버레이의 수평 정렬 설정:

`pamcomp -align {{left|center|right|beyondleft|beyondright}} -xoff {{수평_오프셋}} {{경로/대상/오버레이.pam}} {{경로/대상/언더레이.pam}} > {{경로/대상/출력.pam}}`

- 오버레이의 수직 정렬 설정:

`pamcomp -valign {{top|middle|bottom|above|below}} -yoff {{수직_오프셋}} {{경로/대상/오버레이.pam}} {{경로/대상/언더레이.pam}} > {{경로/대상/출력.pam}}`

- 오버레이의 불투명도 설정:

`pamcomp -opacity {{0.7}} {{경로/대상/오버레이.pam}} {{경로/대상/언더레이.pam}} > {{경로/대상/출력.pam}}`
