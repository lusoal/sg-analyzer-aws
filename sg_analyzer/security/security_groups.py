#!/usr/bin/python
import boto3
from termcolor import colored
from clint.textui import puts, indent

class Security(object):

    #constructor to initialize the client to search under the api
    def __init__(self, acess_key, secret_key, region):
        self.acess_key = acess_key
        self.secret_key = secret_key
        self.region = region
        if self.acess_key != "":
            self.client = boto3.client('ec2', aws_access_key_id=self.acess_key,aws_secret_access_key=self.secret_key, region_name=self.region)
        else:
            self.client = boto3.client('ec2')
        
    def get_security_groups_all_instances(self):
        #filters for ec2 name to check an specific ec2
        try:
            for ec2 in self.client.describe_instances()['Reservations']:
                print "="*30
                print colored(ec2['Instances'][0]['InstanceId'], 'green')
                for sg in ec2['Instances'][0]['SecurityGroups']:
                    print "Security Group Name: " + colored(sg["GroupName"], 'blue')
                    for sg_rules in self.client.describe_security_groups(GroupIds=[str(sg['GroupId'])])['SecurityGroups']:
                        for ips in sg_rules['IpPermissions']:
                                #print ips   
                                if "ToPort" in str(ips):
                                    with indent(2, quote='>'):
                                        puts ("Porta Liberada: "+str(colored(ips["FromPort"], "red") + " - " + colored(ips["ToPort"], 'red')))
                                    for ip_unique in ips['IpRanges']:
                                        with indent(4, quote='-'):
                                            puts(ip_unique['CidrIp'])
                                    for sg_ids in ips['UserIdGroupPairs']:
                                        with indent(4, quote="-"):
                                            puts(sg_ids['GroupId'])
                                else:
                                    with indent(2, quote='>'):
                                        puts(colored("All traffic para", "red"))
                                    for ip_unique in ips['IpRanges']:
                                        with indent(4, quote='-'):
                                            puts(ip_unique['CidrIp'])   
                                    for sg_ids in ips['UserIdGroupPairs']:
                                        with indent(4, quote="-"):
                                            puts(sg_ids['GroupId'])                   
        except Exception as e:
            print "Error " + str(e)

    def get_sg_compromised(self, port):
        #get security groups with some ports open to 0.0.0.0/0
        for ec2 in self.client.describe_instances()['Reservations']:
            for sg in ec2['Instances'][0]['SecurityGroups']:
                if port != "":
                    response = self.client.describe_security_groups(
                    Filters=[
                            {
                                'Name': 'ip-permission.cidr',
                                'Values': [
                                    '0.0.0.0/0',
                                ]
                            }, {'Name': 'ip-permission.to-port', 'Values': [port]}  ], GroupIds=[str(sg['GroupId'])])['SecurityGroups']
                else:
                    response = self.client.describe_security_groups(
                    Filters=[
                            {
                                'Name': 'ip-permission.cidr',
                                'Values': [
                                    '0.0.0.0/0',
                                ]
                            }], GroupIds=[str(sg['GroupId'])])['SecurityGroups']
                for sg_rules in response:
                    print colored(ec2['Instances'][0]['InstanceId'], 'green')
                    print colored(sg['GroupName'], "blue")
                    for ips in sg_rules['IpPermissions']:
                        if "ToPort" in str(ips):
                            with indent(2,quote='>'):
                                puts ("Porta: "+colored(str(ips['FromPort'])+"-"+str(ips['ToPort']), "red")+" para 0.0.0.0/0")
                        else:
                            with indent(2, quote='>'):
                                puts(colored("All Traffic", "red")+" para: 0.0.0.0/0")
