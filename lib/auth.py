from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
import jwt
import os
from dotenv import load_dotenv

# Load environment variables once
load_dotenv(".env")

api_key_header = APIKeyHeader(name="Authorization", auto_error=True)

def auth_jwt(auth_header: str = Depends(api_key_header)):
    try:
        region = os.environ.get("AWS_DEFAULT_REGION")
        user_pool_id = os.environ.get("USER_POOL_ID")
        client_id = os.environ.get("USER_POOL_CLIENT_ID")
        
        if not user_pool_id or not client_id:
            raise HTTPException(status_code=500, detail="Server misconfiguration")

        # Extract token from "Bearer <token>"
        if not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=403, detail="Invalid token format")
        token = auth_header.split(" ", 1)[1]

        issuer = f"https://cognito-idp.{region}.amazonaws.com/{user_pool_id}"
        jwks_url = f"{issuer}/.well-known/jwks.json"
        
        # Fetch signing key
        jwks_client = jwt.PyJWKClient(jwks_url)
        signing_key = jwks_client.get_signing_key_from_jwt(token)

        # Decode and validate the token
        decoded_token = jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            audience=client_id,
            issuer=issuer
        )

        if decoded_token.get("token_use") != "id":
            raise HTTPException(status_code=403, detail="Invalid token use")

        return decoded_token

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid token")
    except Exception as e:
        # Log the exception for debugging (optional)
        print(f"Authentication error: {e}")
        raise HTTPException(status_code=403, detail="Authentication failed")
