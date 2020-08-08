# 测试数据分组
error_phone_params = [
    {'phone': '', 'pwd': 'python', 'expect': '请输入手机号'},
    {'phone': '12345678901', 'pwd': 'python', 'expect': '请输入正确的手机号'},
    {'phone': '1868472055', 'pwd': 'python', 'expect': '请输入正确的手机号'},
    {'phone': '18684720553', 'pwd': '', 'expect': '请输入密码'}
]

# error_pwd = [
#     ('18684720553', '', '请输入密码')
# ]

invalidate_params = [
    {'phone': '18684720553', 'pwd': 'python1', 'expect': '帐号或密码错误!'},
    {'phone': '13711112222', 'pwd':'123456', 'expect': '此账号没有经过授权，请联系管理员!'}
]

exact_params = [
    {'phone': '18684720553', 'pwd': 'python', 'expect': '我的帐户[小小鸟]'}
]