from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from slackclient import SlackClient

SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)
SLACK_OAUTH_TOKEN = getattr(settings, 'SLACK_OAUTH_TOKEN', None)
Client = SlackClient(SLACK_OAUTH_TOKEN)

SHOWS_CHANNEL_ID = "C5P1VJ97S"

class Events(APIView):
	def post(self, request, *args, **kwargs):
		slack_message = request.data
		
		if slack_message.get('token') != SLACK_VERIFICATION_TOKEN:
			return Response(status=status.HTTP_403_FORBIDDEN)

		if slack_message.get('type') == 'url_verification':
			return Response(data=slack_message, status=status.HTTP_200_OK)

		# greet bot
		if 'event' in slack_message:
			event_message = slack_message.get('event')

			# ignore bot's own message
			if event_message.get('subtype') == 'bot_message':
				return Response(status=status.HTTP_200_OK)

			# process user's message
			user = event_message.get('user')
			text = event_message.get('text').split(' ')[1]
			channel = event_message.get('channel')
			bot_text = 'Hi <@{}> :wave:'.format(user)
			if 'hi' in text.lower():
				self.hi(user, text, channel, bot_text)
			elif 'shows' in text.lower():
				self.shows(user, text, channel)

		return Response(status=status.HTTP_200_OK)

	def hi(self, user, text, channel, bot_text):
		Client.api_call(method='chat.postMessage', channel=channel, text=bot_text)
		return Response(status=status.HTTP_200_OK)

	def shows(self, user, text, channel):
		list_of_pinned_shows = Client.api_call(method="pins.list", channel=SHOWS_CHANNEL_ID)
		items = list_of_pinned_shows["items"]
		items_sorted = sorted(items, key=lambda item: item["message"]["text"])
		for x in range(0, len(items_sorted)):
			show = items_sorted[x]["message"]["text"]
			show += str(" - ")
			show += items_sorted[x]["message"]["permalink"] 
			Client.api_call("chat.postMessage", channel=channel, text=show, as_user=True)
		return Response(status=status.HTTP_200_OK)
