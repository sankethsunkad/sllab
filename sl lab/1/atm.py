from flask import Flask, render_template, request, session

app = Flask(__name__)

app.secret_key = "secret"


@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        balance = session["balance"]
        visits = session["visits"]
    except KeyError:
        balance = session["balance"] = 8000
        visits = session["visits"]=0

    if request.method == "GET":
        return render_template("index.html", balance=balance, msg="")

    if request.method == "POST":

        if request.form["amount"] == "":
            msg = "Amount is required"
            return render_template("index.html", balance=balance, msg=msg,visits=visits)

        if int(request.form["amount"]) < 0:
            msg = "Cannot enter negative amount"
            return render_template("index.html", balance=balance, msg=msg,visits=visits)

        if request.form["action"] == 'Withdraw':

            if int(request.form["amount"]) > session["balance"]:
                msg = "Cannot withdraw amount greater than balance"
                return render_template("index.html", balance=balance, msg=msg,visits=visits)

            elif int(request.form["amount"]) > 5000:
                msg = "Cannot withdraw amount greater than 5000"
                return render_template("index.html", balance=balance, msg=msg,visits=visits)

            else:
                if session["visits"]<5:
                    balance = balance - int(request.form["amount"])
                    visits=visits+1
                    session["visits"] = visits
                    session["balance"] = balance
                    msg = "Money Withdrawn"
                    return render_template("index.html", balance=balance, msg=msg,visits=visits)
                else:
                    msg="Transaction limit reached"
                    return render_template("index.html", balance=balance, msg=msg, visits=visits)

        elif request.form["action"] == 'Deposit':

            balance = balance + int(request.form["amount"])
            session["balance"] = balance
            msg = "Money Deposited"
            return render_template("index.html", balance=balance, msg=msg,visits=visits)


if __name__ == '__main__':
    app.run()