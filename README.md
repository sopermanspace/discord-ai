# discord-ai

A Discord bot that integrates with the Cohere LLM API. The bot can respond to specific commands and mentions in a Discord server.

## Features

- Responds to the `!talk` command by generating a response using the Cohere API.
- Responds when mentioned directly in a message.
- Includes a simple test command `!hello` to verify the bot's functionality.

## Requirements

- Python 3.9+
- `discord.py` library
- `cohere` library
- `nest_asyncio` library

## Setup
 
1. **Clone the Repository**

   ```bash
   git clone https://github.com/himanshuskyrockets/discord-ai.git
   cd discord-bot-cohere
   ```

2. **Install Dependencies** 

   Create a virtual environment (optional but recommended) and install the required packages:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install discord.py cohere nest_asyncio
   ```

3. **Configuration**

   Replace the placeholders in the code with your actual API keys:
   - `your-cohere-api-key` in the `cohere.Client` initialization.
   - `your-discord-bot-token` in the `client.run` function.

4. **Run the Bot**

   Execute the script to start the bot:

   ```bash
   python bot.py
   ```

## Code Overview

- **`bot.py`**: Main script to run the bot.
  - `@client.event on_ready()`: Logs a message when the bot is ready.
  - `@client.command talk(ctx, *, message)`: Command to send a message to the Cohere API and get a response.
  - `@client.command hello(ctx)`: Simple command for testing.
  - `@client.event on_message(message)`: Handles direct mentions of the bot and responds using the `talk` command.

## Usage

- Mention the bot in a Discord channel: `@YourBot Hello, how are you?`
- Use the command `!talk <message>` to get a response from Cohere.
- Test the bot with the `!hello` command to confirm it’s working.


## What More You Can Add:
1. **Pass name to LLM**:
**Feature**: Instead of concating the username in message pass the user name to the LLM.

2. **Emoji Reactions Based on User Message**:

**Feature**: Add functionality to react with emojis based on the sentiment or content classification of the user’s message that aligns with reaction.

3. **Custom Command Handling**:

**Feature**: Allow users to define custom commands and responses in the Discord server.

## Acknowledgments

- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Cohere API Documentation](https://cohere.ai/docs/)

## License

This project is licensed under the MIT License.

---

Feel free to adjust the placeholders (`your-cohere-api-key`, `your-discord-bot-token`, etc.) and add any additional details relevant to your project.
