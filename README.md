# Two LLMs Actually Talking to Each Other!

An AI-powered research assistant that showcases interaction between two Gemini models, demonstrating conversational AI capabilities in academic analysis.

## Features

- **Dual-model chat system** using Gemini 2.0 Flash Lite  
- **Automated paper search** functionality  
- **Context-aware conversation** between two LLMs  
- **Intelligent information extraction** from research papers  
- **Auto-timeout system** to manage conversation flow  
- **Detailed chat logging** for analysis  

## Project Structure

```plaintext
├── main.py              # Entry point for initiating AI conversation
├── system_prompt.py     # AI assistant behavior and configurations
├── tools.py             # Utilities for searching and extracting paper data
├── chat_log.txt         # Logs conversation history for analysis
├── papers/              # Directory of research papers
│   ├── aiandclimatechange/
│   └── machinelearninginmedicine/
├── .env                 # Environment configuration file
└── .gitignore           # Configuration for ignoring unnecessary files
```

## Setup

1. **Clone the repository**  
2. **Install dependencies:**  
   ```bash
   pip install google-generativeai python-dotenv
   ```
3. **Configure environment variables:**  
   Create a `.env` file in the root directory with your Gemini API key:  
   ```plaintext
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the program:  
```bash
python main.py
```

The assistant will:  
- Initiate conversation between two LLMs  
- Retrieve relevant academic papers  
- Extract key insights from research  
- Log discussions in `chat_log.txt`  

## Environment Variables  

- `.env`: Stores API keys and other sensitive configurations  
- `GEMINI_API_KEY`: Required for accessing the Gemini model  

## Notes

- **This project demonstrates AI-driven conversation** between two Gemini models, showcasing how LLMs interact meaningfully.  
- **Sessions terminate automatically after 3 minutes** to optimize resources.  
- **Conversations are saved in chat_log.txt** for review and study.  


