def isname(x):
    if x == 'Allen' or x == 'Tom' or x == 'Marvin':
        return True
    else:
        return False
def loading(x):
    lines = []
    with open (x, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines
def processing(x):
    with open ('output.txt', 'w', encoding='utf-8') as f:
        name = ''
        for line in x:
            if isname(line):
                name = line
                continue
            else:
                f.write(name + '：' + line + '\n')
def main():
    data = loading('input.txt')
    processing(data)
main()

