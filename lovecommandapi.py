@app.route('/get_toys', methods=['POST'])
def get_toys():
    url = 'https://{domain}:{httpsPort}/command'
    headers = {'X-platform': 'YourApplicationName'}
    params = {'command': 'GetToys'}
    response = requests.post(url, headers=headers, json=params)
    return jsonify(response.json())

@app.route('/get_toy_name', methods=['POST'])
def get_toy_name():
    url = 'https://{domain}:{httpsPort}/command'
    headers = {'X-platform': 'YourApplicationName'}
    params = {'command': 'GetToyName'}
    response = requests.post(url, headers=headers, json=params)
    return jsonify(response.json())

@app.route('/function', methods=['POST'])
def control_function():
    url = 'https://{domain}:{httpsPort}/command'
    headers = {'X-platform': 'YourApplicationName'}
    params = request.get_json()
    params['command'] = 'Function'
    response = requests.post(url, headers=headers, json=params)
    return jsonify(response.json())

@app.route('/pattern', methods=['POST'])
def send_pattern():
    url = 'https://{domain}:{httpsPort}/command'
    headers = {'X-platform': 'YourApplicationName'}
    params = request.get_json()
    params['command'] = 'Pattern'
    params['apiVer'] = 2
    response = requests.post(url, headers=headers, json=params)
    return jsonify(response.json())

@app.route('/preset', methods=['POST'])
def send_preset():
    url = 'https://{domain}:{httpsPort}/command'
    headers = {'X-platform': 'YourApplicationName'}
    params = request.get_json()
    params['command'] = 'Preset'
    response = requests.post(url, headers=headers, json=params)
    return jsonify(response.json())
