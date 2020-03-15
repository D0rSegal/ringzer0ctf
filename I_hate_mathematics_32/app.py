import requests
import re

REQUEST_URL = r'https://ringzer0ctf.com/challenges/32/'
LOGIN_URL = 'http://ringzer0team.com/login'
MESSAGE_REGEX = r'---- BEGIN MESSAGE -----<br />\r\n\t\t(.*)<'
FLAG_REGEX = r'(FLAG-[a-zA-Z]+)'


def get_response(cookie, key=''):
    res = requests.get(REQUEST_URL + key, cookies={'PHPSESSID': cookie})
    data = res.text
    return str(data)


def extract_data(response_text, regex):
    if response_text:
        regex_results = re.findall(regex, response_text)
        if regex_results:
            return regex_results[0]
    return ''


def calc(expression):
    parts = expression.split(' ')
    a = int(parts[0])
    b = int(parts[2], 16)
    c = int(parts[4], 2)
    return str(a + b - c)


def main():
    cookie = input("ENTER YOUR PHPSESSID:   ")
    response = get_response(cookie)
    expression = extract_data(response, MESSAGE_REGEX)
    key = calc(expression)
    new_response = get_response(cookie, key)
    flag = extract_data(new_response, FLAG_REGEX)
    print(flag)


if __name__ == '__main__':
    main()
