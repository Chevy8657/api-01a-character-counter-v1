# Character Counter

Single-purpose API. Stateless. Deterministic. Returns JSON only.

## Endpoints
- GET `/health`
- GET `/v1/char-count?text=`

## Example

Request:
`/v1/char-count?text=Hello%20world`

Response:
```json
{
  "input": "Hello world",
  "char_count": 11
}
