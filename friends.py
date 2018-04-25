# https://oauth.vk.com/blank.html#access_token=237ac5e482ba5f879f6737b393a6acdf70dcbb6e4c14524a38524dfc4c19a4a0ab16631bce886e9faa3c7&expires_in=86400&user_id=144772087
import requests
import numpy


def get_friends(user_id, fields):
	""" Returns a list of user IDs or detailed information about a user's friends """
	'''assert isinstance(user_id, int), "user_id must be positive integer"
	assert isinstance(fields, str), "fields must be string"
	assert user_id > 0, "user_id must be positive integer"'''
	domain = "https://api.vk.com/method"
	access_token = "237ac5e482ba5f879f6737b393a6acdf70dcbb6e4c14524a38524dfc4c19a4a0ab16631bce886e9faa3c7"
	user_id = "144772087"

	query_params = {
		'domain': domain,
		'access_token': access_token,
		'user_id': user_id,
		'fields': fields
	}

	query = "{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.53".format(**query_params)
	response = requests.get(query)
	return response.json()

# x = get_friends(144772087,'bdate')
# print(x)

# def get(url, params={}, timeout=5, max_retries=5, backoff_factor=0.3):
# 	""" Выполнить GET-запрос

#     :param url: адрес, на который необходимо выполнить запрос
#     :param params: параметры запроса
#     :param timeout: максимальное время ожидания ответа от сервера
#     :param max_retries: максимальное число повторных запросов
#     :param backoff_factor: коэффициент экспоненциального нарастания задержки
#     """
# 	params[0]['url'] = url
# 	query = "{url}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.53".format(**params)
# 	delay = 100

# 	for x in range(0,max_retries):
# 		error = requests.get(query)
# 		if not error:
# 		# ok, got response
# 		break

# 		# error happened, pause between requests
# 		sleep(delay)

# 		# calculate next delay
# 		delay = min(delay * backoff_factor, timeout)
# 		delay = delay + norm_variate(delay * Jitter)


def age_predict(user_id):
	"""
	>>> age_predict(???)
	???
	"""
	assert isinstance(user_id, int), "user_id must be positive integer"
	assert user_id > 0, "user_id must be positive integer"
	friends = get_friends(user_id, 'bdate')
	ages = []
	for x in range(0, friends['response']['count']):
		try:
			date = (friends['response']['items'][x]['bdate'])
			ages.append(int(date.split('.', 3)[2]))
		except:
			pass
	return numpy.median(ages)
print(age_predict(144772087))
