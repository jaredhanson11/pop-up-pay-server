# Pop Up Shop Server

## Endpoints
- Client purchases menu items from merchant id
GET `/purchase/<client_id>/<merchant_id>/<transaction_id>?<menu_item_id>=<quantity>&...`

- Client gets receipts
GET `/customers/<client_id>`

- Merchant gets menu items and receipts
GET `/merchant/<merchant_id>`

- Merchant checks if transaction is complete
GET `/transactions/<transaction_id>`
