from rasa_core.channels.facebook import FacebookInput
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig
from rasa_core.agent import Agent


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/trendernlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = FacebookInput(
fb_verify="123",
# you need tell facebook this token, to confirm your URL
fb_secret="23f506c39633107ed4a15abffd69ea99",  # your app secret
fb_access_token="EAAFoEGlxs6cBALqQYkCFadXZCqzSXdhBpZBur0mPFtFZAyrcZCP80WwXQhYzibTmSXVROyophhOJ30N1E2neK5ZCyUliMonBhQiYDdJTeDCjalTbCZBGF93TIgexJjfgg4FtfQaqL8avOeRZBCsnNO6rZCDF5YsjJExvZANbGaKufiwZDZD"  # token for the page you subscribed to
)

agent.handle_channels([input_channel], 5004, serve_forever=True)
