#!/usr/bin/env python3
"""
Cognitive Debiasing Chatbot - Python Proxy Server
Handles API requests to Anthropic Claude API with CORS support
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, static_folder='.')
CORS(app)  # Enable CORS for all routes

ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
ANTHROPIC_API_URL = 'https://api.anthropic.com/v1/messages'

@app.route('/')
def index():
    """Serve the chatbot HTML"""
    return send_from_directory('.', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Proxy endpoint for Anthropic API calls"""
    try:
        print('📨 Received chat request')

        # Get request data from frontend
        data = request.get_json()

        # Forward request to Anthropic API
        response = requests.post(
            ANTHROPIC_API_URL,
            headers={
                'Content-Type': 'application/json',
                'x-api-key': ANTHROPIC_API_KEY,
                'anthropic-version': '2023-06-01'
            },
            json=data
        )

        # Check status code first
        if response.status_code != 200:
            try:
                response_data = response.json()
            except:
                response_data = {'error': {'message': 'Failed to parse error response', 'type': 'parse_error'}}
            print(f'❌ API Error: {response.status_code}', response_data)
            return jsonify(response_data), response.status_code

        # Get response data for successful response
        response_data = response.json()
        print('✅ API call successful')
        return jsonify(response_data)

    except Exception as e:
        print(f'❌ Server error: {str(e)}')
        return jsonify({
            'error': {
                'message': str(e),
                'type': 'server_error'
            }
        }), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'message': 'Proxy server is running'
    })

if __name__ == '__main__':
    print('\n' + '='*50)
    print('🚀 Cognitive Debiasing Chatbot Server')
    print('='*50)
    print(f'✅ Server running on: http://localhost:3000')
    print(f'✅ API proxy ready at: http://localhost:3000/api/chat')
    print(f'✅ Health check: http://localhost:3000/health')
    print()
    print('📝 Open http://localhost:3000 in your browser')
    print('='*50 + '\n')

    app.run(host='0.0.0.0', port=3000, debug=False)
