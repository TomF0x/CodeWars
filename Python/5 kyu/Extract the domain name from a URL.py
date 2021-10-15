# https://www.codewars.com/kata/514a024011ea4fb54200004b

def domain_name(url):
    if 'http' in url and 'www' in url:
        return url.replace('www.', '').split('//')[1].split('.')[0]
    elif 'http' in url:
        return url.split('//')[1].split('.')[0]
    elif not 'http' in url and not 'www' in url:
        return url.split('.')[0]
    else:
        return url.split('.')[1]
