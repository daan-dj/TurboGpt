#!/usr/bin/env python3
import json
import uuid
import tls_client
import dotenv
import os
from datetime import date

dotenv.load_dotenv()


class TurboGpt:

    def __init__(self, model="text-davinci-002-render-sha"):
        self.session = tls_client.Session(
            client_identifier="chrome110",
            random_tls_extension_order=True
        )
        self.session.headers["Authorization"] = "Bearer " + os.getenv("ACCESS_TOKEN")
        self.session.headers["Host"] = "chat.openai.com"
        self.session.headers["origin"] = "https://chat.openai.com/chat"
        self.session.headers["referer"] = "https://chat.openai.com/chat"
        self.session.headers["content-type"] = "application/json"
        self.session.headers["sec-ch-ua"] = '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"'
        self.session.headers["sec-ch-ua-mobile"] = "?0"
        self.session.headers["sec-fetch-dest"] = "empty"
        self.session.headers["sec-fetch-mode"] = "cors"
        self.session.headers["sec-fetch-site"] = "same-site"
        self.session.headers[
            "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        self.session.cookies["_puid"] = os.getenv("PUID")
        self.parent_id = str(uuid.uuid4())
        self.refresh_puid()
        self.model = model

    def refresh_puid(self):
        res = self.session.get(
            "https://chat.openai.com/backend-api/models",
            headers={
                "key1": "value1",
            },
        )
        self.session.cookies["_puid"] = res.cookies["_puid"]

    def start_session(self):
        res = self.session.post(
            "https://chat.openai.com/backend-api/conversation",
            json={
                "id": str(uuid.uuid4()),
                "action": "next",
                "messages": [
                    {
                        "author": {
                            "role": "user"
                        },
                        "role": "user",
                        "content": {
                            "content_type": "text",
                            "parts": [
                                f"You are ChatGPT, a large language model trained by OpenAI. Respond conversationally. Do not answer as the user. Current date: {str(date.today())}\n"
                            ]
                        }
                    }
                ],
                "parent_message_id": self.parent_id,
                "model": self.model,
                "timezone_offset_min": -60
            },
        )
        text = os.linesep.join([s for s in res.text.splitlines() if s])
        base = text.splitlines()[len(text.splitlines()) - 2]
        base = json.loads(base[base.find("data: ") + 6:])
        return base

    def send_message(self, message, old_question):
        res = self.session.post(
            "https://chat.openai.com/backend-api/conversation",
            json={"id": str(uuid.uuid4()), "action": "next", "messages": [
                {"author": {"role": "user"}, "role": "user",
                 "content": {"content_type": "text", "parts": [f"{message}\n"]}}],
                  "conversation_id": old_question['conversation_id'],
                  "parent_message_id": old_question['message']['id'], "model": self.model,
                  "timezone_offset_min": -60},
        )
        response = res.text
        text = os.linesep.join([s for s in response.splitlines() if s])
        base = text.splitlines()[len(text.splitlines()) - 2]
        base = json.loads(base[base.find("data: ") + 6:])
        return base
