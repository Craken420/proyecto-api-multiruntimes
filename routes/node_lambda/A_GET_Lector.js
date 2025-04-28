// routes/node_lambda/A_GET_Lector.js
exports.handler = async (event) => {
    return {
        statusCode: 200,
        body: JSON.stringify({ message: 'Lambda de lector funcionando' }),
    };
}