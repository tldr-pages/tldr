# ppmpat

> 패턴을 사용하여 PPM 이미지를 생성.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmpat.html>.

- 지정된 패턴과 크기로 PPM 파일 생성:

`ppmpat -{{gingham2|gingham3|madras|tartan|poles|...}} {{너비}} {{높이}} > {{경로/대상/파일.ppm}}`

- 지정된 색상으로 위장 패턴의 PPM 파일 생성:

`ppmpat -camo -color {{색상1,색상2,...}} {{너비}} {{높이}} > {{경로/대상/파일.ppm}}`
