import sys, os

# 1) Write necessary import folders to path for relative imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

# 1.1) Import classes to test
from app import pagerank

# 2) Clean path after necessary imports have been made
sys.path.remove(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

class PageRankTests:
    