# boxes

> ASCII 아트 상자 그리기, 제거 및 복구
> 더 많은 정보: <https://boxes.thomasjensen.com>.

- 문자열 주위에 상자 그리기:

`echo "{{문자열}}" | boxes`

- 문자열에서 상자를 제거:

`echo "{{문자열}}" | boxes -r`

- 문자열 주위에 특정 디자인의 상자 그리기:

`echo "{{문자열}}" | boxes -d {{parchment}}`

- 너비가 10이고 높이가 5인 상자를 그리기:

`echo "{{문자열}}" | boxes -s {{10}}x{{5}}`

- 중앙에 텍스트가 있는 상자 그리기:

`echo "{{문자열}}" | boxes -a c`
