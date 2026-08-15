import data
import sender_stand_request

def get_kit_body(kit_name):
    current_body=data.kit_body.copy()
    current_body["name"] = kit_name
    return current_body
def get_new_user_token():
   response = sender_stand_request.post_new_user(data.user_body)
   return response.json()['authToken']

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
        response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
        assert response.status_code == 400

def test_1_kit_name_min_length():
    new_kit_body = get_kit_body("g")
    positive_assert(new_kit_body)


def test_2_kit_name_max_length():
    new_kit_body = get_kit_body("g" * 511)
    positive_assert(new_kit_body)

def test_3_kit_name_empty():
    new_kit_body = get_kit_body("")
    negative_assert_code_400(new_kit_body)

def test_4_kit_name_too_long():
    new_kit_body = get_kit_body("a" * 512)
    negative_assert_code_400(new_kit_body)

def test_5_kit_name_special_characters():
    new_kit_body = get_kit_body("*&%@")
    positive_assert(new_kit_body)

def test_6_kit_name_with_spaces():
    new_kit_body = get_kit_body(" g grise")
    positive_assert(new_kit_body)

def test_7_kit_name_with_numbers():
    new_kit_body = get_kit_body("123456")
    positive_assert(new_kit_body)

def test_8_kit_name_without_key_and_value():
    new_kit_body = data.kit_body.copy()
    new_kit_body.pop("name")
    negative_assert_code_400(new_kit_body)

def test_9_kit_name_wrong_type():
    new_kit_body = get_kit_body(12345)
    negative_assert_code_400(new_kit_body)
