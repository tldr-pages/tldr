# aws s3 cp

> Copy a local file or S3 object to another location locally or in S3.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html>.

- Copy a local file to S3:

`aws s3 cp {{file_name}} s3://{{example_bucket_name}}/{{file_name}}.txt`

- Copy a file from S3 to S3:

`aws s3 cp s3://{{example_bucket_name}}/{{file_name}}.txt s3://{{example_bucket_name}}/{{file_name_2}}.txt`

- Copy an S3 object from one bucket to another:

`aws s3 cp s3://{{example_bucket_name}}/{{file_name}}.txt s3://{{example_bucket_name_2}}`

- Recursively copy S3 objects to a local directory:

`aws s3 cp s3://{{example_bucket_name}} . --recursive`

- Display help:

`aws s3 cp help`
