# TurboGpt

#### A python based wrapper for GPT-4 & GPT-3.5 PLUS. 

## Benefits and why.
There is currently no way to use GPT-4 outside the online chat.openai.com interface. This wrapper allows you to use GPT-4 in your own projects. \
the current API is extremely slow and even if you have premium it does not speed up the response time. TurboGpt does not use the API and instead uses the same interfaces as the chat.openai.com website.
This means that you can use GPT-4 and GPT-3.5 PLUS in your own projects without having to wait 20+ seconds for a response.

## Install

To use GPT-4 you need to have a GPT PLUS subscription. If you don't, you can get one [here](https://beta.openai.com/pricing).

```bash
pip install turbogpt
```

### Getting the PUID & ACCESS_TOKEN
```
1. Head over to https://chat.openai.com/chat
2. Open the developer console (F12)
3. Go to the application tab
4. Go to local cookies
5. Copy the value of the _puid cookie
6. Copy the value of the __Secure-next-auth.session-token cookie
7. Paste the values into the .env file like so:

ACCESS_TOKEN=__Secure-next-auth.session-token cookie
PUID=_puid
```

## Usage

```python
from turbogpt import TurboGpt

turbogpt = TurboGpt(model="gpt-4")  # or "text-davinci-002-render-sha" (default)(AKA GPT-3.5)
session = turbogpt.start_session()
q = turbogpt.send_message(input(">>> "), session)
print(q['message']['content']['parts'][0])
```
![image](https://i.imgur.com/lyNqjJp.png)


## Info
```text
✅ - cloudflare bypassed
✅ - automatic refresh of _puid
✅ - GPT-4 Support
✅ - GPT-3.5 PLUS Support
✅ - GPT-3.5 Support (Free)
✅ - Fast
✅ - Easy to use
✅ - No API
✅ - No rate limits
✅ - No waiting
✅ - Back and forth conversation support
```

## TurboGpt-CLI
Check out a TurboGpt based CLI [here](https://github.com/daan-dj/TurboGpt-cli)
