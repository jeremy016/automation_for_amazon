

users = [
    {"name": "valid_user", "email": "football-good.rga48cmj@mailosaur.io", "phone": "0978126016", "password": "QWERT!@#$%", "display_name":"amazon_tester"},
    {"name": "invalid_user", "email": "invalidUser@test.com", "phone": "0912345678", "password": "qwert1235"},
]


def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)


