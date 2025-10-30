"""Flask app with a small decision-tree based predictor.

This file reformats the pasted machine-learning decision tree into a Python
predict function and adds input validation so the app can render
`ml2.html` with a prediction.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


def predict(churn_category: float, tenure_months: float) -> str:
    """Predict label based on the pasted decision tree.

    The original content represented a decision tree that primarily checks
    `Churn_Category` and then `Tenure_in_Months`. This function encodes that
    logic in a straightforward, readable form.

    Returns one of: 'Churned', 'Joined', 'Stayed'.
    """
    cc = churn_category
    t = tenure_months

    # Top levels of the tree: many branches lead to 'Churned'
    if cc <= 0.36:
        return "Churned"
    if cc <= 1.37:
        return "Churned"
    if cc <= 2.78:
        return "Churned"
    if cc <= 3.65:
        return "Churned"
    if cc <= 4.96:
        return "Churned"

    # cc > 4.96: deeper branch that checks tenure
    if t > 41.97:
        return "Stayed"
    # t <= 41.97
    if t > 23.06:
        return "Stayed"
    # t <= 23.06
    if t > 14.50:
        return "Stayed"
    # t <= 14.50
    if t > 13.59:
        return "Stayed"
    # t <= 13.59
    if t <= 3.67:
        return "Joined"
    return "Stayed"


@app.route('/')
def home():
    return render_template('ml1.html')


@app.route('/result', methods=['POST'])
def result():
    # Read form values safely and convert to floats with fallbacks
    raw_cc = request.form.get('Churn Category', '')
    raw_tenure = request.form.get('Tenure in Months', '')

    try:
        churn_category = float(raw_cc)
    except (ValueError, TypeError):
        churn_category = 0.0

    try:
        tenure_months = float(raw_tenure)
    except (ValueError, TypeError):
        tenure_months = 0.0

    label = predict(churn_category, tenure_months)

    # Pass back values to the template for display/debugging
    return render_template('ml2.html', result=label, churn_category=churn_category, tenure_months=tenure_months)


if __name__ == '__main__':
    # Only run when executed directly; easier for import and testing
    app.run(debug=True)