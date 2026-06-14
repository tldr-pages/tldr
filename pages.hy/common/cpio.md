# cpio

> Պատճենեք ֆայլերը արխիվներում և արխիվներից դուրս:.
> Աջակցում է արխիվի հետևյալ ձևաչափերին՝ cpio-ի հատուկ երկուական, հին ASCII, նոր ASCII, crc, HPUX երկուական, HPUX հին ASCII, հին tar և POSIX.1 tar:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/cpio/manual/cpio.html#Invoking-cpio>:.

- Վերցրեք ֆայլերի անունների ցուցակը `stdin`-ից և ավելացրեք դրանք արխիվում (copy-[o]ut) cpio-ի երկուական ձևով.:

`echo "{{path/to/file1 path/to/file2 ...}}" | cpio {{[-o|--create]}} > {{archive.cpio}}`

- Պատճենեք բոլոր ֆայլերը և գրացուցակները գրացուցակում և դրանք ավելացրեք արխիվում (copy-[o]ut), բառացի ռեժիմով.:

`find {{path/to/directory}} | cpio {{[-ov|--create --verbose]}} > {{archive.cpio}}`

- Ընտրեք բոլոր ֆայլերը արխիվից (copy-[i]n)՝ ստեղծելով դիրեկտորիաներ, որտեղ անհրաժեշտ է, բառացի ռեժիմում.:

`cpio < {{archive.cpio}} {{[-idv|--extract --make-directories --verbose]}}`
