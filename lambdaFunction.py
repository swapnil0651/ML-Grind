#lambda function for terminating instances with certain tags
import boto3

def lambda_handler(event, context):
    # Create an EC2 resource client using boto3
    ec2_client = boto3.client('ec2')

    # Describe all EC2 instances
    response = ec2_client.describe_instances()

    # Loop through each reservation (group of instances)
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # Get the instance ID
            instance_id = instance['InstanceId']
            
            # Check if the instance has tags
            if 'Tags' in instance:
                # Loop through tags to find 'env' tag
                for tag in instance['Tags']:
                    if tag['Key'] == 'env' and tag['Value'] == 'test':
                        # If 'env' tag exists and its value is 'test', terminate the instance
                        print(f"Terminating instance: {instance_id}")
                        ec2_client.terminate_instances(InstanceIds=[instance_id])
                        break
    return {
        'statusCode': 200,
        'body': f"Checked instances and terminated the ones with 'env' tag as 'test'."
    }
#run this on a lambda function with a manual trigger and roles specified to delete instances with tag env with value test