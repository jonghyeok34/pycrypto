from pbkdf2 import crypt

pwhash = crypt('secret', iterations=400)
# pwhash = crypt('secret', iterations=400)
print(pwhash)
alleged_pw = 'secret'
if pwhash ==crypt(alleged_pw, pwhash):
    print('good')
else:
    print('bad')
