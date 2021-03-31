import webbrowser

def main():
    f = open('test1.html', 'w')
    message = """<html>
                <head></head>
                <body><p>Hello World!</p></body>
                </html>"""

    f.write(message)
    f.close()
    webbrowser.open('test1.html')

    while True:
        user_msg = input('input user message here-> ')
        f = open('test1.html', 'w')
        message = (f"""<html>
                    <head></head>
                    <body><p>Hello World! {user_msg}</p></body>
                    </html>""")

        f.write(message)
        f.close()

if __name__ == '__main__':
    main()