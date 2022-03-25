from flask import Flask, make_response, request, render_template
from werkzeug.utils import redirect

app = Flask(__name__, template_folder='./')


sessionCookie = 'session_id'
sessionID = 'c2738d39-293a-43e9-a683-f1f82b06a229'
flag = 'flag'


@app.route('/', methods=['GET', 'POST'])
def passwords():
    if request.method == 'GET':
        if request.cookies.get(sessionCookie) == sessionID:
            return render_template('passwords.html')

        return render_template('login.html')

    if request.form['username'] == 'admin' and request.form['password'] == 'admin':
        resp = make_response(redirect('/'))
        resp.set_cookie(sessionCookie, sessionID)
        return resp

    return redirect('/')


@app.post('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie(sessionCookie, '', expires=0)
    return resp


if __name__ == '__main__':
    app.run('', 8080)
