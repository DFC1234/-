# -*- coding: utf-8 -*-
import requests

def send_verification_code(phone):
    url = "https://p.njupt.edu.cn:802/eportal/portal/sms"
    
    # 替换这些值为实际的设备和页面信息
    term = {
        'mac': 'xx:xx:xx:xx:xx:xx',  # 设备的MAC地址
        'ip': '192.168.1.1',         # 设备的IP地址
        'ipv6': 'fe80::xxxx:xxxx:xxxx:xxxx'  # 设备的IPv6地址
    }
    page = {
        'index': 1  # 页面索引
    }
    
    data = {
        'telephone': phone,
        'mac': term['mac'],
        'ip': term['ip'],
        'ipv6': term['ipv6'],
        'bind': 0,
        'page_index': page['index'],
        'prefix': '',
        'sms_type': 0,
    }
    
    try:
        response = requests.get(url, params=data)
        if response.status_code == 200:
            print("服务器响应:", response.text)  # 打印服务器的原始响应内容
            response_data = response.json()  # 尝试解析 JSON
            if response_data['result'] == 1 or response_data['result'] == 'ok':
                print(u'验证码正下发，请注意查收！')
            else:
                print(response_data.get('msg', u'发送验证码失败，因为网络问题或者页面已过期，请刷新页面重试！如果已收到验证码，请忽略此提示！'))
        else:
            print(u'服务器响应状态码:', response.status_code)
    except requests.RequestException as e:
        print(u'发送验证码失败，因为网络问题或者页面已过期，请刷新页面重试！如果已收到验证码，请忽略此提示！: {}'.format(e))
    except ValueError as ve:
        print(u'无法解析服务器响应的JSON格式: {}'.format(ve))

# 输入实际的手机号
phone = "        "  # 这里填写实际的手机号
send_verification_code(phone)
