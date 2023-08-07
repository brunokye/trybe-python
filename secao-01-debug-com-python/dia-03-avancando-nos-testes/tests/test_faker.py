from create_user import create_user


def test_create_user(faker):
    fake_email = faker.email()
    fake_name = faker.name()

    res = create_user(fake_name, fake_email)

    assert fake_name.startswith(res["first_name"])
    assert fake_name.endswith(res["last_name"])
    assert res["email"] == fake_email
    assert fake_email.endswith(res["email_domain"])


def test_faker_email(faker):
    fake_email = faker.email()
    assert isinstance(fake_email, str)
    assert '@' in fake_email
    assert '.' in fake_email
