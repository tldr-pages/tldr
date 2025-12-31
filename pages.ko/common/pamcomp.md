# pamcomp

> 두 개의 PAM 이미지를 오버레이.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamcomp.html>.

- 오버레이가 아래 부분을 가리도록 두 이미지를 오버레이:

`pamcomp {{경로/대상/오버레이.pam}} {{경로/대상/언더레이.pam}} > {{경로/대상/출력.pam}}`

- 오버레이의 수평 정렬 설정:

`pamcomp {{[-ali|-align]}} {{left|center|right|beyondleft|beyondright}} {{[-x|-xoff]}} {{수평_오프셋}} {{경로/대상/오버레이.pam}} {{경로/대상/언더레이.pam}} > {{경로/대상/출력.pam}}`

- 오버레이의 수직 정렬 설정:

`pamcomp {{[-va|-valign]}} {{top|middle|bottom|above|below}} {{[-y|-yoff]}} {{수직_오프셋}} {{경로/대상/오버레이.pam}} {{경로/대상/언더레이.pam}} > {{경로/대상/출력.pam}}`

- 오버레이의 불투명도 설정:

`pamcomp {{[-o|-opacity]}} {{0.7}} {{경로/대상/오버레이.pam}} {{경로/대상/언더레이.pam}} > {{경로/대상/출력.pam}}`
