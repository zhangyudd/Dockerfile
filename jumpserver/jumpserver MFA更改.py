from itsdangerous import TimedJSONWebSignatureSerializer, JSONWebSignatureSerializer, \
    BadSignature, SignatureExpired
import random

'''

抄写jumpserver 两个公共类 制作签名，签名有方法可以生成otp签名

'''

class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance

class Signer(metaclass=Singleton):
    """用来加密,解密,和基于时间戳的方式验证token"""
    def __init__(self, secret_key=None):
        self.secret_key = secret_key

    def sign(self, value):
        if isinstance(value, bytes):
            value = value.decode("utf-8")
        s = JSONWebSignatureSerializer(self.secret_key)
        return s.dumps(value)

    def unsign(self, value):
        if value is None:
            return value
        s = JSONWebSignatureSerializer(self.secret_key)
        try:
            return s.loads(value)
        except BadSignature:
            return {}

    def sign_t(self, value, expires_in=3600):
        s = TimedJSONWebSignatureSerializer(self.secret_key, expires_in=expires_in)
        return str(s.dumps(value), encoding="utf8")

    def unsign_t(self, value):
        s = TimedJSONWebSignatureSerializer(self.secret_key)
        try:
            return s.loads(value)
        except (BadSignature, SignatureExpired):
            return {}

song=Signer(secret_key=此出处填写你的secret_key ,可以在config.py中找到)

seed = "234567ABCDEFGHIJKLMNOPQRSTUVWXYZ="
sa = []
for i in range(16):
    sa.append(random.choice(seed))
salt = ''.join(sa)
print(salt)

otpxx=song.sign(salt).decode('utf-8')
print(otpxx)