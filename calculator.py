from flask import Flask, render_template, request

app = Flask(__name__)

# Home page with calculator form
@app.route('/')
def calculator():
    return render_template('calculator.html')

# Route for processing the calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        # Perform the operation based on user input
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                result = "Cannot divide by zero!"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation!"
            
    except ValueError:
        result = "Invalid input! Please enter valid numbers."
    
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
