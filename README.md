# Pop Up Shop Server

## Endpoints
| Endpoint | Parameters | Response |
|   ---    |     ---    |   ---    |
| GET `/merchant/<int:merchant_id>` | n/a | `{'merchant': {'id': `<string>`, 'name': `<string>`, 'menu': [<menu_items>], 'receipt': [<receipt_items>]` |

## Objects
menu_item:
```json
{
    'id': <int>,
    'price': <float>,
    'merchant_id': <string>
}
```

receipt_item:
```json
{
  'id': <int>,
  'datetime': <datetime>,
  'items': [<menu_items>...]
  'merchant_id': <string>
}
```

