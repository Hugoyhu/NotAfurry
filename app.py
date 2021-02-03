import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

BOLT_PORT = 3000

try: 
    BOLT_PORT = int(os.environ.get('PORT'))
except KeyError:  
    print(f"Environment variable does not exist, using port ${port}") 

@app.message("furry")
@app.message("fuwwy")
@app.message("fuzzy")
@app.message("fluffy")
@app.message("fur")
@app.message("feathery")
@app.message("fwuwwy")
@app.message("fwurry")
@app.message("fwuzzy")
@app.message("fwur")
@app.message("fweathery")
@app.message("fwufry")
def say_hello(message, say):
    user = message['user']
    say(f"<@{user}> NO, U :nou:")

# Start your app
if __name__ == "__main__":
    app.start(port=BOLT_PORT)
