# SG-AWS-ANALYZER

Analyzes all rules of security groups attached to instances (EC2) and also verify if some security group have some rule open to 0.0.0.0

Obs: At moment analyzes just security groups attached to ec2 instances.

## Getting Started

For getting started with sg-analyzer-aws first you have to run the follow commands.
  
  - python setup.py install

After that you will be able to start using sg-analyzer-aws

### Prerequisites

- Python 2.7
- awscli (You have to configure your aws cli and the credentials you want to analyze in your machine)

### Installing

First you have to install

```
python setup.py install
```

After that you will be able to invoke like this:

```
sg_analyzer --help
```


