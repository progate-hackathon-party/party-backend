import	sys
import	os
import	boto3
import hmac
import hashlib
import base64
from dotenv import load_dotenv

def cognito_auth(parameter):
	# 認証開始
	try:
		aws_client = boto3.client('cognito-idp')

		aws_result = aws_client.admin_initiate_auth(
			UserPoolId = parameter["user_pool_id"],
			ClientId = parameter["user_pool_client_id"],
			AuthFlow = "ADMIN_USER_PASSWORD_AUTH",
			AuthParameters = {
				"USERNAME": parameter["usr"],
				"PASSWORD": parameter["password"],
			}
		)

		# 認証完了
		sys.stderr.write("*** success ***\n")
		return aws_result

	except Exception as ee:
		# 認証失敗
		sys.stderr.write("*** error ***\n")
		sys.stderr.write(str(ee) + "\n")
		return None

sys.stderr.write("*** 開始 ***\n")
dotenv_path = '.env'
load_dotenv(dotenv_path)

parameter={}
parameter["user_pool_id"]=os.environ.get("USER_POOL_ID")
parameter["user_pool_client_id"]=os.environ.get("USER_POOL_CLIENT_ID")
parameter["usr"]=os.environ.get("USR")
parameter["password"]=os.environ.get("PASSWORD")

print(parameter)
result = cognito_auth(parameter)
print(result)
print("Bearer "+result["AuthenticationResult"]["IdToken"])
sys.stderr.write("*** 終了 ***\n")