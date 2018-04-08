import json
import os
import hashlib


blockchain_dir = os.curdir + '/blockchain/'

def get_hash(filename):
#    blockchain_dir = os.curdir + '/blockchain/'
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()

def get_files():
    files = os.listdir(blockchain_dir)
    return sorted([int(i) for i in files])

def check_integrity():
#    blockchain_dir = os.curdir + '/blockchain/'
#    files = os.listdir(blockchain_dir)
#    files = sorted([int(i) for i in files])
    files = get_files()

    results = []

    for box in files[1:]:
        file_back = open(blockchain_dir + str(box))
        hash_back = json.load(file_back)['hash']
#     hash_back = json.load(open(blockchain_dir + str(box)))['hash']  
        box_file = str(box -1)
        hash_actual = get_hash(box_file)
#        print(hash_actual)
        if  hash_back == hash_actual:
            conclusion_result = 'OK'
        else:
            conclusion_result = 'DANGER'
        #print('block {} is: {} '.format(box_file, res))
        results.append({ 'block': box_file, 'result': conclusion_result})

    return results

#    print(files)


def write_block(name, amount, to_whom, prev_hash=''):
#    blockchain_dir = os.curdir + '/blockchain/'
#    files = os.listdir(blockchain_dir)             
#    files = sorted([int(i) for i in files])
    files = get_files()
    last_file = files[-1]

    filename = str(last_file + 1)

    prev_hash = get_hash(str(last_file))
#    print(files)
    data = { 'name': name,
             'amount': amount,
             'to_whom': to_whom,
             'hash': prev_hash}

    with open(blockchain_dir + filename, 'w') as file:                
        json.dump(data, file, indent=4, ensure_ascii=False)



def main():
#    write_block(name = '', amount = 5, to_whom = '') 
#     print(check_integrity())
     check_integrity()

if __name__ == '__main__':
    main()
