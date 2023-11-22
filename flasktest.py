from flask import Flask, render_template
import matplotlib
matplotlib.use('Agg') #non-interactive backend
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__, template_folder='template')

def generate_plot():
    x = [1, 2, 3, 4, 5]
    y = [i ** 2 for i in x]

    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Sample Plot')

    img = io.BytesIO()
    plt.saveflg(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue().decode)
    plt.close() #close plot

@app.route('/')
def plot():
    plot_url = generate_plot()
    return render_template('plot.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)