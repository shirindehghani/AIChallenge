from src.client import GameClient
from src.model import GameView


def get_thief_starting_node(view: GameView) -> int:
    # write your code here
    return 2


class Phone:
    def __init__(self, client: GameClient):
        self.client = client

    def send_message(self, message):
        self.client.send_message(message)


class AI:
    def __init__(self, phone: Phone):
        self.phone = phone

    def thief_move_ai(self, view: GameView) -> int:
        import random
        available_nodes = []
        for path in view.config.graph.paths:
            if path.price > view.balance:
                continue
            if view.viewer.node_id == path.first_node_id or view.viewer.node_id == path.second_node_id:
                node = path.first_node_id if path.second_node_id == view.viewer.node_id else path.second_node_id
                available_nodes.append(node)
        return random.choice(available_nodes)

        # write your code here
        message = ''
        for m in range(len(view.visible_agents)):
            message = message  + '0'
        self.phone.send_message(message)
        return 2

    def police_move_ai(self, view: GameView) -> int:
        import random
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
