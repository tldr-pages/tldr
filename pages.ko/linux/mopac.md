# mopac

> MOPAC (Molecular Orbital PACkage)는 Dewar 및 Thiel의 NDDO 근사를 기반으로 한 반경험적 양자 화학 프로그램입니다.
> 더 많은 정보: <https://github.com/openmopac/mopac>.

- 입력 파일(`.mop`, `.dat`, `.arc`)에 따라 계산 수행:

`mopac {{경로/대상/입력_파일}}`

- 현재 디렉토리에 기록하고 출력 파일을 스트리밍하는 HF의 최소 작업 예제:

`touch test.out; echo "PM7\n#comment\n\nH 0.95506 0.05781 -0.03133\nF 1.89426 0.05781 -0.03133" > test.mop; mopac test.mop & tail -f test.out`
