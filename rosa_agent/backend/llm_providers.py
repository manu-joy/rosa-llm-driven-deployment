from abc import ABC, abstractmethod
from typing import List, Dict, Optional
import os
import openai
import anthropic
import requests


class LLMProvider(ABC):
    """Abstract base class for LLM providers"""
    
    @abstractmethod
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Generate a response from the LLM"""
        pass
    
    @abstractmethod
    def validate_config(self) -> bool:
        """Validate provider configuration"""
        pass


class OpenAIProvider(LLMProvider):
    """OpenAI GPT provider (using legacy v0.28 API)"""
    
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key
    
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=kwargs.get('temperature', 0.7),
                max_tokens=kwargs.get('max_tokens', 2000)
            )
            return response.choices[0].message['content']
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
    
    def validate_config(self) -> bool:
        try:
            # Test with a simple completion
            openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": "test"}],
                max_tokens=5
            )
            return True
        except Exception:
            return False



class GroqProvider(LLMProvider):
    """Groq fast inference provider (using OpenAI v0.28 compatible API)"""
    
    def __init__(self, api_key: str, model: str = "llama-3.1-8b-instant"):
        self.api_key = api_key
        self.model = model
        # Groq endpoint for v0.28 style API
        self.base_url = "https://api.groq.com/openai/v1"
    
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        try:
            # Use requests library since the old openai library doesn't support custom endpoints well
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": self.model,
                "messages": messages,
                "temperature": kwargs.get('temperature', 0.7),
                "max_tokens": kwargs.get('max_tokens', 2000)
            }
            # Retry logic for rate limits
            max_retries = 3
            base_delay = 2
            
            for attempt in range(max_retries + 1):
                try:
                    response = requests.post(
                        f"{self.base_url}/chat/completions",
                        json=payload,
                        headers=headers,
                        timeout=60
                    )
                    response.raise_for_status()
                    return response.json()['choices'][0]['message']['content']
                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 429:
                        if attempt < max_retries:
                            import time
                            sleep_time = base_delay * (2 ** attempt)
                            print(f"Groq rate limit hit, retrying in {sleep_time}s...")
                            time.sleep(sleep_time)
                            continue
                    raise e
        except Exception as e:
            raise Exception(f"Groq API error: {str(e)}")
    
    def validate_config(self) -> bool:
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": self.model,
                "messages": [{"role": "user", "content": "test"}],
                "max_tokens": 5
            }
            response = requests.post(
                f"{self.base_url}/chat/completions",
                json=payload,
                headers=headers,
                timeout=10
            )
            return response.status_code == 200
        except Exception:
            return False


class AnthropicProvider(LLMProvider):
    """Anthropic Claude provider"""
    
    def __init__(self, api_key: str, model: str = "claude-3-sonnet-20240229"):
        self.api_key = api_key
        self.model = model
        self.client = anthropic.Anthropic(api_key=api_key)
    
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        try:
            # Extract system message if present
            system_message = ""
            user_messages = []
            
            for msg in messages:
                if msg["role"] == "system":
                    system_message = msg["content"]
                else:
                    user_messages.append(msg)
            
            response = self.client.messages.create(
                model=self.model,
                max_tokens=kwargs.get('max_tokens', 2000),
                system=system_message,
                messages=user_messages,
                temperature=kwargs.get('temperature', 0.7)
            )
            return response.content[0].text
        except Exception as e:
            raise Exception(f"Anthropic API error: {str(e)}")
    
    def validate_config(self) -> bool:
        try:
            # Test with a simple completion
            self.client.messages.create(
                model=self.model,
                max_tokens=5,
                messages=[{"role": "user", "content": "test"}]
            )
            return True
        except Exception:
            return False


class LocalProvider(LLMProvider):
    """Local LLM provider (Ollama, vLLM, etc.)"""
    
    def __init__(self, endpoint_url: str, api_key: str = None, model: str = "llama2"):
        self.endpoint_url = endpoint_url
        self.api_key = api_key
        self.model = model
    
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        try:
            headers = {"Content-Type": "application/json"}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"

            # OpenAI-compatible API format
            response = requests.post(
                f"{self.endpoint_url}/v1/chat/completions",
                headers=headers,
                json={
                    "model": self.model,
                    "messages": messages,
                    "temperature": kwargs.get('temperature', 0.7),
                    "max_tokens": kwargs.get('max_tokens', 2000)
                },
                timeout=60
            )
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            raise Exception(f"Local LLM API error: {str(e)}")
    
    def validate_config(self) -> bool:
        try:
            headers = {}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"
            
            # Test endpoint availability
            response = requests.get(f"{self.endpoint_url}/v1/models", headers=headers, timeout=5)
            return response.status_code == 200
        except Exception:
            return False


class LLMProviderFactory:
    """Factory for creating LLM providers"""
    
    @staticmethod
    def create_provider(provider_type: str, config: Dict) -> LLMProvider:
        """Create an LLM provider based on type and configuration"""
        
        if provider_type.lower() == "openai":
            return OpenAIProvider(
                api_key=config.get('api_key'),
                model=config.get('model', 'gpt-4')
            )
        
        elif provider_type.lower() == "groq":
            return GroqProvider(
                api_key=config.get('api_key'),
                model=config.get('model', 'llama-3.1-8b-instant')
            )
        
        elif provider_type.lower() == "anthropic":
            return AnthropicProvider(
                api_key=config.get('api_key'),
                model=config.get('model', 'claude-3-sonnet-20240229')
            )
        
        elif provider_type.lower() == "local":
            return LocalProvider(
                endpoint_url=config.get('endpoint_url'),
                api_key=config.get('api_key'),
                model=config.get('model', 'llama2')
            )
        
        else:
            raise ValueError(f"Unknown provider type: {provider_type}")
