# tree

> Mevcut dizinin içeriğini ağaç biçiminde göster.
> Daha fazla bilgi: <http://mama.indstate.edu/users/ice/tree/>.

- Dosya ve dizinleri `num` değeri kadar derinlikte göster (1 olması durumunda mevcut dizin gösterilir):

`tree -L {{num}}`

- Yalnızca dizinleri göster:

`tree -d`

- Renklendirme açık olacak şekilde gizli dosyaları dahi göster:

`tree -a -C`

- Ağacın satırlarını girintiler yerine tüm yolu belirterek göster:

`tree -i -f`

- Tüm dosyaların ve dizinlerin eklenerek artan boyutlarını, insanların okuyabileceği bir biçimde göster:

`tree -s -h --du`

- Ağaç hiyerarşisi içindeki dosyaları bir wildcard (glob) kalıbı kullanarak ve aranan özellikteki dosyalara sahip olmayan dizinleri yoksayarak göster:

`tree -P '{{*.txt}}' --prune`

- Ağaç hiyerarşisi içindeki dizinleri bir wildcard (glob) kalıbı kullanarak ve istenen dizine atalığı olmayan dizinleri yoksayarak göster:

`tree -P {{dizin_ismi}} --matchdirs --prune`

- Ağacı belirtilen dizinleri yoksayarak göster:

`tree -I '{{dizin_ismi1|dizin_ismi2}}'`
