"""
remove unnecessary empty lines.

sample: 'line1\n\n\nline2\n\nline3' --> 'line1\nline2\nline3'
"""

def remove_lines(lines):
    useless_indexes = []
    valid_lines = []
    for i in range(len(lines)):
        try:
            if lines[i] == lines[i+1] == u'':
                useless_indexes.append(i+1)
            else:
                valid_lines.append(lines[i])
        except IndexError:
            valid_lines.append(lines[i])

    # print 'useless indexes:', useless_indexes
    return '\n'.join(valid_lines)

def main():
    import clipboard
    ret_text = remove_lines(clipboard.paste().splitlines())
    clipboard.copy(ret_text)
    print 'OUTPUT:\n\n', ret_text

if __name__ == '__main__':
    main()
    input()
