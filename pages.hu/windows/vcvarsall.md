# vcvarsall

> A Microsoft Visual Studio eszközeinek parancssorból történő használatához szükséges környezeti változók beállítása. A `vcvarsall` elérési útvonalát egy adott Visual Studio telepítéshez a `vswhere` segítségével találja meg. További információ: <https://learn.microsoft.com/cpp/build/building-on-the-command-line>.

- Állítsa be a natív x64 környezetet:

`vcvarsall x64`

- Állítsa be a környezetet a keresztkompilált natív x86-os x64-es gazdaállomásról:

`vcvarsall x64_x86`

- A keresztkompilált natív Arm x64 környezet beállítása az x64 gazdaállomásról:

`vcvarsall x64_arm64`

- A környezet beállítása natív UWP x64 számára:

`vcvarsall x64 uwp`
