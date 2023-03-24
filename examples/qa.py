from turbogpt import TurboGpt

turbogpt = TurboGpt(model="gpt-4")  # or "text-davinci-002-render-sha" (default)
session = turbogpt.start_session()
q = turbogpt.send_message(input(">>> "), session)
print(q['message']['content']['parts'][0])
