"""
by: Philipp Machácek, Felix Siegmann @ TBS1
"""
import sqlite3
from os import path as path
cur_path = path.dirname(__file__)
global db_file
db_file = path.join(cur_path, "..\\..\\db\\my_wiki.sqlite")

class PageNode:
    """
    Class PageNode, represents one page
    """
    def __init__(self, starting_rank: float, 
                id: int,
                incoming: list,
                outgoing: list):
        """
        Constructor of class PageNode
        :param starting_rank: the default rank for this node
        :param id: this node's id
        :param incoming: list of nodes by id who link to this node
        :param outgoing: list of nodes by id this node links to
        """
        self.rank_value = starting_rank
        self.id = id
        self.incoming_ids = incoming
        self.outgoing_ids = outgoing

    def get_own_title_from_db(self):
        # 1) Initialize db connection and cursor
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        
        # 2) Get title by id from database file, increment id by 1 to align with mediawiki scheme
        cur.execute("SELECT page_title from page WHERE page_id = ?", (self.id + 1,))
        result = cur.fetchone()
        
        # 3) Return the page title
        return result[0]


class Graph:
    """
    Class Graph, represents a system of interlinked pages (PageNodes)
    """
    def __init__(self, nodes: list):
        """
         Constructor of class Graph
         :param nodes: list of nodes this graph contains
         """
        self.nodes = nodes

    def output(self):
        """
        function output
        prints nodes and their values to the screen
        :return return_string String current status of nodes
        """
        return_string = ""
        total_value = 0
        for n in self.nodes:
            return_string += f"page_title = {n.get_own_title_from_db()} page_id = {n.id} \n PageRank-Value = {n.rank_value} \n"
            total_value += n.rank_value
        return_string += f"\n TOTAL VALUE: {str(round(total_value, 6))} \n"
        return return_string

    def show_graph(self):
        for n in self.nodes:
            print(f"{n.id}, HAS INCOMING {n.incoming_ids}, HAS OUTGOING {n.outgoing_ids}")

    def get_node(self, id:int):
        """
        function get_node
        returns a node contained in this graph by id
        :param id: node id to be searched for
        :return: PageNode with this id
        """
        for node in self.nodes:
            if node.id == id:
                return node


class PageRankApp:
    """
    Class that represents a specific PageRank calculation scenario
    """
    def __init__(self, scenario: list, default_rank: float, dampening_factor: float, iterations: int):
        """
        Constructor of class PageRankApp
        :param scenario: list of lists, each list containing incoming node ids for a node in the scenario
        :param default_rank: Page-Rank nodes start out with
        :param dampening_factor: dampening factor to be applied
        :param iterations: number of iterations to approximate result of system of linear equations for graph
        """
        self.scenario = scenario
        self.default_rank = default_rank
        self.dampening_factor = dampening_factor
        self.graph = Graph(self.build_graph())
        self.iterations = iterations

    def start(self):
        """
        starts execution
        """
        self.iterate(verbose=False)

    def build_graph(self):
        """
        function build_graph
        Initializes list of PageNode-Objects
        sets their rank, id, incoming_ids and outgoing_ids
        :return: list of PageNode-Objects
        """
        nodes = []
        for i in range(len(self.scenario)):
            nodes.append(PageNode(self.default_rank, i, self.scenario[i],
                         list(set([self.scenario.index(n) for n in self.scenario if i in n]))))
        return nodes

    def iterate(self, verbose: bool):
        """
        function iterate
        function that iterates over system of linear equations a specified amount of times
        uses updated page within each iteration
        :params verbose: boolean that specifies if output is desired after each iteration
        """
        # 1) iterate _ times
        for _ in range(self.iterations):
            # 2) each time, iterate over all nodes in graph
            for node in self.graph.nodes:
                # 3) initialize or reset temp_sum that represents sum of weight of linking nodes
                temp_sum = 0

                # 4) for the current node, iterate over all nodes that link to it
                for id in node.incoming_ids:
                    # 5) increment temp_sum by weight of each incoming node
                    temp_sum = temp_sum + self.graph.get_node(id).rank_value / len(self.graph.get_node(id).outgoing_ids)

                # 6) update rank for current node using Page-Rank formula using dampening factor
                #    round to the 8th decimal
                node.rank_value = (1 - self.dampening_factor) + self.dampening_factor * temp_sum

            if verbose:
                print("ITERATION " + str(_) + "\n " + self.graph.output() + "~~~~~~~~~~~~ \n")
        
        print(f"FINAL NODE STATUS\n {self.graph.output()}")
        

graph_one = [[1], [0]]
graph_two = [[1], [0], [2]]
graph_three = [[1], [0], [0, 1]]
graph_four = [[], [0], [1]]