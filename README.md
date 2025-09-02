# Rogan-Style Birthday Message Generator

People want a fun, customized birthday message inspired by Joe Rogan, tied to a user-provided topic, but creating one that is engaging, on-topic, and policy-compliant takes time and skill. This agent generates short, shareable birthday messages in the playful style of Joe Rogan while clearly disclosing that the message is AI-generated and not written or endorsed by the public figure.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key
```

## Usage

```bash
python run.py "Your input message here"
```

## Development

This agent is built using the OpenAI Agents SDK and follows canonical patterns from the official documentation.

### Files
- `agent.py` - Main agent implementation
- `run.py` - Command-line interface
- `requirements.txt` - Dependencies
- `.env.example` - Environment configuration template
