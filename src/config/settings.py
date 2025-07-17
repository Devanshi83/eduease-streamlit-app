import os
import streamlit as st
from dataclasses import dataclass

@dataclass
class Settings:
    """Manages application settings and API keys loaded from environment variables."""

    # API Keys
    GOOGLE_API_KEY: str = None

    # AI/Audio Model Config
    WHISPER_MODEL: str = "base"
    GEMINI_MODEL: str = "gemini-1.5-flash-latest"

    def __post_init__(self):
        """Loads API keys after the object is created."""
        self._load_api_keys()

    def _load_api_keys(self):
        """
        Loads the Google API key from environment variables.
        Raises an exception if the key is not found.
        """
        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        if not self.GOOGLE_API_KEY:
            st.error("Google AI API key not found. Please set `GOOGLE_API_KEY` as an environment variable.", icon="🚨")
            raise Exception("API Key configuration error.")
