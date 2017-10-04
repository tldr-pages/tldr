# bedops

> BEDOPS: A fast, highly scalable, and easily-parallelizable genome analysis toolkit
> Apply efficient set operations on any number of sorted BED or Starch files such as element-of, intersection, merge, difference, partition, etc. and their logical inverses

- Take the multiset union of two or more BED or Starch files and write the sorted result to {{path/to/output_file}}:

`bedops --everything {{path/to/file_1}} {{path/to/file_2}} [{{path/to/file_3}} ...] > {{path/to/output_file}}`

- Find elements from reference set {{path/to/reference_file}} that overlap one or more query sets by one or more bases:

`bedops --element-of 1 {{path/to/reference_file}} {{path/to/query_file_1}} [{{path/to/query_file_2}} ...] > {{path/to/output_file}}`

- Merge the overlapping intervals in one or more files and write the sorted result to {{path/to/output_file}}:

`bedops --merge {{path/to/file_1}} [{{path/to/file_2}} {{path/to/file_3}} ...] > {{path/to/output_file}}`

- Partition overlapping intervals in one or more files into disjoint intervals and write the sorted result to {{path/to/output_file}}:

`bedops --partition {{path/to/file_1}} [{{path/to/file_2}} {{path/to/file_3}} ...] > {{path/to/output_file}}`

- For all operations, efficiently apply set operations on specified {{chromosome}} and ignore other chromosomes:

`bedops --chrom {{chromosome}} --operation {{files...}} > {{path/to/output_file}}`
