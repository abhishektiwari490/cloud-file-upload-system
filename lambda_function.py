import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        url = s3.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': 'your-bucket-name',
                'Key': 'uploaded_file.jpg'
            },
            ExpiresIn=300
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'upload_url': url
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
