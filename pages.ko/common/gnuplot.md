# gnuplot

> 다양한 포맷으로 출력하는 그래프 플로터.
> 더 많은 정보: <https://manned.org/gnuplot>.

- 대화형 그래프 플로팅 쉘을 시작:

`gnuplot`

- 지정된 그래프 정의 파일에 대한 그래프를 그림:

`gnuplot {{경로/대상/정의파일.plt}}`

- 정의 파일을 로드하기 전에 명령을 실행하여 출력 형식을 설정:

`gnuplot -e "{{set output "경로/대상/파일이름.png" size 1024,768}}" {{경로/대상/정의파일.plt}}`

- gnuplot이 종료된 후에도 그래프 플롯 미리보기 창을 유지:

`gnuplot --persist {{경로/대상/정의파일.plt}}`
