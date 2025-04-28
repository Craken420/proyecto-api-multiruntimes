# routes/python_lambda/A_GET_Huella.py

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': '{"message": "Lambda de huella funcionando"}'
    }
