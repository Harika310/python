import boto3  # pip install boto3

# Initialize a session using Amazon EC2
ec2 = boto3.resource('ec2')

# Create a new EC2 instance
instances = ec2.create_instances(
    ImageId='ami-09c813fb71547fc4f',  # Replace with your desired AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    SecurityGroupIds=['sg-089040169ad25fd55'],
    # KeyName='your-key-pair-name'  # Replace with your key pair name
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Python'  # Replace with your desired instance name
                }
            ]
        }
    ]

)

# Print instance details
for instance in instances:
    
    print(f"EC2 Instance ID: {instance.id}")
    print(f"Instance State: {instance.state['Name']}")
    # print(f"Stop instance: {stop_instance('i-0abcd1234efgh5678')}")


# def start_instance(instance_id):
#     ec2.start_instances(InstanceIds=[instance_id])
#     print(f"Started instance: {instance_id}")

# def stop_instance(instance_id):
#     ec2.stop_instances(InstanceIds=[instance_id])
#     print(f"Stopped instance: {instance_id}")
    





# import boto3

# Print all instance details(terminated, Running)
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
#     Start or stop instances by calling the respective functions with instance IDs
#      start_instance('i-0abcd1234efgh5678')
#      stop_instance('i-0abcd1234efgh5678')
