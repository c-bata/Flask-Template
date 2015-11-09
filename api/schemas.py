login_schema = {
    "name": "Login",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer",
            "minimum": 0
        },
        "password": {
            "type": "string",
            "minLength": 4,
            "maxLength": 128,
        }
    }
}

signup_schema = {
    "name": "Signup",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "minLength": 4,
            "maxLength": 128,
        },
        "email": {
            "type": "string",
            "oneOf": [{ "format": "email"}]
        },
        "password": {
            "type": "string",
            "minLength": 4,
            "maxLength": 128,
        }
    }
}

record_schema = {
    "name": "Records",
    "type": "object",
    "properties": {
        "day": {
            "type": "date",
            "pattern": "^[0-9]{4}-[0-9]{2}$"
        },
        "begin_time": {
            "type": "string",
            "oneOf": [{ "format": "date-time" }]
        },
        "finish_time": {
            "type": "string",
            "oneOf": [
                { "format": "date-time" }
            ]
        },
        "contents": {
            "type": "string",
            "minLength": "0",
            "maxLength": "256"
        }
    }
}
