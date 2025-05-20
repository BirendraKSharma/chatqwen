# ChatQwen

ChatQwen is a simple Streamlit web application that allows users to interact with the Qwen2.5 language model (via Ollama) in a conversational chat interface.

## Features

- Chat with the Qwen2.5 LLM using a clean web UI.
- Keeps track of conversation history.
- Powered by [Streamlit](https://streamlit.io/) and [Ollama LLM](https://ollama.com/).
- Fast response generation with error handling.

## Getting Started

### Prerequisites

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [langchain_ollama](https://python.langchain.com/docs/integrations/llms/ollama)
- Ollama server running with the `qwen2.5-coder` model available

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BirendraKSharma/chatqwen.git
   cd chatqwen
   ```

2. Install dependencies:

   ```bash
   pip install streamlit langchain_ollama
   ```

3. Ensure Ollama is running with the `qwen2.5-coder` model. You can pull the model using:

   ```bash
   ollama pull qwen2.5-coder
   ```

### Running the App

```bash
streamlit run main.py
```

Open your browser to the provided local URL (typically http://localhost:8501).

## Usage

- Type your question or prompt in the chat input.
- The model will respond, and the conversation history will be displayed in the UI.

## Project Structure

```
main.py       # Streamlit app code
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/)
- [LangChain](https://www.langchain.com/)