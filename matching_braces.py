s = []

def matching_braces(input):
    for char in input:
        if char in ['{','(','[']:
            s.append(char)

        if (len(s)) == 0:
            return False

        if char == '}':
            result_char = s.pop()
            if result_char == ')' or result_char == ']':
                return False

        elif char == ')':
            result_char = s.pop()
            if result_char == '}' or result_char == ']':
                return False

        elif char == ']':
            result_char = s.pop()
            if result_char == ')' or result_char == '}':
                return False


    if len(s) != 0:
        return False
    else:
        return True


string = input()
result = matching_braces(string)

if(result):
    print('balanced')
else:
    print('Unbalanced')
