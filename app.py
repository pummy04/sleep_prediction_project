from flask import Flask, render_template, request

app = Flask(__name__)

# Load your trained model (replace 'model.pkl' with the actual path to your model)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        try:
            age = int(request.form.get('age'))
            sleep_hours = float(request.form.get('sleep_hours'))
            exercise = request.form.get('exercise')
            diet = request.form.get('diet')
        except ValueError:
            error = "Invalid input. Please enter valid numbers for age and sleep hours."
            return render_template('prediction.html', error=error)

        # Input validation
        if age < 0 or age > 120:
            error = "Please enter a valid age (between 0 and 120)."
            return render_template('prediction.html', error=error)

        if sleep_hours < 0 or sleep_hours > 24:
            error = "Please enter valid sleep hours (between 0 and 24)."
            return render_template('prediction.html', error=error)

        # Example of prediction logic (replace with your model's prediction)
        # Convert inputs into a format suitable for your model
        # input_data = [[age, sleep_hours, exercise, diet]]  # Modify according to your model
        # prediction = model.predict(input_data)

        # Placeholder insights for now
        sleep_insight = "Based on your input, it's recommended to get at least 7-9 hours of sleep."
        health_insight = "A healthy diet and regular exercise can greatly improve your well-being."

        # Tailoring the insights based on user inputs
        if exercise == "yes":
            health_insight = "Great job! Regular exercise is key to maintaining good health."
        else:
            health_insight = "Consider incorporating regular exercise into your routine for better health."

        if diet == "poor":
            diet_insight = "A poor diet can negatively affect your health. Try improving your eating habits."
        elif diet == "average":
            diet_insight = "Your diet is average, but there's always room for improvement."
        else:
            diet_insight = "You're doing great with your diet!"

        # Combine all insights
        combined_insight = f"{sleep_insight} {health_insight} {diet_insight}"

        # Render the results page with the insights
        return render_template('results.html',
                               age=age,
                               sleep_hours=sleep_hours,
                               exercise=exercise,
                               diet=diet,
                               sleep_insight=sleep_insight,
                               health_insight=health_insight,
                               diet_insight=diet_insight,
                               combined_insight=combined_insight)

    # Handle GET request
    return render_template('prediction.html')

@app.route('/age_info', methods=['GET', 'POST'])
def age_info():
    if request.method == 'POST':
        try:
            # Get the age input
            age = int(request.form.get('age'))
        except ValueError:
            error = "Invalid input. Please enter a valid number for age."
            return render_template('age_info.html', error=error)

        # Input validation
        if age < 0 or age > 120:
            error = "Please enter a valid age (between 0 and 120)."
            return render_template('age_info.html', error=error)

        # Example insights based on the age entered
        if age < 18:
            age_specific_insight = "It's important for children and teenagers to get plenty of sleep, ideally 8-10 hours."
        elif 18 <= age <= 60:
            age_specific_insight = "For adults, 7-9 hours of sleep is optimal for maintaining good health."
        else:
            age_specific_insight = "For older adults, around 7-8 hours of sleep can help maintain cognitive and physical health."

        # Render the age-specific insights
        return render_template('age_results.html', age=age, age_specific_insight=age_specific_insight)

    # Handle GET request
    return render_template('age_info.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)





