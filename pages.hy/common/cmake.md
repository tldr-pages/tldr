#cmmake

> Կառուցման ավտոմատացման միջպլատֆորմային համակարգ, որը ստեղծում է բնօրինակ կառուցման համակարգերի բաղադրատոմսեր:.
> Լրացուցիչ տեղեկություններ. <https://cmake.org/cmake/help/latest/manual/cmake.1.html>:.

- Ստեղծեք կառուցման բաղադրատոմս ընթացիկ գրացուցակում `CMakeLists.txt`-ով նախագծի գրացուցակից.:

`cmake {{path/to/project_directory}}`

- Օգտագործեք ստեղծված բաղադրատոմսը տվյալ գրացուցակում արտեֆակտներ ստեղծելու համար.:

`cmake --build {{path/to/build_directory}}`

- Տեղադրեք կառուցման արտեֆակտները `/usr/local/`-ում և շերտազերծեք վրիպազերծման նշանները՝:

`cmake --install {{path/to/build_directory}} --strip`

- Ստեղծեք կառուցման բաղադրատոմս, որի կառուցման տեսակը սահմանված է `Release` CMake փոփոխականով.:

`cmake {{path/to/project_directory}} -D CMAKE_BUILD_TYPE=Release`

- Ստեղծեք կառուցման բաղադրատոմս՝ օգտագործելով `generator_name` որպես հիմքում ընկած կառուցման համակարգ.:

`cmake -G {{generator_name}} {{path/to/project_directory}}`

- Տեղադրեք կառուցման արտեֆակտները՝ օգտագործելով երթուղիների հատուկ նախածանցը.:

`cmake --install {{path/to/build_directory}} --strip --prefix {{path/to/directory}}`

- Գործարկել հատուկ կառուցման թիրախ.:

`cmake --build {{path/to/build_directory}} {{[-t|--target]}} {{target_name}}`

- Ցուցադրել օգնությունը.:

`cmake {{[-h|--help]}}`
