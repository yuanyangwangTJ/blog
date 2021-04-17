#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Function: formatted text document by adding newline
# Author: king

def main():
    print('This python script help you formatted text document.')
    fin = input('Input the file location : ')
    fout = input('Input the new file location: ')
    print('begin...')

    MAX_SIZE = 78
    newlines = ''

    with open(fin, encoding='utf-8') as fp:
        lines = fp.readlines()

        for line in lines:
            content = line.encode('gbk')

            while len(content) > MAX_SIZE + 1:
                newcontent = content[:MAX_SIZE]
                content = content[MAX_SIZE:]
                try:
                    newline = newcontent.decode('gbk')
                    newlines += newline + '\n'
                except:
                    newcontent += content[:1]
                    content = content[1:]
                    newline = newcontent.decode('gbk')

            newlines += content.decode('gbk')

    with open(fout, 'w', encoding='utf-8') as fo:
        fo.write(newlines)

    print('Finish Done!')
    pass

if __name__ == '__main__':
    main()
