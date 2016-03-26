from flask import render_template
from app import app
from app.forms import BandForm

@app.route('/')
@app.route('/index')
def index():
    band = BandForm()
    return render_template('index.html',
                           title='Home',
                           form=band)

@app.route('/band', methods=['POST'])
def band():
    form = BandForm()
    if form.validate_on_submit():
        if form.band.data.lower() == 'meshuggah':
            return render_template('result.html',
                                   title='Result',
                                   result="You were right!")
        else:
            return render_template('result.html',
                                   title='Result',
                                   result="wrong motherfucker")
    return render_template('index.html',
                           title='Home',
                           form=form)

if __name__ == "__main__":
    app.config['SECRET_KEY'] = 'zomg'
    app.run(debug=True, host='0.0.0.0')
