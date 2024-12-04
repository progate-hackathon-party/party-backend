import jwt
import	os
from dotenv import load_dotenv

def auth_jwt(token: str):
    load_dotenv(".env")

    region = 'ap-northeast-1'
    user_pool_id = os.environ.get("USER_POOL_ID")
    client_id = os.environ.get("USER_POOL_CLIENT_ID")
    
    issuer = f'https://cognito-idp.{region}.amazonaws.com/{user_pool_id}'
    jwks_url = f'{issuer}/.well-known/jwks.json'

    jwks_client = jwt.PyJWKClient(jwks_url)
    signing_key = jwks_client.get_signing_key_from_jwt(token)

    token = jwt.decode(
        token,
        signing_key.key,
        algorithms=["RS256"],
        audience=client_id,
        issuer=issuer
    )

    if token['token_use'] != 'id':
        raise Exception('Invalid token_use')
    
    return token