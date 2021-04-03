# import webbrowser
# import cgi

# def main():
#     # f = open('test1.html', 'w')
#     # message = """<html>
#     #             <head></head>
#     #             <body><p>Hello World!</p></body>
#     #             </html>"""

#     # f.write(message)
#     # f.close()
#     webbrowser.open('test1.html')

#     while True:
#         user_msg = input('input user message here-> ')
#         f = open('test1.html', 'w')
#         message = (f"""<html>
#                     <head></head>
#                     <body><p>Hello World!</p></body>
#                     <form name="search" action="/cgi-bin/test.py" method="get">
#                     Search: <input type="text" name="searchbox">
#                     <input type="submit" value="Submit">
#                     </form> 
#                     </html>""")
#         # form = cgi.FieldStorage()
#         # searchterm =  form.getvalue('searchbox')
#         # print(f"{searchterm}")

#         f.write(message)
#         f.close()

# if __name__ == '__main__':
#     main()

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('test1.html')

@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    return variable

if __name__ == '__main__':
    app.run(debug=True)
