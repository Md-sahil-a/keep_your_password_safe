import requests
import hashlib
import sys

def api_get(hasq):
    url = "https://api.pwnedpasswords.com/range/" + hasq
    res = requests.get(url)
    if res.status_code !=200:
        raise RuntimeError(f'fetching error{res.status_code}, check your api')
    return res


def count_pass(hashes, hash_to_check):
    hashes = (line.split(':')for line in hashes.text.splitlines())
    for h,count in hashes:
        if h == hash_to_check:
            return count
    return 0        





def check_pass(passwords):
    converting = hashlib.sha1(passwords.encode('utf-8')).hexdigest().upper()
    first5, last = converting[:5] , converting[5:]
    response = api_get(first5)
    return count_pass(response, last)


def main(args):
    for passwords in args:
        count = check_pass(passwords)
        if count:
            print(f'{passwords} was found on number of counts {count} make your pass very strong ')
        else:
            print(f'{passwords} was not found dont worry')
    return 'Done'        


main(sys.argv[1:])
