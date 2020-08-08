bid_error_data_1 = [
    {'amount': '1', 'expect': '请输入10的整数倍'},
    {'amount': '9', 'expect': '请输入10的整数倍'},
    {'amount': '99', 'expect': '请输入10的整数倍'},
]

bid_error_data_2 = [
    {'amount': '10', 'expect': '投标金额必须为100的倍数'},
    {'amount': '90', 'expect': '投标金额必须为100的倍数'},
    {'amount': '200000000000000000', 'expect': '投标金额大于可用金额'},
]

bid_success_data = [
    {'amount': '100', 'expect': '投标成功！'},
    {'amount': '1000', 'expect': '投标成功！'},
]