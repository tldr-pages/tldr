# boxes

> ASCII 아트 상자 그리기, 제거 및 복구
> 더 많은 정보: <https://boxes.thomasjensen.com/boxes-man-1.html>.

- 문자열 주위에 상자 그리기:

`echo "{{문자열}}" | boxes`

- 문자열에서 상자를 제거[r]:

`echo "{{문자열}}" | boxes -r`

- 문자열 주위에 특정 디자인[d]의 상자 그리기:

`echo "{{문자열}}" | boxes -d {{parchment}}`

- 상자 크기[s] 지정(열 단위):

`echo "{{문자열}}" | boxes -s {{10}}x{{5}}`

- 상자 텍스트 수평[h] 정렬[a](왼쪽[l], 중앙[c], 오른쪽[r]):

`echo "{{문자열}}" | boxes -a h{{l|c|r}}`

- 상자 텍스트 수직[v] 정렬[a](위쪽[t], 중앙[c], 아래쪽[b]):

`echo "{{문자열}}" | boxes -a v{{t|c|b}}`

- 상자 텍스트 양쪽 조정[j](왼쪽[l], 중앙[c], 오른쪽[r]):

`echo "{{문자열}}" | boxes -a j{{l|c|r}}{{vt}}`
