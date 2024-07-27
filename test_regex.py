import re

def check_token(token):
    token_pattern = re.compile(r'[MN][A-Za-z\d]{23}\.[\w-]{6}\.[\w-]{27}')
    return bool(token_pattern.fullmatch(token))
print(check_token("i think its true bro"))