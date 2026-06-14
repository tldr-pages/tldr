# նահանջ

> Փոխեք C/C++ ծրագրի տեսքը՝ տեղադրելով կամ ջնջելով բացատը:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/indent/manual/indent/Option-Summary.html>:.

- Ձևաչափեք C/C++ աղբյուրը ըստ Linux ոճի ուղեցույցի, ինքնաբերաբար կրկնօրինակեք բնօրինակ ֆայլերը և փոխարինեք ներքևված տարբերակներով.:

`indent {{[-linux|--linux-style]}} {{path/to/source1.c path/to/source2.c ...}}`

- Ձևաչափեք C/C++ աղբյուրը ըստ GNU ոճի՝ ներքևված տարբերակը պահելով մեկ այլ ֆայլում՝:

`indent {{[-gnu|--gnu-style]}} {{path/to/source.c}} -o {{path/to/indented_source.c}}`

- Ձևաչափեք C/C++ աղբյուրը ըստ Kernighan & Ritchie-ի (K&R) ոճի, առանց ներդիրների, 3 բացատ մեկ նահանջում և փաթեթավորեք տողերը 120 նիշով:

`indent {{[-kr|--k-and-r-style]}} {{[-il|--indent-level]}}3 {{[-nut|--no-tabs]}} {{[-l|--line-length]}}120 {{path/to/source.c}} -o {{path/to/indented_source.c}}`
