from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin

def send_otp_code(phone_number, code):
	try:
		api = KavenegarAPI('686A6B495A41416E6B626632544F63336D5756774A6944542F386844646B78422F4A654473364B4A45786B3D')
		params = {
			'sender': '',
			'receptor': phone_number,
			'message': f'{code} کد تایید شما '
		}
		response = api.sms_send(params)
		print(response)
	except APIException as e:
		print(e)
	except HTTPException as e:
		print(e)



class IsAdminUserMixin(UserPassesTestMixin):
	def test_func(self):
		return self.request.user.is_authenticated and self.request.user.is_admin