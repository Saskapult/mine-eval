import os
import json
from kg_gen import KGGen, Graph
import time


essays_path = "./kg-gen/MINE/essays.json"


def make_graphs(model, just_one=False):
	essays = None
	with open(essays_path, "r") as f:
		essays = json.load(f)
	
	kg = KGGen(
		model=model,
		api_key=os.getenv("OPENAI_API_KEY"),
	)
	graphs = []
	for i, essay in enumerate(essays):
		print(f"Evaluating essay {i+1}/{len(essays)}")
		if model == "openai/gpt-4o" and i in [60, 77]:
			print("Skipped due to GPT-4o errors")
			continue

		topic = essay["topic"]
		content = essay["content"]
		graph = kg.generate(
			input_data=content,
			context=topic,
		)
		graphs.append(graph)
		if just_one:
			print("Note: Only generating one graph")
			break

	return graphs


def save_graph_json(graph, path):
	data = {
		"entities": list(graph.entities),
		"edges": list(graph.edges),
		"relations": list(graph.relations),
	}
	with open(path, "w") as f:
		json.dump(data, f, indent=2)


def load_graph_json(path):
	graph = None
	with open(path, "r") as f:
		data = json.load(f)
		graph = Graph(
			entities = data["entities"],
			relations = data["relations"],
			edges = data["edges"],
		)
	return graph


def main():
	model = os.getenv("MODEL_TO_TEST", "openai/gpt-4o")
	print(f"Generating results for model '{model}'")

	start = time.time()

	# graphs = make_graphs(model, just_one=True)
	graphs = make_graphs(model)

	end = time.time()
	duration = end - start
	print(f"That took {duration:.2f} seconds")

	if os.path.exists("./kg-gen/MINE/KGs"):
		print("Trashing old data")
		os.system("trash ./kg-gen/MINE/KGs")
	os.makedirs("./kg-gen/MINE/KGs")

	for i, graph in enumerate(graphs):
		print(f"Saving graph {i+1}/{len(graphs)}")
		save_graph_json(graph, "./kg-gen/MINE/KGs/" + f"{i+1}.json")


if __name__ == "__main__":
	main()
