import requests
import random
import time
from datetime import datetime
import plotly
import plotly.graph_objs as go
import plotly.plotly as py
import numpy
# import igraph
# from igraph import Graph, plot
from collections import Counter


config = {
    'access_token': 'd5ef4719e789c8f72f79e71f467246e3aeebe0b40b579be851ae9a5965c3db51ed52d9f317c8b728ed919',
    'plotly_username': 'YanaEvshina',
    'plotly_api_key': 'S0JPRMKf6hwSLec6QLtY',
    'domain': 'https://api.vk.com/method',
    'user_id': "144772087",
    'fields': 0,
    'count': 0,
    'offset': 0,
    'target_uid': 0

}

def get(url, params={}, timeout=5, max_retries=60, backoff_factor=0.3):
    delay = 0
    for i in range(max_retries):
        try:
            response = requests.get(url, params)
            return response.json()
        except:
            pass
        time.sleep(delay)
        delay = min(delay * backoff_factor, timeout)
        delay += random.random()
    raise ConnectionResetError("Error")


def get_friends(user_id, fields):

    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"

    params = {
        'domain': config['domain'],
        'access_token': config['access_token'],
        'user_id': user_id,
        'fields': fields,
    }

    query = "{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.53".format(**params)
    response = get(query)
    return response.json()


def age_predict(user_id):

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


def messages_get_history(user_id, offset=0, count=900):
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    assert isinstance(offset, int), "offset must be positive integer"
    assert offset >= 0, "user_id must be positive integer"
    assert count >= 0, "user_id must be positive integer"
    max_count = 200
    params = {
        'domain': config['domain'],
        'access_token': config['access_token'],
        'user_id': user_id,
        'offset': offset,
        'count': min(count, max_count),
        'v': '5.53'
    }
    messages = []
 
    while count > 0:
        query = "{}/messages.getHistory".format(config['domain'])
        response = get(query, params=params)
        count -= min(count, max_count)
        params['offset'] += 200
        params['count'] = min(count, max_count)
        messages += response['response']
        time.sleep(0.333333334)
 
    return messages


def count_dates_from_messages(messages):
    def parse(d):
        return datetime.fromtimestamp(d).strftime("%Y-%m-%d")
 
    msg_list = [parse(c.get('date')) for c in messages]
    counted = Counter(msg_list)
 
    x = []
    y = []
    for key in counted:
        x.append(key)
        y.append(counted[key])
 
    return x, y

def plotly_messages_freq(freq_list):

    x, y = (freq_list)
    plotly.tools.set_credentials_file(username=config['plotly_username'], api_key=config['plotly_api_key'])
    data = [go.Scatter(x=x, y=y)]
    py.plot(data)
messages = messages_get_history(56200185)
frequency = count_dates_from_messages(messages)
plotly_messages_freq(frequency)


def get_network(users_ids, as_edgelist=True):
    mutual_friends = []
    edge_list = []
    for i in range(0, users_ids['response']['count']):
        mf = get_mutual_friends(144772087, '', users_ids['response']['items'][i]['id'])
        try:
            mutual_friends.append((mf['response']))
        except:
            pass
    
    matrix = numpy.zeros((users_ids['response']['count'], users_ids['response']['count']))

    for i in range(0, len(mutual_friends)):
        mutual_friends[i] = return_position(users_ids['response']['items'], mutual_friends[i])
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


def get_mutual_friends(user_id, fields, target_uid):
    """ Returns a list of user IDs or detailed information about a user's friends """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"

    params = {
        'domain': config['domain'],
        'access_token': config['access_token'],
        'user_id': user_id,
        'fields': fields,
        'target_uid': target_uid
    }

    query = "{domain}/friends.getMutual?access_token={access_token}&user_id={user_id}&fields={fields}&target_uid={target_uid}&v=5.53".format(**params)
    response = get(query)
    return response.json()


def return_position(friends, mutual):
    for i in range(0, len(mutual)):
        for j in range(0, len(friends)):
            if(friends[j]['id'] == mutual[i]):
                mutual[i] = j
    return mutual


# def plot_graph(vertices, edges):
#     g = Graph(vertex_attrs={"label": vert},
#               edges=e, directed=False)
#     N = len(vert)
#     visual_style = {}
#     visual_style["layout"] = g.layout_fruchterman_reingold(
#         maxiter=1000,
#         area=N ** 3,
#         repulserad=N ** 3)

#     g.simplify(multiple=True, loops=True)
#     communities = g.community_edge_betweenness(directed=False)
#     clusters = communities.as_clustering()
#     pal = igraph.drawing.colors.ClusterColoringPalette(len(clusters))
#     g.vs['color'] = pal.get_many(clusters.membership)

#     plot(g, **visual_style)

# friends = get_friends(56200185, 'sex')
# vert = [i for i in range(friends['response']['count'])]
# e = get_network(friends, as_edgelist=True)
# plot_graph(vert, e)