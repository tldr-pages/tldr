# svgr

> SVG를 React 컴포넌트로 변환.
> 더 많은 정보: <https://react-svgr.com/docs/options/>.

- SVG 파일을 React 컴포넌트로 변환하여 `stdout`으로 출력:

`svgr -- {{경로/대상/파일.svg}}`

- SVG 파일을 TypeScript를 사용하여 React 컴포넌트로 변환하여 `stdout`으로 출력:

`svgr --typescript -- {{경로/대상/파일.svg}}`

- SVG 파일을 JSX 변환을 사용하여 React 컴포넌트로 변환하여 `stdout`으로 출력:

`svgr --jsx-runtime automatic -- {{경로/대상/파일.svg}}`

- 디렉터리의 모든 SVG 파일을 특정 디렉터리의 React 컴포넌트로 변환:

`svgr --out-dir {{경로/대상/출력_폴더}} {{경로/대상/입력_폴더}}`

- 이미 변환된 파일을 건너뛰고 디렉터리의 모든 SVG 파일을 특정 디렉터리의 React 컴포넌트로 변환:

`svgr --out-dir {{경로/대상/출력_폴더}} --ignore-existing {{경로/대상/입력_폴더}}`

- 파일 이름에 특정 케이스를 사용하여 디렉터리의 모든 SVG 파일을 특정 디렉터리의 React 컴포넌트로 변환:

`svgr --out-dir {{경로/대상/출력_폴더}} --filename-case {{camel|kebab|pascal}} {{경로/대상/입력_폴더}}`

- 색인 파일을 생성하지 않고 디렉터리의 모든 SVG 파일을 특정 디렉터리의 React 컴포넌트로 변환:

`svgr --out-dir {{경로/대상/출력_폴더}} --no-index {{경로/대상/입력_폴더}}`
