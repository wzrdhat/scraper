from flask import Flask, views, render_template

@views.route('/contact')
def contact():
    return render_template('contact.html')