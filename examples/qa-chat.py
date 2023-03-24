from turbogpt import TurboGpt

if __name__ == '__main__':
    turbogpt = TurboGpt()  # or "text-davinci-002-render-sha" (default)
    session = turbogpt.start_session()
    while True:
        q = turbogpt.send_message(input(">>> "), session)
        print(q['message']['content']['parts'][0])
        session = q
