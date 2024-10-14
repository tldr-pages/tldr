# vcvarsall

> Microsoft Visual Studio 도구를 사용하기 위해 필요한 환경 변수를 설정합니다.
> 특정 Visual Studio 설치에 대한 `vcvarsall` 경로는 `vswhere`를 사용하여 찾을 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/cpp/build/building-on-the-command-line>.

- 네이티브 x64 환경 설정:

`vcvarsall x64`

- x64 호스트에서 네이티브 x86 크로스 컴파일 환경 설정:

`vcvarsall x64_x86`

- x64 호스트에서 네이티브 Arm x64 크로스 컴파일 환경 설정:

`vcvarsall x64_arm64`

- 네이티브 UWP x64 환경 설정:

`vcvarsall x64 uwp`
