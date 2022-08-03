import enum
from src import hide_and_seek_pb2


class GameStatus(enum.Enum):
    PENDING = hide_and_seek_pb2.GameStatus.PENDING
    ONGOING = hide_and_seek_pb2.GameStatus.ONGOING
    FINISHED = hide_and_seek_pb2.GameStatus.FINISHED

    def to_proto(self):
        return self.value

    @staticmethod
    def to_model(status):
        if status == hide_and_seek_pb2.GameStatus.PENDING:
            return GameStatus.PENDING
        elif status == hide_and_seek_pb2.GameStatus.ONGOING:
            return GameStatus.ONGOING
        else:
            return GameStatus.FINISHED


class GameResult(enum.Enum):
    UNKNOWN = hide_and_seek_pb2.GameResult.UNKNOWN
    FIRST_WINS = hide_and_seek_pb2.GameResult.FIRST_WINS
    SECOND_WINS = hide_and_seek_pb2.GameResult.SECOND_WINS
    TIE = hide_and_seek_pb2.GameResult.TIE

    def to_proto(self):
        return self.value

    @staticmethod
    def to_model(result):
        if result == hide_and_seek_pb2.GameResult.UNKNOWN:
            return GameResult.UNKNOWN
        elif result == hide_and_seek_pb2.GameResult.FIRST_WINS:
            return GameResult.FIRST_WINS
        elif result == hide_and_seek_pb2.GameResult.SECOND_WINS:
            return GameResult.SECOND_WINS
        else:
            return GameResult.TIE


class TurnType(enum.Enum):
    THIEF_TURN = hide_and_seek_pb2.TurnType.THIEF_TURN
    POLICE_TURN = hide_and_seek_pb2.TurnType.POLICE_TURN

    def to_proto(self):
        return self.value

    @staticmethod
    def to_model(turn_type):
        if turn_type == hide_and_seek_pb2.TurnType.THIEF_TURN:
            return TurnType.THIEF_TURN
        else:
            return TurnType.POLICE_TURN


class Turn:
    def __init__(self, turn_number: int, turn_type: TurnType):
        self.turn_number = turn_number
        self.turn_type = turn_type

    def to_proto(self):
        return hide_and_seek_pb2.Turn(turnNumber=self.turn_number, turnType=self.turn_type.to_proto())

    @staticmethod
    def to_model(turn: hide_and_seek_pb2.Turn):
        return Turn(turn_number=turn.turnNumber, turn_type=turn.turnType)


class Node:
    def __init__(self, id: int):
        self.id = id

    def to_proto(self):
        return hide_and_seek_pb2.Node(id=self.id)

    @staticmethod
    def to_model(node: hide_and_seek_pb2.Node):
        return Node(id=node.id)


class Path:
    def __init__(self, id: int, first_node_id: Node, second_node_id: Node, price: float):
        self.id = id
        self.first_node_id = first_node_id
        self.second_node_id = second_node_id
        self.price = price

    def to_proto(self):
        return hide_and_seek_pb2.Path(id=self.id,
                                      first_node_id=self.first_node_id,
                                      second_node_id=self.second_node_id,
                                      price=self.price)

    @staticmethod
    def to_model(path: hide_and_seek_pb2.Path):
        return Path(id=path.id,
                    first_node_id=path.first_node_id,
                    second_node_id=path.second_node_id,
                    price=path.price)


class Graph:
    def __init__(self, paths: [], nodes: []):
        self.paths = paths
        self.nodes = nodes

    @staticmethod
    def to_model(graph: hide_and_seek_pb2.Graph):
        paths = []
        for p in graph.paths:
            paths.append(Path.to_model(p))

        nodes = []
        for n in graph.nodes:
            nodes.append(Node.to_model(n))

        return Graph(paths=paths, nodes=nodes)


class GameConfig:
    def __init__(self, graph: Graph,
                 police_income_each_turn: float,
                 thief_income_each_turn: float,
                 max_turn: int,
                 visible_turns: [],
                 chat_box_max_size: int,
                 chat_cost_per_char: float):
        self.graph = graph
        self.police_income_each_turn = police_income_each_turn
        self.thief_income_each_turn = thief_income_each_turn
        self.max_turn = max_turn
        self.visible_turns = visible_turns
        self.chat_box_max_size = chat_box_max_size
        self.chat_cost_per_char = chat_cost_per_char

    @staticmethod
    def to_model(config: hide_and_seek_pb2.GameConfig):
        return GameConfig(graph=Graph.to_model(config.graph),
                          police_income_each_turn=config.incomeSettings.policeIncomeEachTurn,
                          thief_income_each_turn=config.incomeSettings.thievesIncomeEachTurn,
                          max_turn=config.turnSettings.maxTurns,
                          visible_turns=config.turnSettings.visibleTurns,
                          chat_box_max_size=config.chatSettings.chatBoxMaxSize,
                          chat_cost_per_char=config.chatSettings.chatCostPerCharacter)


class Team(enum.Enum):
    FIRST = hide_and_seek_pb2.Team.FIRST
    SECOND = hide_and_seek_pb2.Team.SECOND

    @staticmethod
    def to_model(team: hide_and_seek_pb2.Team):
        if team == hide_and_seek_pb2.Team.FIRST:
            return Team.FIRST
        return Team.SECOND


class AgentType(enum.Enum):
    THIEF = hide_and_seek_pb2.AgentType.THIEF
    POLICE = hide_and_seek_pb2.AgentType.POLICE

    @staticmethod
    def to_model(agent_type: hide_and_seek_pb2.AgentType):
        if agent_type == hide_and_seek_pb2.AgentType.THIEF:
            return AgentType.THIEF
        return AgentType.POLICE


class Agent:
    def __init__(self, id: int, team: Team, agent_type: AgentType, node_id: int, is_dead: bool):
        self.id = id
        self.team = team
        self.agent_type = agent_type
        self.node_id = node_id
        self.is_dead = is_dead

    @staticmethod
    def to_model(agent: hide_and_seek_pb2.Agent):
        return Agent(id=agent.id, team=agent.team, agent_type=agent.type, node_id=agent.node_id, is_dead=agent.is_dead)


class Chat:
    def __init__(self, id: str, from_agent_id: int, text: str):
        self.id = id
        self.from_agent_id = from_agent_id
        self.text = text

    @staticmethod
    def to_model(chat: hide_and_seek_pb2.Chat):
        return Chat(id=chat.id, from_agent_id=chat.fromAgentId, text=chat.text)


class GameView:
    def __init__(self, status: GameStatus,
                 result: GameResult,
                 turn: Turn,
                 config: GameConfig,
                 viewer: Agent,
                 balance: float,
                 visible_agents: list,
                 chat_box: list):
        self.status = status
        self.result = result
        self.turn = turn
        self.config = config
        self.viewer = viewer
        self.balance = balance
        self.visible_agents = visible_agents
        self.chat_box = chat_box

    @staticmethod
    def to_model(view: hide_and_seek_pb2.GameView):
        visible_agents_model = []
        for visible_agents in view.visible_agents:
            visible_agents_model.append(Agent.to_model(visible_agents))

        chat_box_model = []
        for chat in view.chatBox:
            chat_box_model.append(Chat.to_model(chat))
        return GameView(status=GameStatus.to_model(view.status),
                        result=GameResult.to_model(view.result),
                        turn=Turn.to_model(view.turn),
                        config=GameConfig.to_model(view.config),
                        viewer=Agent.to_model(view.viewer),
                        balance=view.balance,
                        visible_agents=visible_agents_model,
                        chat_box=chat_box_model
                        )
