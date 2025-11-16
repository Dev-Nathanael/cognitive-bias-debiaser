# Setup Guide - Cognitive Bias Debiaser

This guide provides detailed instructions for setting up and running the Cognitive Bias Debiaser chatbot.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Application](#running-the-application)
5. [Deployment](#deployment)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Configuration](#advanced-configuration)

## Prerequisites

### Required Software

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **pip** - Usually included with Python
- **Modern web browser** - Chrome, Firefox, Safari, or Edge (latest versions)
- **Anthropic API Key** - [Get API key](https://console.anthropic.com/)

### Check Prerequisites

```bash
# Check Python version (should be 3.8 or higher)
python --version
# or
python3 --version

# Check pip is installed
pip --version
# or
pip3 --version
```

## Installation

### Step 1: Clone or Download the Repository

```bash
# If using Git
git clone <repository-url>
cd cognitive-bias-debiaser

# Or download and extract the ZIP file, then navigate to the folder
cd cognitive-bias-debiaser
```

### Step 2: Install Python Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Or if you're using Python 3 explicitly
pip3 install -r requirements.txt
```

This will install:
- Flask 3.0.0 (web framework)
- flask-cors 4.0.0 (CORS handling)
- requests 2.31.0 (HTTP client)
- python-dotenv 1.0.0 (environment variables)

### Step 3: Verify Installation

```bash
# Check that Flask was installed correctly
python -c "import flask; print(flask.__version__)"
```

Should output: `3.0.0`

## Configuration

### Step 1: Get Anthropic API Key

1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key (you won't be able to see it again)

### Step 2: Create Environment File

Create a file named `.env` in the project root directory:

```bash
# On Linux/Mac
touch .env

# On Windows
type nul > .env
```

### Step 3: Add API Key to Environment File

Open `.env` in a text editor and add:

```
ANTHROPIC_API_KEY=your-api-key-here
```

Replace `your-api-key-here` with your actual Anthropic API key.

**Example:**
```
ANTHROPIC_API_KEY=sk-ant-api03-abc123xyz789...
```

**Important:**
- Never commit the `.env` file to version control
- The `.gitignore` file is already configured to exclude `.env`
- Keep your API key secret

### Step 4: Verify Configuration

```bash
# Check that .env file exists
ls -la .env

# On Windows
dir .env
```

## Running the Application

### Development Mode

#### Start the Server

```bash
# Run the Flask server
python server.py

# Or if using Python 3 explicitly
python3 server.py
```

You should see output like:
```
Starting Cognitive Debiasing Chatbot Server
Server running on http://0.0.0.0:3000
API configured and ready
```

#### Access the Application

1. Open your web browser
2. Navigate to: `http://localhost:3000`
3. The chatbot interface should load

#### Stop the Server

Press `Ctrl+C` in the terminal to stop the server.

### Running on a Different Port

If port 3000 is already in use, modify `server.py`:

```python
# Change this line at the bottom of server.py
app.run(host='0.0.0.0', port=3000)  # Change 3000 to your desired port
```

For example, to use port 8080:
```python
app.run(host='0.0.0.0', port=8080)
```

Then access via `http://localhost:8080`

### Background Mode (Linux/Mac)

To run the server in the background:

```bash
# Start in background
nohup python server.py > server.log 2>&1 &

# Check if running
ps aux | grep server.py

# View logs
tail -f server.log

# Stop the server
pkill -f server.py
```

## Deployment

### Production Considerations

For production deployment, consider:

1. **Use a Production WSGI Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:3000 server:app
   ```

2. **Enable HTTPS**
   - Use a reverse proxy like Nginx
   - Obtain SSL certificate (Let's Encrypt)

3. **Set Environment Variables Securely**
   - Don't use `.env` files in production
   - Use system environment variables or secrets management

4. **Configure CORS Properly**
   - Update CORS settings in `server.py` for your domain
   - Don't use `'*'` in production

### Example Nginx Configuration

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Docker Deployment (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}

EXPOSE 3000

CMD ["python", "server.py"]
```

Build and run:
```bash
docker build -t cognitive-bias-debiaser .
docker run -p 3000:3000 -e ANTHROPIC_API_KEY=your-key cognitive-bias-debiaser
```

## Troubleshooting

### Server Won't Start

**Error: `ModuleNotFoundError: No module named 'flask'`**

Solution:
```bash
pip install -r requirements.txt
```

**Error: `Port 3000 is already in use`**

Solution: Change port in `server.py` or kill the process using port 3000:
```bash
# Find process using port 3000
lsof -i :3000  # Mac/Linux
netstat -ano | findstr :3000  # Windows

# Kill the process
kill -9 <PID>  # Mac/Linux
taskkill /PID <PID> /F  # Windows
```

**Error: `ANTHROPIC_API_KEY not found`**

Solution:
1. Verify `.env` file exists in project root
2. Check the file contains: `ANTHROPIC_API_KEY=your-key`
3. Restart the server after creating/editing `.env`

### Frontend Issues

**Error: "Analysis Failed" or "Re-analysis Failed"**

Possible causes:
1. **Invalid API Key**
   - Check API key in `.env` is correct
   - Verify key is active in Anthropic Console

2. **No API Credits**
   - Check your Anthropic account balance
   - Add credits if needed

3. **Network Issues**
   - Check internet connection
   - Verify firewall isn't blocking requests to api.anthropic.com

4. **Rate Limiting**
   - You may have exceeded API rate limits
   - Wait a few minutes and try again

**Blank Page or Loading Issues**

Solution:
1. Check browser console for errors (F12 → Console)
2. Verify all CDN libraries loaded:
   - React
   - ReactDOM
   - Babel
   - Marked
   - DOMPurify
   - idb
3. Try hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
4. Clear browser cache

**Session Not Saving**

Solution:
1. Enable cookies and local storage in browser
2. Check IndexedDB is supported (all modern browsers)
3. Clear browser data and try again

### API Issues

**High API Costs**

- Each session typically costs $0.10-0.30
- Monitor usage in Admin Panel
- Consider setting up API usage alerts in Anthropic Console

**Slow Response Times**

- Claude API typically responds in 2-5 seconds
- Longer delays may indicate:
  - Network congestion
  - API service issues
  - Very complex analysis requests

### Browser Compatibility

**Issue: Features Not Working**

Minimum browser versions:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

Check your browser version and update if needed.

## Advanced Configuration

### Customize Question Bank

Edit `QUESTION_BANK` in `index.html` (around line 200):

```javascript
const QUESTION_BANK = [
    {
        id: "Q001",
        question: "Your custom question here?",
        biases_addressed: ["confirmation_bias"],
        question_type: "insight"
    },
    // Add more questions...
];
```

### Modify Context Questions

Edit `CONTEXT_QUESTIONS` in `index.html` (around line 250):

```javascript
const CONTEXT_QUESTIONS = [
    {
        id: "custom_question",
        question: "Your question?",
        type: "text"
    },
    // Add more questions...
];
```

### Adjust Bias Detection Sensitivity

Modify the AI prompts in the API calls (search for `callAnthropicAPIWithTools` in `index.html`).

### Change Server Host/Port

In `server.py`, modify the last line:

```python
app.run(
    host='0.0.0.0',  # '0.0.0.0' = all interfaces, 'localhost' = local only
    port=3000,       # Change port number
    debug=False      # Set True for development (auto-reload)
)
```

### Enable Debug Mode

**Warning: Only use in development, never in production**

In `server.py`:
```python
app.run(host='0.0.0.0', port=3000, debug=True)
```

This enables:
- Auto-reload on code changes
- Detailed error messages
- Interactive debugger

### CORS Configuration

To restrict CORS to specific domains (production), edit `server.py`:

```python
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://yourdomain.com"],
        "methods": ["POST"],
        "allow_headers": ["Content-Type"]
    }
})
```

### Custom Styling

The application uses Tailwind CSS via CDN. To customize:

1. Add custom CSS in the `<style>` section of `index.html`
2. Or modify Tailwind classes directly in the React components

### Data Retention

By default, the app keeps:
- Last 100 sessions in IndexedDB
- All question statistics
- Session expires after 1 hour

To change retention in `index.html`:

```javascript
// Search for "Keep only last 100 sessions" and change:
if (allSessions.length > 100) {  // Change 100 to your desired number
```

## Testing

### Basic Functionality Test

1. Start the server
2. Open browser to `http://localhost:3000`
3. Answer a few context questions
4. Verify questions appear and accept responses
5. Check for API errors in browser console
6. Verify session persists after page refresh

### API Connection Test

```bash
# Test health endpoint
curl http://localhost:3000/health

# Should return: {"status": "ok"}
```

### Load Testing

For production, test with tools like:
- Apache Bench (ab)
- Locust
- JMeter

Example:
```bash
ab -n 100 -c 10 http://localhost:3000/
```

## Performance Optimization

### Frontend

- All CDN libraries are production minified versions
- Minimal bundle size (single HTML file)
- IndexedDB for efficient local storage
- No unnecessary re-renders

### Backend

- Lightweight Flask proxy (no heavy processing)
- Stateless design (scales horizontally)
- Simple request forwarding

### Database

- Client-side only (no server database needed)
- IndexedDB handles up to 50MB+ easily
- Automatic cleanup of old sessions

## Security Best Practices

1. **Never commit `.env`** - Already in `.gitignore`
2. **Rotate API keys regularly** - Every 90 days recommended
3. **Use HTTPS in production** - Encrypt all traffic
4. **Sanitize user input** - DOMPurify already implemented
5. **Monitor API usage** - Set up billing alerts
6. **Update dependencies** - Run `pip list --outdated` regularly

## Support

If you encounter issues not covered here:

1. Check browser console for errors (F12)
2. Check server logs in terminal
3. Verify all prerequisites are met
4. Review the main [README.md](README.md)
5. Open an issue on GitHub with:
   - Error message
   - Steps to reproduce
   - Browser/OS version
   - Server logs

## Next Steps

After successful setup:

1. Try a complete session to understand the flow
2. Review the Admin Panel to see analytics
3. Customize questions for your use case
4. Consider deployment options for production use
5. Set up monitoring and logging

---

**Happy debiasing!** Remember: the goal is awareness, not perfection.
