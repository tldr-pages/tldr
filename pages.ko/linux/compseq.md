# compseq

> 시퀀스 내 고유 단어의 구성을 계산합니다.
> 더 많은 정보: <https://www.bioinformatics.nl/cgi-bin/emboss/help/compseq/>.

- FASTA [f]파일에서 단어의 관찰 빈도를 계산하고, 대화형 프롬프트로 매개 변수 값을 제공합니다:

`compseq {{경로/대상/파일.fasta}}`

- FASTA [f]파일에서 아미노산 쌍의 관찰 빈도를 계산하고, 출력 결과를 텍스트 [f]파일에 저장:

`compseq {{경로/대상/입력_단백질.fasta}} -word 2 {{경로/대상/출력_파일.comp}}`

- FASTA [f]파일에서 헥사뉴클레오타이드의 관찰 빈도를 계산하고, 출력 결과를 텍스트 [f]파일에 저장하며, 0의 빈도는 무시:

`compseq {{경로/대상/입력_DNA.fasta}} -word 6 {{경로/대상/출력_파일.comp}} -nozero`

- 특정 읽기 프레임에서 코돈의 관찰 빈도를 계산하고, 중복 카운트를 무시 (즉, 단어 길이 3만큼 창을 이동):

`compseq -sequence {{경로/대상/입력_RNA.fasta}} -word 3 {{경로/대상/출력_파일.comp}} -nozero -frame {{1}}`

- 3 위치만큼 프레임이 이동된 코돈의 관찰 빈도를 계산하고, 중복 카운트를 무시 (첫 번째 코돈 제외 모든 코돈을 보고해야 함):

`compseq -sequence {{경로/대상/입력_RNA.fasta}} -word 3 {{경로/대상/출력_파일.comp}} -nozero -frame 3`

- FASTA [f]파일에서 아미노산 삼중체를 계산하고, 이전에 실행된 `compseq`와 비교하여 예상 및 정규화된 빈도 값을 계산:

`compseq -sequence {{경로/대상/인간_프로테옴.fasta}} -word 3 {{경로/대상/출력_파일1.comp}} -nozero -infile {{경로/대상/출력_파일2.comp}}`

- 준비된 파일 없이 위 명령을 근사치로 계산하고, 제공된 입력 시퀀스의 단일 염기/잔기 빈도를 사용하여 예상 빈도를 계산:

`compseq -sequence {{경로/대상/인간_프로테옴.fasta}} -word 3 {{경로/대상/출력_파일.comp}} -nozero -calcfreq`

- 도움말 표시 (`-help -verbose`로 관련 및 일반 한정자에 대한 추가 정보 표시):

`compseq -help`
