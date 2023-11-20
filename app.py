from flask import Flask, render_template, request

app = Flask(__name__)

# Puzzle questions
questions = [
    "Fun start question: What is one thing we have in common (refer to my hints in the post)?",
    "(Number of male bigs) - (number of female bigs) = ???",
    "Who is the champion of this year (you know what I’m talking about)?",
    "What are the truth values for this sentence:<br>\"I will get to see my big if I solve this puzzle and the weather is not rainy, or if it is rainy but I have an umbrella\".<br> Find the number behind the truth values!<br>I know you are good at 311",
    "Finally, let’s get to some code :)).<br> It’s everyone’s favorite programming language (Python).<br>Obviously, I ban you from using any outside source. Keep academic honesty!!!"
]
questions = [
    {"text": "Fun start question: What is one thing we have in common (refer to my hints in the post)?", "image": "image1.jpg"},
    {"text": "(Number of male bigs) - (number of female bigs) = ???", "image": "image2.jpg"},
    {"text": "Who is the champion of this year (you know what I’m talking about)?", "image": "image3.jpeg"},
    {"text": "What are the truth values for this sentence:<br>\"I will get to see my big if I solve this puzzle and the weather is not rainy, or if it is rainy but I have an umbrella\".<br> Find the number behind the truth values!<br>I know you are good at 311", "image": "image4.jpg"},
    {"text": "Finally, let’s get to some code :)).<br> It’s everyone’s favorite programming language (Python).<br>Obviously, I ban you from using any outside source. Keep academic honesty!!!", "image": "image5.jpg"}
]

# Answer for each question
answers = [
    "Holy Family Catholic Church",
    "9",
    "SKT",
    "251",
    "return s[::-1]"
]

@app.route('/')
def index():
    return render_template('index.html', intro="My Little, please save me!")

@app.route('/puzzle/<int:question_number>', methods=['GET', 'POST'])
def puzzle(question_number):
    if 1 <= question_number <= len(questions):
        if request.method == 'POST':
            user_answer = request.form.get('answer').lower()
            current_level = question_number - 1

            if user_answer == answers[current_level]:
                if question_number == len(questions):
                    return render_template('complete.html')
                else:
                    next_level = question_number + 1
                    return render_template('puzzle.html', question=questions[next_level - 1]["text"], image=questions[next_level - 1]["image"], question_number=next_level)
            else:
                prompt = "Sorry, wrong answer. Try again!"
                return render_template('puzzle.html', question=questions[current_level]["text"], image=questions[current_level]["image"], question_number=question_number, prompt=prompt)

        return render_template('puzzle.html', question=questions[question_number - 1]["text"], image=questions[question_number - 1]["image"], question_number=question_number)
    else:
        return render_template('complete.html')

if __name__ == '__main__':
    app.run(debug=True)
