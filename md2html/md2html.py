# coding: utf-8

import markdown, time, os

# file should be utf-8 encoded
FILEPATH = 'log.md'
CODEC = 'utf-8'

TPL = """
<!DOCTYPE HTML>
<html>
<head><meta charset="UTF-8"></head>
<body>
%s	
</body>
</html>
"""

def main():
    text = open(FILEPATH).read()
    html = markdown.markdown(
        text.decode(CODEC),
        extensions=[
            'markdown.extensions.tables', 
            'markdown.extensions.toc'
            ]
        ).encode(CODEC)
    with open( os.path.splitext(FILEPATH)[0] + '.html', 'w' ) as f:
        f.write(TPL % html)

if __name__ == "__main__":
    main()
    print 'done'
    time.sleep(2)
    
    
