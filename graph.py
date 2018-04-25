import requests
import numpy


def get_friends(user_id, fields):
	""" Returns a list of user IDs or detailed information about a user's friends """
	'''assert isinstance(user_id, int), "user_id must be positive integer"
	assert isinstance(fields, str), "fields must be string"
	assert user_id > 0, "user_id must be positive integer"'''
	domain = "https://api.vk.com/method"
	access_token = "17318950681ade2e37c1c26cb3972331a078329c9902bb009897cb90f7a03317acf743f857a138a224c62"
	user_id = "56200185"

	query_params = {
		'domain': domain,
		'access_token': access_token,
		'user_id': user_id,
		'fields': fields
	}

	query = "{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.53".format(**query_params)
	response = requests.get(query)
	return response.json()


def get_mutual_friends(user_id, fields, target_uid):
	""" Returns a list of user IDs or detailed information about a user's friends """
	'''assert isinstance(user_id, int), "user_id must be positive integer"
	assert isinstance(fields, str), "fields must be string"
	assert user_id > 0, "user_id must be positive integer"'''
	domain = "https://api.vk.com/method"
	access_token = "17318950681ade2e37c1c26cb3972331a078329c9902bb009897cb90f7a03317acf743f857a138a224c62"
	user_id = "56200185"

	query_params = {
		'domain': domain,
		'access_token': access_token,
		'user_id': user_id,
		'fields': fields,
		'target_uid': target_uid
	}

	query = "{domain}/friends.getMutual?access_token={access_token}&user_id={user_id}&fields={fields}&target_uid={target_uid}&v=5.53".format(**query_params)
	response = requests.get(query)
	return response.json()


def get_network(users_ids, as_edgelist=True):
	""" Building a friend graph for an arbitrary list of users """
	mutual_friends = []
	edge_list = []
	for i in range(0, users_ids['response']['count']):
		mf = get_mutual_friends(56200185, '', users_ids['response']['items'][i]['id'])
		try:
			mutual_friends.append((mf['response']))
		except:
			pass
	

	matrix = numpy.zeros((users_ids['response']['count'], users_ids['response']['count']))

	for i in range(0, len(mutual_friends)):
		mutual_friends[i] = return_position(users_ids['response']['items'], mutual_friends[i])
		print(mutual_friends[i])
		for j in range(0, len(mutual_friends[i])):
			item = mutual_friends[i][j]
			matrix[i][item] = 1

	if(as_edgelist):
		for i in range(0, len(matrix)):
			for j in range(0, len(matrix)):
				if(matrix[i][j] == 1):
					edge_list.append((i, j))
		return edge_list
	else:
		return matrix


def return_position(friends, mutual):
	for i in range(0, len(mutual)):
		for j in range(0, len(friends)):
			if(friends[j]['id'] == mutual[i]):
				mutual[i] = j
	return mutual


friends = get_friends(56200185, 'sex')
get_network(friends, as_edgelist=True)
