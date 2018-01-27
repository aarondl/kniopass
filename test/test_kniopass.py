import kniopass

PASSWORD = 'hunter42'

def test_compute_key():
    key = kniopass.PasswordStore.compute_key(PASSWORD)
    assert key ==  (
        b'\x08\xcb\xcc\xc2\x18 \x8f\xca\xe4\xf0\xabx+\x94\xb9\x16.\x14H\x16'
        b"\xba\xf5<\xc9\x7f\xbf\xaelA>!\x9a\x1c\xf6H\x85ty\x87N\xd5'u\\\xda\xfbL\xe1"
        b'\x80|\x0e\xbb\xa8\xe2\x9a\xdd\xb0\x07\xc4\xd66\x97\x04U\x0e\xe0\x9c\xba'
        b'\xf8}\xf1\x8a\xe9{\xee\x9em\n\xf8l\xff\xc6\x97\x15\x01\xe9\x9c@[\x9fMN'
        b'Fj\x1a\xfa\x84\xda\xa8\xe1\x1e\x1dq\xb5\x16\xc7\x11c\xc7\x00\xbd\xfd'
        b'\xbd\x03\x04\xfa\x83\x85\xbeZ\xf4G\x7f\xe0<\xd1\xce\x02A\xb9\x00,\x04\x1dY1'
        b'\xa2\x7f\x0ba8\x9a\x01\x01\x05\xad\x85\x19#\xfe.\xdd\x13}T\x16)\x9e\xf3\xc1'
        b'*\x03\x90\xa4Q\xb6\x83\x1d\xaew\xfb\x1f}wV\x9f\x89rx\xbd\xdckz\x0cXQ8n'
        b'\xf3\xc3\xf8\x17\x18\xbc\xe7\xa5\xa8c\xe2?\xda\x90\xbb\x14\xb6\x99C\xf1'
        b'K\xc5%"\xec\xcd\x17\x8d\xe6\x93\xfa%\x8a\xa4\xcc\xdeh\xc3,\x94o]\x9cc'
        b'\x16\x03\x10\x7f\xda\xe5\x0cM\xa4\xd0,)\x87$\xdddU\\\xe4z\x9b\x0b\xc0,')

def test_encrypt_data():
    key = kniopass.PasswordStore.compute_key(PASSWORD)
    data = b'foobar asdasd kasdkljasdkl asjdkl asjdkla sjdl'
    ct = kniopass.PasswordStore.encrypt_data(key, data)
    pt = kniopass.PasswordStore.decrypt_data(key, ct)
    assert data == pt

def test_password():
    password = kniopass.PasswordStore.generate_password()
    print(password)
    assert password == ''
