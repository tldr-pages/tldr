# aws cur

> Create, query, ແລະ delete AWS ທີ່ສະແດງເຖິງຄຳຈຳກັດຄວາມ.
> ຂໍ້ມູນເພີ່ມເຕີມ: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>.

- ສ້າງຕົ້ນທຶນ AWS ແລະ ລາຍງານການໃຊ້ງານຈາກໄຟລ໌ JSON:

`aws cur put-report-definition --report-definition file://{{path/to/report_definition.json}}`

- ລາຍງານກາຍເຄື່ອນໄຫວຂອງບັນຊີ:

`aws cur describe-report-definitions`

- ລຶບລາຍງານການເຄື່ອນໄຫວ:

`aws cur --region {{aws_region}} delete-report-definition --report-name {{report}}`
