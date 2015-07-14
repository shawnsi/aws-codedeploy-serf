# Auto Scaling Serf

This project will assist in creating an autoscaling Serf infrastructure.  The serf members are discovered via EC2 API calls.  This can be extended to make clustered applications aware of cluster state and scaling events.

## Setup Launch Configuration

Use `cloudformation/template.json` to setup IAM polices, roles, and profiles.  This will also configure a launch configuration to be used in autoscaling.

### Parameters

#### AmiId

Provide an Amazon Linux AMI for your region (ami-1ecae776 in us-east-1).

#### KeyPair

SSH Keypair to access the Serf instances with.

#### SecurityGroup

The security group to apply to serf instances.  Open port 7946 TCP/UDP from anywhere.  Open port 22 TCP from your location or anywhere.

#### SerfEncryptKey

Provide a *base64* encoded key for Serf encryption.  The output of `serf keygen` works well.

## Create Auto Scaling Group

Setup an autoscaling group in the network of your choice.  Just use the launch configuration in the cloudformation outputs.

## Setup CodeDeploy

Create a codedeploy application that deploys to the autoscaling group.

## Setup CodePipeline

Create a pipeline that deploys from github to the codedeploy application.
