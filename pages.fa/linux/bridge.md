# bridge

> نمایش و تغییر آدرس‌ها و دستگاه‌های پل شبکه.
> اطلاعات بیشتر: <https://manned.org/bridge>.

- فهرست کردن همهٔ پل‌ها و رابط‌های آن‌ها:

`bridge {{[l|link]}}`

- نمایش اطلاعات VLAN درگاه:

`bridge {{[v|vlan]}}`

- اختصاص یک VLAN به یک درگاه:

`sudo bridge {{[v|vlan]}} {{[a|add]}} dev {{lanX}} vid {{vlan_id}} pvid {{tagged|untagged}}`

- حذف یک VLAN از یک درگاه:

`sudo bridge {{[v|vlan]}} {{[d|delete]}} dev {{lanX}} vid {{vlan_id}}`

- پایش تغییرات رابط‌های پل:

`bridge {{[mo|monitor]}}`

- نمایش راهنما:

`bridge {{[h|help]}}`
