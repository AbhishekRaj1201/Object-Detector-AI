import app
# from flask import Flask
# from flask_ngrok import run_with_ngrok

# ap=Flask(__name__)
# run_with_ngrok('ap')
# @ap.route('/main')

def main():
    app.App(window_title="Object Detector")


if __name__ == "__main__":
    # ap.run(host='0.0.0.0',port=5000)
    main()