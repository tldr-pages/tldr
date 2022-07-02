# cmake

> Çok platformlu yapım sistem oluşturucusu.
> Hedeflenen sisteme göre Makefile, Visual Studio projeleri ve benzerlerini oluşturur.
> Daha fazla bilgi: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Bir Makefile oluştur ve onu aynı dizindeki bir projeyi derlemek için kullan:

`cmake && make`

- Bir Makefile oluştur ve onu farklı bir "yapim" dizinindeki projeyi derlemek için kullan (kaynak-dışı yapım):

`cmake -H. -B {{build}} && make -C {{yapim}}`
