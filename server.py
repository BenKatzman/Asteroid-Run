from flask import Flask

players = []
user1 = []
user2 = []

app = Flask(__name__)

@app.route('/start/<a>')
def start(a):
    players.append(a)
    if len(players) == 2:
        return '2'
    else:
        return '1'

@app.route('/send/<i>/<s>')
def send(i, s):
    if i == '1':
        user2.append(s)
        return 'Done'
    else:
        user1.append(s)
        return 'Done'

@app.route('/recieve/<u>')
def recieve(u):
    if u == '1':
        if len(user1) == 1:
            return user1[0]
        elif len(user1) > 1:
            for i in user1:
                if user1.index(i) == len(user1):
                    return i
                else:
                    return i+','
    elif u == '2':
        if len(user2) == 1:
            return user2[0]
        elif len(user2) > 1:
            for i in user2:
                if user2.index(i) == len(user2):
                    return i
                else:
                    return i+','



if __name__ == '__main__':
    app.run(port=8080)
