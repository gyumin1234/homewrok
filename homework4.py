from flask import Flask, render_template, request, redirect, url_for
import random
import sqlite3

app = Flask(__name__)

# sqlite3 데이터베이스 초기화 및 연결
conn = sqlite3.connect('rps_records.db')
c = conn.cursor()

# 데이터베이스에 테이블 생성
c.execute('''CREATE TABLE IF NOT EXISTS rps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_choice TEXT,
                computer_choice TEXT,
                result TEXT
            )''')
conn.commit()


@app.route('/')
def index():
    # 승/무/패 통계 및 게임 기록 가져오기
    c.execute("SELECT COUNT(*) FROM rps")
    total_games = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM rps WHERE result='win'")
    wins = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM rps WHERE result='tie'")
    ties = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM rps WHERE result='lose'")
    losses = c.fetchone()[0]
    game_records = c.execute("SELECT * FROM rps").fetchall()
    return render_template('index.html', total_games=total_games, wins=wins, ties=ties, losses=losses, game_records=game_records)


@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = get_result(user_choice, computer_choice)

    # 결과를 데이터베이스에 저장
    c.execute("INSERT INTO rps (user_choice, computer_choice, result) VALUES (?, ?, ?)",
              (user_choice, computer_choice, result))
    conn.commit()

    return redirect(url_for('index'))


def get_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'win'
    else:
        return 'lose'


if __name__ == '__main__':
    app.run(debug=True)
