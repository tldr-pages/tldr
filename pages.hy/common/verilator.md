# ստուգաբան

> Վերափոխեք Verilog-ը և SystemVerilog ապարատային նկարագրության լեզուն (HDL) դիզայնը C++ կամ SystemC մոդելի, որը կկատարվի կազմելուց հետո:.
> Լրացուցիչ տեղեկություններ. <https://veripool.org/guide/latest/>:.

- Ստեղծեք որոշակի C նախագիծ ընթացիկ գրացուցակում.:

`verilator --binary --build-jobs 0 -Wall {{path/to/source.v}}`

- Ստեղծեք C++ գործարկվող հատուկ թղթապանակում.:

`verilator --cc --exe --build --build-jobs 0 -Wall {{path/to/source.cpp}} {{path/to/output.v}}`

- Ընթացիկ գրացուցակում գտնվող կոդի վրայի ներդիր.:

`verilator --lint-only -Wall`

- Ստեղծեք XML ելք դիզայնի մասին (ֆայլեր, մոդուլներ, օրինակների հիերարխիա, տրամաբանություն և տվյալների տեսակներ)՝ այլ գործիքների մեջ սնվելու համար.:

`verilator --xml-output -Wall {{path/to/output.xml}}`
