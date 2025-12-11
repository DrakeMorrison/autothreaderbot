# Discord AutoThreader Bot

Creates a thread every 10 messages unless reset by an anchor user.

## Setup

1. Clone this repository
2. Install dependencies:
```
   pip install -r requirements.txt
```

3. Create a Discord bot:
   - Go to https://discord.com/developers/applications
   - Click "New Application"
   - Go to "Bot" tab and click "Add Bot"
   - Enable "Message Content Intent" under Privileged Gateway Intents
   - Copy your bot token

4. Configure the bot:
   - Copy `.env.example` to `.env`
   - Replace `your_bot_token_here` with your actual bot token

5. Invite the bot to your server:
   - Go to OAuth2 → URL Generator
   - Select scopes: `bot`
   - Select permissions: `Send Messages`, `Create Public Threads`, `Read Message History`
   - Copy and visit the generated URL

6. Run the bot:
```
   python autothreadbot.py
```

## Commands

- `!enable` - Enable bot in current channel (requires Manage Channels)
- `!disable` - Disable bot in current channel (requires Manage Channels)
- `!setanchor @user` - Set anchor user (requires Manage Channels)
- `!removeanchor` - Remove anchor user (requires Manage Channels)
- `!checkanchor` - Check current anchor user
