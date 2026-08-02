import boto3

ec2 = boto3.client('ec2')

INSTANCE_ID = "i-016becfdafc7c13bb"

def lambda_handler(event, context):
    response = ec2.reboot_instances(
        InstanceIds=[INSTANCE_ID]
    )

    return {
        "statusCode": 200,
        "body": f"EC2 Instance {INSTANCE_ID} reboot initiated successfully."
    }
