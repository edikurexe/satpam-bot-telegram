# satpam-bot-telegram

Telegram moderation bot focused on enforcing username rules in group chats.

## What this bot does
- Monitors members who do not have a Telegram username
- Sends warnings to non-compliant members
- Escalates warnings up to a defined limit
- Removes members who still do not follow the group rule
- Provides basic `/start` and `/help` commands

## Main use case
This bot is useful for Telegram groups that require members to have a public username for moderation, identification, or admin workflow reasons.

## Tech stack
- Python 3
- python-telegram-bot
- python-dotenv
- Docker / Docker Compose

## Local setup
```bash
git clone https://github.com/edikurexe/satpam-bot-telegram.git
cd satpam-bot-telegram
pip install -r requirements.txt
cp token.env.example token.env 2>/dev/null || printf 'TOKEN=your_bot_token_here
' > token.env
python bot.py
```

## Docker setup
```bash
docker-compose up --build -d
```

## Configuration
Create a `token.env` file in the project root:
```env
TOKEN=your_bot_token_here
```

## Repository structure
- `bot.py` — main bot logic
- `requirements.txt` — Python dependencies
- `Dockerfile` — container build definition
- `token.env` — local environment file template/value placeholder

## Notes
This repository represents a practical moderation utility built for real Telegram group operations.
