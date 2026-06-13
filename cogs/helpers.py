from google import genai
import discord
from discord.ext import commands
import os
import asyncio
from cogs.hyperparams import *

class LLMHelper():
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GOOGLE_LLM_API"))

    async def _ask(self, final_prompt, model="gemma-4-31b-it", max_output_tokens=1500):
        response = await self.client.aio.models.generate_content(
            model=model,
            contents=final_prompt,
            config=genai.types.GenerateContentConfig(
                max_output_tokens=max_output_tokens,
            )
        )
        print(response)
        # instead of response.text
        parts = response.candidates[0].content.parts
        actual_text = parts[-1].text
        print(actual_text)
        return actual_text
    
    async def askllm(self, user_raw_prompt, attempts=5, wait_time = 2):
        final_prompt = system_prompt + user_raw_prompt
        for attempt in range(attempts):
            try:
                response = await self._ask(final_prompt=final_prompt)
                if not response:
                    raise RuntimeError("Got an empty message")
                return response
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                await asyncio.sleep(wait_time)
        return customError("LLMfailure")

def customError(permission, arguments = None) -> discord.Embed:
    categories = {
        "missingUserPerm": ["Missing User Permission","The user doesn't have the permission(s) to use this command"],
        "LLMfailure": ["Low IQ LLM", "The bot's LLM is stupid and basically died :/"]
    }
    # permission = ["which_category","arguments"]
    category = categories[permission]
    embed = discord.Embed(
        title=category[0],
        description=category[1],
        color=discord.Color.red()
    )
    return embed

