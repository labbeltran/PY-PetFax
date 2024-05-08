from flask import (Blueprint, render_template, request)
bp= Blueprint('submit', __name__, url_prefix='/facts')


@bp.route('/new', methods=('GET', 'POST'))
def new_fact():
    if request.method == 'POST':
        name = request.form.get('name')
        pet_fact = request.form.get('pet_fact')
        # Process form data
        print("Name:", name)
        print("Pet Fact:", pet_fact)
        return 'Form submitted successfully!'
    # Return a response if the request method is not POST (optional)
    else:
        return render_template('new_fact.html')