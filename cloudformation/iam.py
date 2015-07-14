#!/usr/bin/env python
# Converted from IAM_Users_Groups_and_Policies.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import FindInMap, Parameter, Ref, Template
from troposphere.iam import PolicyType, Role

from awacs.aws import Allow, Policy, Principal, Statement
from awacs.sts import AssumeRole

t = Template()

t.add_description("AWS CloudFormation Template: IAM Roles for "
                  "https://github.com/shawnsi/aws-codedeploy-serf.")

encrypt_key = t.add_parameter(Parameter(
    "SerfEncryptKey",
    Description="Base64 encoded encryption key for Serf cluster.",
    Type="String"
))

t.add_mapping("Region2Principal", {
    'ap-northeast-1': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'ap-southeast-1': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'ap-southeast-2': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'cn-north-1': {
        'EC2Principal': 'ec2.amazonaws.com.cn',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com.cn'},
    'eu-central-1': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'eu-west-1': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'sa-east-1': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'us-east-1': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'us-west-1': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'us-west-2': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'}
    }
)

t.add_resource(Role(
    "SerfInstanceRole",
    AssumeRolePolicyDocument=Policy(
        Statement=[
            Statement(
                Effect=Allow, Action=[AssumeRole],
                Principal=Principal(
                    "Service", [
                        FindInMap(
                            "Region2Principal",
                            Ref("AWS::Region"), "EC2Principal")
                    ]
                )
            )
        ]
    ),
    Path="/"
))

t.add_resource(PolicyType(
    "CodedeployServicePolicy",
    PolicyName="CodedeployServiceRole",
    PolicyDocument={
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:Get*",
                    "s3:List*"
                ],
                "Resource": [
                    "*",
                ]
            }
        ]
    },
    Roles=[Ref("SerfInstanceRole")]
))

t.add_resource(PolicyType(
    "CodedeployS3Policy",
    PolicyName="CodedeployS3Policy",
    PolicyDocument={
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:Get*",
                    "s3:List*"
                ],
                "Resource": [
                    "*",
                ]
            }
        ]
    },
    Roles=[Ref("SerfInstanceRole")]
))

t.add_resource(PolicyType(
    "SerfEC2Policy",
    PolicyName="SerfEC2Policy",
    PolicyDocument={
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "ec2:Describe*",
                    "autoscaling:Describe*"
                ],
                "Resource": [
                    "*",
                ]
            }
        ]
    },
    Roles=[Ref("SerfInstanceRole")]
))

print(t.to_json())

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
