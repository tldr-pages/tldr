# gnatprep

> Ada 소스 코드 파일용 전처리기 (GNAT 둩체인의 일부).
> 더 많은 정보: <https://gcc.gnu.org/onlinedocs/gnat_ugn/Preprocessing-with-gnatprep.html>.

- 파일에 정의된 심볼값을 사용:

`gnatprep {{소스_파일}} {{타겟_파일}} {{정의_파일}}`

- 명령줄에서 심볼 값을 직접 지정:

`gnatprep -D{{이름}}={{값}} {{소스_파일}} {{타겟_파일}}`
