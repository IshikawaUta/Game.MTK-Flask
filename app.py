from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

OPERATIONS = ['+', '-', '*', '/']
NUM_QUESTIONS = 5
score = 0
question_index = 0
num1 = 0
num2 = 0
operation = ''
correct_answer = 0
feedback = None
feedback_class = None

def generate_question():
    global num1, num2, operation, correct_answer
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(OPERATIONS)

    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        if num1 < num2:
            num1, num2 = num2, num1
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    elif operation == '/':
        # Ensure integer results for division where num1 is divisible by num2
        num2 = random.randint(1, 10)
        multiplier = random.randint(1, 10)
        num1 = num2 * multiplier
        correct_answer = num1 // num2
        if num2 == 0:
            num2 = 1 # Safety net, though should not be reached with new logic

    return f"{num1} {operation} {num2} = ?"

@app.route('/')
def index():
    global score, question_index, feedback, feedback_class
    score = 0
    question_index = 0
    feedback = None
    feedback_class = None
    return redirect(url_for('play'))

@app.route('/play', methods=['GET', 'POST'])
def play():
    global score, question_index, correct_answer, feedback, feedback_class

    if request.method == 'POST':
        user_answer = request.form.get('answer')
        try:
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                score += 1
                feedback = "Jawaban Benar!"
                feedback_class = "correct"
            else:
                feedback = f"Jawaban Salah. Jawaban yang benar adalah {correct_answer}."
                feedback_class = "incorrect"
        except ValueError:
            feedback = "Input tidak valid. Masukkan angka."
            feedback_class = "incorrect"

        question_index += 1
        if question_index < NUM_QUESTIONS:
            return redirect(url_for('play'))
        else:
            return redirect(url_for('results'))

    question = generate_question()
    return render_template('play.html', question=question, question_number=question_index + 1, total_questions=NUM_QUESTIONS, feedback=feedback, feedback_class=feedback_class)

@app.route('/results')
def results():
    return render_template('results.html', score=score, total_questions=NUM_QUESTIONS)

if __name__ == '__main__':
    app.run(debug=True)