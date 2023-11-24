from flask import Flask, request, render_template
import random

app = Flask(__name__)

DEFAULT_MESSAGES = [
    "Makan patty itu spongebob",
    "Berdansalah, Patrick",
    "Pergi ke rumah Squidward",
    "Belajar di Krusty Krab",
    "Kamu cantik masyaallah",
    "Bismillah ip semester 3 naik",
    "Susah sekali tugas minggu ini",
    "Mau magang di Jakarta aamiin",
    "Semester 4 semoga tetap sehat",
    "Semoga lulus tepat waktu"
]

@app.route('/')
def puja_kerang_ajaib():
    name = request.args.get('nama')
    if name:
        message = f"{name}, {random.choice(DEFAULT_MESSAGES)}"
    else:
        message = random.choice(DEFAULT_MESSAGES)
    return render_template('index.html', message=message)

@app.route('/', methods=['POST'])
def puja_kerang_ajaib_post():
    name = request.form.get('nama')
    if name:
        message = f"Selamat datang, {name}, anda berhasil masuk ke Puja Kerang Ajaib"
    else:
        message = "Silakan masukkan nama Anda dalam parameter 'nama'"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()