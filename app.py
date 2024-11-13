from flask import Flask, render_template, request

app = Flask(__name__)

singers = ['Ariana Grande', 'Ed Sheeran', 'Beyoncé', 'Bruno Mars', 'Taylor Swift']
votes = {singer: 0 for singer in singers}

@app.route('/')
def home():
    return render_template('index.html', singers=singers)

@app.route('/vote', methods=['POST'])
def vote():
    selected_singer = request.form['singer']
    if selected_singer in votes:
        votes[selected_singer] += 1
    return render_template('results.html', votes=votes)

if __name__ == '__main__':
    app.run(debug=True)
