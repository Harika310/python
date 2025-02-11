import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-west-2')  # Change the region as needed


    instance = ec2.run_instances(

        ImageId='ami-09c813fb71547fc4f',  # Replace with your desired AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        SecurityGroupIds=['sg-089040169ad25fd55'],
        # SubnetId=''
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

    return {
        'statusCode': 200,
        'body': 'Instance created successfully',
        'instance_id': instance['Instances'][0]['InstanceId']
    }
