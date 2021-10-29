"""
by: Philipp Machácek, Felix Siegmann @ TBS1
"""
import src.app.pagerank as pagerank


def main():
    graph_mediawiki = [[11],[1, 4, 10],[],[1, 11],[],[1],[1, 8, 21],[1, 7, 10],[1],[1, 8],[1, 22],[1, 14, 22, 27],[1],[32],[1],[1],[1, 16],[1],[1, 22],[1, 9],[1, 6, 10, 22],[1],[1],[1],[1, 6, 17, 18, 26],[1, 17],[1, 28, 29],[1, 18, 22, 25, 29, 31],[1, 9],[1, 22, 27],[1, 7, 23],[1, 12, 22, 27, 30],[1, 22],[]]
    # 1) Initialize specific PageRank-Scenario
    app = pagerank.PageRankApp(scenario=graph_mediawiki, default_rank=1, dampening_factor=0.85, iterations=1000)
    # 2) Start Execution)
    app.start()
    
if __name__ == "__main__":
    main()