import requests
import re
import hashlib

REQUEST_URL = r'https://ringzer0ctf.com/challenges/14/'
LOGIN_URL = 'http://ringzer0team.com/login'
MESSAGE_REGEX = r'---- BEGIN MESSAGE -----<br />\r\n\t\t(.*)<'
FLAG_REGEX = r'(FLAG-\w+)'


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


def get_hash(text):
    n = int(text, 2)
    text = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    return hashlib.sha512(text.encode('utf8')).hexdigest()


def main():
    cookie = input("ENTER YOUR PHPSESSID:   ")
    response = get_response(cookie)
    expression = extract_data(response, MESSAGE_REGEX)
    key = get_hash(expression)
    new_response = get_response(cookie, key)
    flag = extract_data(new_response, FLAG_REGEX)
    print(flag)


if __name__ == '__main__':
    main()
