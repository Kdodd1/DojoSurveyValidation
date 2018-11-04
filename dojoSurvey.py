from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)

app.secret_key = "secret"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    if request.form['name'] == "" and request.form['comment'] == "":
        flash("*The name field cannot be empty")
        flash("*Please leave a comment")
        return redirect('/')
    elif len(request.form['name']) <1:
        flash("*The name field cannot be empty.")
        session['comment'] = request.form['comment']
        return redirect('/')
    elif len(request.form['comment']) <1:
        flash("*Please leave a comment")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("*Please dont exceed 120 characters")
        session['comment'] = request.form['comment']
        return redirect('/')

    session.clear()
    return render_template("result.html")

@app.route('/danger')
def danger():
	print("a user tried to vist /danger")
	return redirect("/")



if __name__=="__main__":
    app.run(debug=True) 