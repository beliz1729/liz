import requests
from datetime import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go


def messages_get_history(user_id, offset=0, count=20):
	assert isinstance(user_id, int), "user_id must be positive integer"
	assert user_id > 0, "user_id must be positive integer"
	assert isinstance(offset, int), "offset must be positive integer"
	assert offset >= 0, "user_id must be positive integer"
	assert count >= 0, "user_id must be positive integer"

	domain = "https://api.vk.com/method"
	access_token = "17318950681ade2e37c1c26cb3972331a078329c9902bb009897cb90f7a03317acf743f857a138a224c62"

	query_params = {
		'domain': domain,
		'access_token': access_token,
		'user_id': user_id,
		'count': count,
		'offset': offset
	}

	query = "{domain}/messages.getHistory?access_token={access_token}&user_id={user_id}&count={count}&offset={offset}&v=5.53".format(**query_params)
	response = requests.get(query)
	return response.json()


def count_dates_from_messages(messages):
	dates = []; counter = 1; frequency = []
	for i in range(0, len(messages['response']['items'])):
		date = datetime.fromtimestamp(messages['response']['items'][i]['date']).strftime("%Y-%m-%d")
		dates.append(date)
	for x in range(1, len(messages['response']['items'])):
		if (dates[x] == dates[x-1]):
			counter += 1
		else:
			frequency.append(counter)
			counter = 0
	return list(set(dates)), frequency
message = messages_get_history(56200185)
x, y = count_dates_from_messages(message)
plotly.tools.set_credentials_file(username='YanaEvshina', api_key='S0JPRMKf6hwSLec6QLtY')
data = [go.Scatter(x=x, y=y)]
py.iplot(data)
