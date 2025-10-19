# Stage 0 — Dynamic Profile API

This is a simple FastAPI project that returns user profile information along with a dynamic cat fact fetched from the [Cat Fact API](https://catfact.ninja/fact).


## Features
- `/me` endpoint returning:
  - User name, email, and backend stack
  - Random cat fact (fetched live from API)
  - Dynamic UTC timestamp in ISO 8601 format
- Handles API errors gracefully
- Uses environment variables for sensitive data
- Includes CORS for cross-domain requests
- Logging for debugging and monitoring


## Response Example

```json
{
  "status": "success",
  "user": {
    "name": "Mary Kafaru",
    "email": "mary.kafaru@example.com",
    "stack": "Python/FastAPI"
  },
  "fact": "Cats sleep for 70% of their lives.",
  "timestamp": "2025-10-19T12:45:23.123Z"
}
