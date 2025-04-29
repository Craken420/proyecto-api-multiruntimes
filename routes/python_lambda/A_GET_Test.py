from app import app

@app.get("/A_GET_Test")
def lambda_handler():
    return {
        'statusCode': 200,
        'body': '{"message": "Lambda de Test esta funcionando"}'
    }
