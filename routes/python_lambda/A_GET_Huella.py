from app import app

@app.get("/A_GET_Huella")
def lambda_handler():
    return {
        'statusCode': 200,
        'body': '{"message": "Lambda de huella funcionando"}'
    }
