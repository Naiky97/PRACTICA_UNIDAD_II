from flask import Flask, render_template, request, redirect
from ejercicio import a_piramide

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='área de una piramide')


@app.route('/exec_equation', methods=['GET', 'POST'])
def execute() -> 'html':
    ab = int(request.form['ab'])
    al = int(request.form['al'])
    title = 'Tu resultado es: '
    result = a_piramide(ab, al)
    return render_template('results.html',
                           the_title=title,
                           the_ab=ab,
                           the_al=al,
                           the_result=result, )


if __name__ == '__main__':
    app.run('localhost', 5001, debug=True)
