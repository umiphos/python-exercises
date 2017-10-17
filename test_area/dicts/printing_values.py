import re
def truer(string):
    dict_ = {
        'alphanumeric': False,
        'alphabetical': False,
        'digits': False,
        'lowercase': False,
        'uppercase': False,
    }
    if re.search('\w', string):
        dict_['alphanumeric'] = True
    if re.search('[a-zA-Z]', string):
        dict_['alphabetical'] = True
    if re.search('[0-9]', string):
        dict_['digits'] = True
    if re.search('[a-z]', string):
        dict_['lowercase'] = True
    if re.search('[A-Z]', string):
        dict_['uppercase'] = True
    return dict_
if __name__ == '__main__':
    s = raw_input()
    dict_ = truer(s)
    keys = ['alphanumeric', 'alphabetical', 'digits', 'lowercase', 'uppercase']
    import ipdb;ipdb.set_trace()
    for x in range(len(dict_)):
        print dict_[keys[x]]
