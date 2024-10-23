from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def bin_lookup(bin_number):
    url = f"https://binov.net/api/{bin_number}"  # Replace with the actual API endpoint
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    try:
        # Send a GET request to the API
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            bin_data = response.json()
            
            # Extract and return relevant information
            return {
                "bin": bin_data.get("bin"),
                "bank": bin_data.get("bank"),
                "card_type": bin_data.get("type"),
                "card_brand": bin_data.get("brand"),
                "country": bin_data.get("country"),
                "api": "API by @kiltes"
            }
        else:
            return {"error": f"Failed to fetch data. Status code: {response.status_code}", "api": "API by @kiltes"}

    except Exception as e:
        return {"error": str(e), "api": "API by @kiltes"}

@app.route('/lookup', methods=['GET'])
def lookup():
    bin_number = request.args.get('bin')
    if not bin_number:
        return jsonify({"error": "Please provide a BIN number.", "api": "API by @kiltes"}), 400

    result = bin_lookup(bin_number)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
