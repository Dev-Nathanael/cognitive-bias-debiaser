# Cognitive Bias Debiaser

An AI-powered thinking partner that helps you explore cognitive biases in your decision-making through structured conversations with Claude AI.

## Overview

The Cognitive Bias Debiaser is a web-based chatbot that guides you through a neutral, exploratory conversation about your decisions. Unlike traditional decision-making tools that prescribe solutions, this tool helps you become aware of thinking patterns that might be influencing your choices.

### Philosophy

- **Exploratory, not corrective** - Reveals thinking patterns without prescribing changes
- **Awareness-focused** - Success is measured by awareness gained, not behavior change
- **Neutral tone** - No judgment, purely curious and observational
- **Respects expertise** - Assumes you may have valid reasons for your approaches

## Features

### Core Functionality

- **Structured Decision Analysis** - 15-question context gathering phase
- **AI-Powered Bias Detection** - Analyzes 5 cognitive bias types using Claude Sonnet 4.5
- **Adaptive Questioning** - 50-question bank with intelligent question selection
- **Follow-up Detection** - AI automatically asks clarifying questions when needed
- **Synthesis Questions** - Connects insights across multiple responses
- **Progress Tracking** - Re-analyzes biases every 3 questions to track awareness evolution
- **Interactive Reporting** - Visual dashboard showing bias patterns and changes

### Cognitive Biases Analyzed

1. **Confirmation Bias** - Tendency to seek information that confirms existing beliefs
2. **Availability Bias** - Over-relying on easily recalled examples
3. **Overconfidence Bias** - Excessive certainty in judgments
4. **Anchoring Bias** - Over-reliance on initial information
5. **Loss Aversion** - Fear of losses outweighing potential gains

### Advanced Features

- **Session Persistence** - Auto-save and resume conversations (within 1 hour)
- **Learning System** - Tracks question effectiveness for future optimization
- **Cost Monitoring** - Real-time API token usage and cost tracking
- **Admin Panel** - Analytics dashboard for question performance and usage stats
- **Privacy-First** - All data stored locally in browser (IndexedDB)
- **Gibberish Detection** - Client-side validation to ensure genuine engagement

## Technology Stack

### Frontend
- React 18 (CDN-based, no build process)
- Tailwind CSS
- IndexedDB for persistent storage
- Marked.js for markdown rendering
- DOMPurify for XSS protection

### Backend
- Python 3 with Flask
- Flask-CORS for cross-origin requests
- Anthropic Claude API (Sonnet 4.5)

### Architecture
- Single-page application with minimal backend proxy
- Client-side state management
- Structured API integration with tool/function calling

## Quick Start

See [SETUP.md](SETUP.md) for detailed installation instructions.

```bash
# 1. Clone the repository
git clone <repository-url>
cd cognitive-bias-debiaser

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Set up environment variables
echo "ANTHROPIC_API_KEY=your-api-key-here" > .env

# 4. Run the server
python server.py

# 5. Open browser
# Navigate to http://localhost:3000
```

## Usage

### Starting a Session

1. Open the application in your browser
2. Answer 15 context questions about your decision
3. Review the initial bias analysis
4. Engage with adaptive debiasing questions
5. View your final report with bias evolution

### Question Types

The chatbot uses three types of questions:

- **Insight** - Reveal mental models and assumptions
- **Probing** - Dig deeper into specific patterns
- **Conversational** - Softer, more exploratory tone

### Understanding Your Results

The final report shows:

- **Before/After Comparison** - How bias scores changed during the conversation
- **Bias Evolution Timeline** - Checkpoints showing progress through the conversation
- **Pattern Observations** - AI-generated insights about your thinking patterns
- **Executive Summary** - Overall awareness metrics

Bias scores range from 0-1:
- **Green (0-0.4)** - Low risk
- **Yellow (0.4-0.6)** - Medium risk
- **Red (0.6-1.0)** - High risk

Note: High scores are observations, not failures. The goal is awareness, not necessarily changing your decision.

## Admin Panel

Access the admin panel via the UI to view:

- Question effectiveness statistics
- API cost tracking (input/output tokens)
- Session history and analytics
- Data export for machine learning training

## Project Structure

```
cognitive-bias-debiaser/
├── index.html          # Complete React SPA (2,654 lines)
├── server.py           # Flask proxy server (90 lines)
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not in repo)
├── .gitignore         # Git ignore rules
├── README.md          # This file
└── SETUP.md           # Detailed setup guide
```

## Configuration

### Debiasing Configuration

The chatbot behavior is configured via `DEBIASING_CONFIG` in `index.html`:

```javascript
{
    approach: "exploratory",        // not "corrective"
    success_metric: "awareness",    // not "behavior_change"
    tone: "curious_neutral",        // not "analytical_critical"
    respect_expertise: true,
    allow_maintained_positions: true
}
```

### API Configuration

- **Model**: claude-sonnet-4-5-20250929

## Privacy & Data

- **Local storage only** - All data stored in browser IndexedDB
- **Metadata only** - Question effectiveness metrics, not actual answers
- **No server-side storage** - Server only proxies API requests
- **User control** - Clear all data via admin panel

## Browser Compatibility

Requires a modern browser with:
- ES6+ JavaScript support
- IndexedDB support
- LocalStorage (fallback)

## API Costs

Typical session costs (approximate):
- Context phase: 500-1000 input tokens
- Analysis phase: 1500-2500 tokens per checkpoint
- Debiasing phase: 300-800 tokens per question
- Total session: ~$0.10-0.30 depending on conversation depth

## Troubleshooting

### "Analysis Failed" Error
- Check your Anthropic API key in `.env`
- Verify internet connection
- Check API rate limits

### Session Not Resuming
- Sessions expire after 1 hour
- LocalStorage must be enabled
- Clear browser cache if issues persist

### Questions Not Personalizing
- Requires context from Phase 1
- Check network tab for API errors
- Verify API key has sufficient credits

## Contributing

Contributions are welcome! Areas for improvement:

- Additional bias types
- Enhanced question bank
- Improved visualization components
- Multi-language support
- Mobile optimization

## Acknowledgments

- Built with [Anthropic Claude API](https://www.anthropic.com/)
- Inspired by research in cognitive psychology and behavioral economics

## Support

For issues or questions:
- Check [SETUP.md](SETUP.md) for installation help
- Review troubleshooting section above
- Open an issue on GitHub

---

**Remember:** The goal is awareness, not perfection. Maintaining a decision with full awareness of your thinking patterns is sophisticated decision-making.
