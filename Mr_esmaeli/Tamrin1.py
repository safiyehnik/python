import re
from kavenegar import *

operator_database = {
    "hamrah_e_aval": ["912", "919", "910", "915"],
    "irancell": ["930", "933", "935", "936", "937", "938", "939"],
    "Taliya": ["932"],
    "raytel": ["920", "921"],
    "kish": ["934"],
    "spadan": ["931"],
}
phone_number_database = [
    {
        "phone_number": "09133218364",
        "message": "hi safiyeh , i'm testing a code"
     },
    {
         "phone_number": "0915505416",
         "message": "hi Mom , i'm testing a code"
     },
    {
        "phone_number": "09151520047",
        "message": "Hi ali , i'm testing a code"
     },
]


def valid_phone_number(phone_number: str = None) -> bool:
    rejex = r"(0|\+98)?([ ]|-|[()]){0,2}9[1|2|3|4]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}"
    if phone_number is None:
        return False
    else:
        return False if re.search(rejex, phone_number) is None else True


def get_operator(phone_number: str = None) -> (str, str):
    result_valid_phone_number = valid_phone_number(phone_number)
    if result_valid_phone_number is False:
        return "", "phone number is wrong"
    else:
        if len(phone_number) == 13:
            pre_number = phone_number[3: 6]
        elif len(phone_number) == 11:
            pre_number = phone_number[1: 4]
        for key, value in operator_database.items():
            if pre_number in value:
                return key, ""
        else:
            return "", "Operator not found"


def send_sms(phone_number: str = None, messeage: str = None) -> (str, str):
    result_valid_phone_number = valid_phone_number(phone_number)
    if result_valid_phone_number is False:
        return "", "phone number is wrong"
    else:
        try:
            api = KavenegarAPI('66656D6A31502B4150652B516E392B34616867554C524132534C466862616155786F34696B5A37483656553D')
            params = {'sender': '', 'receptor': phone_number, 'message': messeage}
            response = api.sms_send(params)
            return phone_number, response
        except APIException as e:
            return "", str(e)
        except HTTPException as e:
            return "", str(e)


def send_SMS_Multiuser():
    for user in phone_number_database:
        phone = user.get("phone_number")
        sms = user.get("message")
        if valid_phone_number(phone) is False:
            print("phone number is wrong")
        else:
            operator_name = get_operator(phone)
            if operator_name == ('', 'Operator not found'):
                print("operator not in list")
            else:
                print(operator_name)
                phone_number, sms_status = send_sms(phone, sms)
                print(phone_number, sms_status)





#message = "hello world"
#phone_number = "09153218364"
#x, y = send_sms(phone_number, message)
#print(x, y)
send_SMS_Multiuser()
