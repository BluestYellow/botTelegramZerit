import mercadopago

sdk = mercadopago.SDK(TOKEN)

payment_data = {
    "transaction_amount": valor,
    "description": "descrição",
    "payment_method_id": 'pix',
    "installments": 1,
    "payer": {
        "email": 'email_do_cliente@dominio.xpto'
    }
}
result = sdk.payment().create(payment_data)
print(result['response'])