from flask import Flask, jsonify, request
import re

application = Flask(__name__)


@application.route('/check', methods=['GET'])
def check():
    if 'q' not in request.args:
        return 'program requires question arguements', 200

    if request.args['q'] == 'Ping':
        return 'OK'
    elif request.args['q'] == 'Years':
        return '3'
    elif request.args['q'] == 'Referrer':
        return 'Linkedin'
    elif request.args['q'] == 'Resume':
        return 'https://www.linkedin.com/in/yitao-sun-146015104/'
    elif request.args['q'] == 'Email Address':
        return 'yitao.sun@yahoo.com'
    elif request.args['q'] == 'Position':
        return 'Data Pipeline Engineer'    
    elif request.args['q'] == 'Name':
        return 'Yitao Sun'
    elif request.args['q'] == 'Degree':
        return 'Baruch College - Master of Science Quantitative Methods and Modeling'
    elif request.args['q'] == 'Phone':
        return '6469123830'
    elif request.args['q'] == 'Puzzle':
        puzzle = request.args.get('d')
        matrix = get_matrix(puzzle)
        out_matrix = process_matrix(matrix)
        out_string = form_string(out_matrix)
        return out_string
    elif request.args['q'] == 'Status':
        return 'Yes'
    elif request.args['q'] == 'Source':
        return 'https://github.com/oooook0/Exercise'

    return 'Unseen questions pattern', 200


def get_matrix(sentence):
    m = re.search('Please solve this puzzle:',sentence)
    clean_string = sentence[:m.start()] + sentence[m.end():]
    token = clean_string.split('\n')
    A = list(token[2])[1:]
    B = list(token[3])[1:]
    C = list(token[4])[1:]
    D = list(token[5])[1:]
    out = []
    out.append(A)
    out.append(B)
    out.append(C)
    out.append(D)
    return out

def process_matrix(a):
    for i in range(4):
        a[i][i] = '='
    for index, row in enumerate(a):
        if '>' in row:
            ind = row.index('>')
            a[ind][index] = '<'
        if '<' in row:
            ind = row.index('<')
            a[ind][index] = '>'
    for index, row in enumerate(a):
        ind = [i for i,val in enumerate(row) if val=='-']
        if len(ind) == 2:
            if '>' in row:
                a[index] = ['>']*4
                a[index][index] = '='
            if '<' in row:
                a[index] = ['<']*4
                a[index][index] = '=' 
    for index, row in enumerate(a):
        if '-' in row:
            ind = row.index('-')
            if a[ind][index] == '>':
                a[index][ind] = '<'
            else:
                a[index][ind] = '>'
    return a

def form_string(a):
    base_string = ' ABCD\n'
    for i in zip(['A','B','C','D'], a):
        string = i[0] + ''.join(i[1]) + '\n'
        base_string += string
    return base_string



if __name__ == "__main__":
    application.run(debug=True,host='0.0.0.0')
