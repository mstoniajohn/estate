from email.policy import default

from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    status_code = 404
    default_detail="The requested profile does not exist" #need to use these 2


class NotYourProfile(APIException):
    status_code = 403
    default_detail = "You can only edit your own profile"
