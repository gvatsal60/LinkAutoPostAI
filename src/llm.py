"""
Module for interacting with large language models (LLMs).
"""

from litellm import completion


class LLM:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.llm = litellm.from_pretrained(model_name)

    def generate_text(self, prompt: str) -> str:
        response = completion.create(
            model=self.model_name, messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
