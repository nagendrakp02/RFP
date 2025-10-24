from langgraph.graph import StateGraph, START, END
from src.nodes.rfp_node import RFPNode

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(dict) # RFP state is a dict

    def build_rfp_graph(self):
        node = RFPNode(self.llm)
        self.graph.add_node("extract_text", node.extract_text)
        self.graph.add_node("extract_structured_data", node.extract_structured_data)
        self.graph.add_edge(START, "extract_text")
        self.graph.add_edge("extract_text", "extract_structured_data")
        self.graph.add_edge("extract_structured_data", END)
        return self.graph

    def setup_graph(self):
        self.build_rfp_graph()
        return self.graph.compile()
