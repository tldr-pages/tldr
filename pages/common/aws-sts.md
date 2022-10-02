# aws-sts

> Security Token Service (STS) enables you to request temporary credentials for (IAM) users or for users that you authenticate (federated users)
> More information: <https://docs.aws.amazon.com/cli/latest/reference/sts/> 

-  To get temporary security credentials that you can use to access Amazon Web Services resources that you might not normally have access to:

` aws sts assume-role --role-arn {{ aws-role-arn}}`

-  To get IAM user or role whose credentials are used to call the operation:

` aws sts get-caller-identity`
