# 0) General imports
from unittest import TestCase

# 1.1) Import classes to test
from app import pagerank


class PageRankTests(TestCase):
    def setUp(self):
        # 1) Provide test scenarios
        graph_one = [[1], [0]]
        graph_two = [[1], [0], [2]]
        graph_three = [[1], [0], [0, 1]]
        graph_four = [[], [0], [1]]

        # 2) Provide the final PageRank values expected for each scenario
        result_graph_one = [1.0, 1.0]
        result_graph_two = [1.0, 1.0, 1.0]
        result_graph_three = [0.2608695652297508, 0.2608695652226441, 0.3717391304422678]
        result_graph_four = [0.15000000000000002, 0.2775, 0.385875]

        # 3) Save to instance variables
        self.graphs = [graph_one, graph_two, graph_three, graph_four]
        self.expected_results = [result_graph_one, result_graph_two, result_graph_three, result_graph_four]

    def test_init_creates_right_amount_of_nodes(self):
        # 1) Iterate over all test graph scenarios
        for graph in self.graphs:
            # 1.1) Initialize a PageRank-Scenario
            app = pagerank.PageRankApp(graph, 1, 0.85, 15, False)
            print(app)
            # 1.2) Test whether the amount of initialized nodes is equal to the length of nodes in the passed list
            assert len(app.graph.nodes) == len(graph)
    
    def test_final_node_value(self):
        # 1) Iterate over all test graph scenarios
        for n in range(len(self.graphs)):
            # 1.1) Initialize a PageRank-Scenario
            app = pagerank.PageRankApp(self.graphs[n], 1, 0.85, 15, False)

            # 1.2) Perform a PageRank-Calculation for the graph
            app.start()

            # 1.3) Save the final PageRank for each node to a list
            final_node_values = []
            for node in app.graph.nodes:
                final_node_values.append(node.rank_value)

            # 1.3) Compare the list with the expected results
            assert final_node_values == self.expected_results[n]

    def test_malformed_graph(self):
        pass
            

    