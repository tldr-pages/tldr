# virt-xml-validate

> `libvirt` XML 파일을 스키마에 따라 검증.
> 스키마가 지정되지 않으면, XML 파일의 루트 요소에 의해 스키마가 결정됩니다.
> 더 많은 정보: <https://libvirt.org/manpages/virt-xml-validate.html>.

- 특정 스키마에 따라 XML 파일 검증:

`virt-xml-validate {{경로/대상/파일.xml}} {{스키마}}`

- 도메인 스키마에 따라 도메인 XML 검증:

`virt-xml-validate {{경로/대상/도메인.xml}} domain`
