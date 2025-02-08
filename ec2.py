import boto3  # pip install boto3

ec2 = boto3.client('ec2')

def list_instances():
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}")


if __name__ == "__main__":
    list_instances()

# import boto3

# ec2 = boto3.client('ec2')

# def list_instances():
#     response = ec2.describe_instances()
#     for reservation in response['Reservations']:
#         for instance in reservation['Instances']:
#             print(f"Instance ID: {instance['InstanceId']}")

# def start_instance(instance_id):
#     ec2.start_instances(InstanceIds=[instance_id])
#     print(f"Started instance: {instance_id}")

# def stop_instance(instance_id):
#     ec2.stop_instances(InstanceIds=[instance_id])
#     print(f"Stopped instance: {instance_id}")

# if __name__ == "__main__":
#     list_instances()
#     # Start or stop instances by calling the respective functions with instance IDs
#     # start_instance('i-0abcd1234efgh5678')
#     # stop_instance('i-0abcd1234efgh5678')
