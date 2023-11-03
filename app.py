from flask import Flask

app = Flask(__name__)

@app.route('/welcome/')
@app.route('/welcome/<nama>')
def welcome(nama=None):
    if nama and nama.strip():
        return f"Selamat datang, {nama}!"
    else:
        return "Anonymous"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
