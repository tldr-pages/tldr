# vcpkg

> C/C++ գրադարանների փաթեթների կառավարիչ:.
> Նշում. Փաթեթները տեղադրված չեն համակարգում: Դրանք օգտագործելու համար դուք պետք է ասեք ձեր build համակարգին (օրինակ՝ CMake) օգտագործել `vckg`:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/vcpkg/>:.

- Ստեղծեք և ավելացրեք `libcurl` փաթեթը `vcpkg` միջավայրում՝:

`vcpkg install curl`

- Կառուցեք և ավելացրեք `zlib`՝ օգտագործելով `emscripten` գործիքաշարը՝:

`vcpkg install --triplet=wasm32-emscripten zlib`

- Փաթեթի որոնում.:

`vcpkg search {{pkg_name}}`

- Կազմաձևեք CMake նախագիծը `vcpkg` փաթեթներ օգտագործելու համար.:

`cmake -B build -DCMAKE_TOOLCHAIN_FILE={{path/to/vcpkg_install_directory}}/scripts/buildsystems/vcpkg.cmake`
