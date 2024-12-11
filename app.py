##  Flask app routing

from flask import Flask,render_template,request

## create a flask application
app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "<h1>Welcome to my flask first page</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "<h2>Welcome to the index page</h2>"

## variable rule : if we pass a particular variable with defining required data type.
@app.route("/success/<int:score>")
def success(score):
    return "The person is passed and the score is:" + str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person is failed and the score is:" + str(score)

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        #return redirect(url_for(result,score=average_marks))


        return render_template('result.html',results=average_marks)


if __name__=="__main__":
    app.run(debug=True)

