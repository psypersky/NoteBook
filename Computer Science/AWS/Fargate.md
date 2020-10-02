# Fargate

Managed containers without EC2

ECS EC2 (traditional)

    You are all-in on AWS
    You have an existing AWS footprint such as an already defined VPC and subnets, processes for provisioning and managing EC2 instances
    You have an Ops team in place to manage AWS resources

ECS Fargate

    You are mostly utilizing AWS and may or may not have an existing VPC
    You may or may not be currently utilizing ECS and do not want or are looking to reduce your operations responsibility on AWS
    Your applications are stateless or manage state through S3, RDS or other external services from your containers.

## Resources

https://www.dragonspears.com/blog/aws-container-orchestration-101-ecs-vs-fargate-vs-eks
https://medium.com/containers-on-aws/building-a-socket-io-chat-app-and-deploying-it-using-aws-fargate-86fd7cbce13f