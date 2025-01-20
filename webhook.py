from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/notifications', methods=['POST'])
def handle_notifications():
    """Handle notifications and validation from Microsoft Graph."""
    validation_token = request.args.get('validationToken')
    
    if validation_token:
        # Decode the validation token and return it as plain text
        response = make_response(validation_token, 200)
        response.headers['Content-Type'] = 'text/plain'
        return response

    # Handle actual notifications (if this is not a validation request)
    notification_data = request.json
    print("Received notification:", notification_data)

    # Respond with HTTP 202 to acknowledge the notification
    return '', 202


if __name__ == '__main__':
    app.run(port=5000, debug=True)
