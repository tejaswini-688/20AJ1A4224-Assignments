from flask import Flask
app=Flask(__name__)
@app.route('/')
def fun():
    return("Welcome to the Virtual world")
@app.route('/ready')
def mid():
    return("It is our creative world")
@app.route('/end')
def end():
    return("Enjoying ourselves")
if __name__=='__main__':
    app.run()