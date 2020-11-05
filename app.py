import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.message("furry")
@app.message("fuwwy")
@app.message("fuzzy")
@app.message("fluffy")
@app.message("fur")
@app.message("feathery")
def say_hello(message, say):
    user = message['user']
    say(f"<@{user}> NO U :nou:")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 5000)))
