from flask import Flask, render_template, jsonify
import test  # ваш основной скрипт
import threading

app = Flask(__name__)

# Запускаем предсказания в фоновом режиме
def run_predictor():
    test.predict_and_compare_next_spin()

thread = threading.Thread(target=run_predictor)
thread.daemon = True
thread.start()

@app.route('/')
def home():
    last_spins = test.get_last_5_spins()
    return render_template('index.html', spins=last_spins)

@app.route('/api/prediction')
def get_prediction():
    last_spins = test.get_last_5_spins()
    return jsonify({
        "prediction": "ten",  # Здесь будет ваше предсказание
        "last_spins": last_spins
    })

if __name__ == '__main__':
    app.run(debug=True)