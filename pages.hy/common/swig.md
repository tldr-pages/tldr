# ճոճանակ

> Ստեղծեք կապեր C/C++ կոդի և բարձր մակարդակի տարբեր լեզուների միջև, ինչպիսիք են JavaScript-ը, Python-ը, C#-ը և այլն:.
> Այն օգտագործում է հատուկ `.i` կամ `.swg` ֆայլեր՝ կապեր ստեղծելու համար (C/C++ SWIG դիրեկտիվներով), այնուհետև թողարկում է C/C++ ֆայլ, որը պարունակում է ընդլայնման մոդուլ ստեղծելու համար անհրաժեշտ փաթաթման ծածկագիրը:.
> Լրացուցիչ տեղեկություններ. <https://www.swig.org/Doc4.4/SWIGDocumentation.html#SWIG_nn2>:.

- Ստեղծեք կապ C++-ի և Python-ի միջև.:

`swig -c++ -python -o {{path/to/output_wrapper.cpp}} {{path/to/swig_file.i}}`

- Ստեղծեք կապ C++-ի և Go-ի միջև.:

`swig -go -cgo -intgosize 64 -c++ {{path/to/swig_file.i}}`

- Ստեղծեք կապ C-ի և Java-ի միջև.:

`swig -java {{path/to/swig_file.i}}`

- Ստեղծեք կապ C-ի և Ruby-ի միջև և Ruby մոդուլի նախածանցը `foo::bar::`-ով:

`swig -ruby -prefix "{{foo::bar::}}" {{path/to/swig_file.i}}`
