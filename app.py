import re
import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Listens to incoming messages that contain "hello"
@app.message("furry")
@app.message("fuwwy")
@app.message("fuzzy")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"NO I'M NOT! YOU ARE!")

@app.message(re.compile("/.*a.*d.*r.*i.*a.*n.*f.*u.*[r|w].*[r|w].*y.*/gmi"))
def say_hello_regex(say, context):
    # regular expression matches are inside of context.matches
    greeting = context['matches'][0]
    say(f"UwU yes a vewwy vewwy bad fuwwy")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
