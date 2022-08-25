from src.client import GameClient
from src.model import GameView

from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix
import random


def get_graph_distances(view: GameView):
    nodes = [node.id for node in view.config.graph.nodes]
    graph = [len(nodes)*[0] for i in range(len(nodes))]
    for path in view.config.graph.paths:
        graph[path.first_node_id-1][path.second_node_id-1] = 1
        graph[path.second_node_id-1][path.first_node_id-1] = 1
    graph = csr_matrix(graph)
    distances = shortest_path(graph, directed=False)
    return distances


def get_distance(i, j, distances):
    return distances[i-1, j-1]


def get_optimal_node_thief(view, available_nodes):
    d = get_graph_distances(view)
    weights = []
    for node in available_nodes:
        closest_police = 1000
        for agent in view.visible_agents:
            if not agent.is_dead and agent.team != view.viewer.team and agent.agent_type != view.viewer.agent_type:
                police_node = agent.node_id
                closest_police = min(closest_police, get_distance(node, police_node, distances=d))
        weights.append(closest_police * closest_police)

    return random.choices(available_nodes, weights=weights)[0]


def get_thief_starting_node(view: GameView) -> int:
    # write your code here
    available_nodes = []
    for i in range(2, len(view.config.graph.nodes)+1):
        available_nodes.append(i)
    return get_optimal_node_thief(view, available_nodes)


class Phone:
    def __init__(self, client: GameClient):
        self.client = client

    def send_message(self, message):
        self.client.send_message(message)


class AI:
    def __init__(self, phone: Phone):
        self.phone = phone

    def thief_move_ai(self, view: GameView) -> int:
        available_nodes = []
        for path in view.config.graph.paths:
            if path.price > view.balance:
                continue
            if view.viewer.node_id == path.first_node_id or view.viewer.node_id == path.second_node_id:
                node = path.first_node_id if path.second_node_id == view.viewer.node_id else path.second_node_id
                available_nodes.append(node)
        available_nodes.append(view.viewer.node_id)

        return get_optimal_node_thief(view, available_nodes)

        # write your code here
        message = ''
        for m in range(len(view.visible_agents)):
            message = message  + '0'
        self.phone.send_message(message)
        return 2

    def police_move_ai(self, view: GameView) -> int:
        available_nodes = []
        for path in view.config.graph.paths:
            if path.price > view.balance:
                continue
            if view.viewer.node_id == path.first_node_id or view.viewer.node_id == path.second_node_id:
                node = path.first_node_id if path.second_node_id == view.viewer.node_id else path.second_node_id
                available_nodes.append(node)
        return random.choice(available_nodes)

        # write your code here
        self.phone.send_message('00101001')
        return 1
