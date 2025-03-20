import os
import json


def read_result_json(path):
	data = None
	with open(path, "r") as f:
		data = json.load(f)
	return data


def read_results_json():
	results = []
	for f in os.listdir("./kg-gen/MINE/KGs"):
		print(f)
		if f.endswith("_results.json"):
			result = read_result_json("./kg-gen/MINE/KGs/" + f)
			results.append(result)
	return results


def result_sum(results):
	count = len(results) - 1
	score_sum = 0
	for result in results:
		if "evaluation" in result.keys():
			score_sum += result["evaluation"]
	return count, score_sum


def main():
	files = read_results_json()
	for file in files:
		count, score_sum = result_sum(file)
		print(f"Score {score_sum} / {count} ({(score_sum/count):.2f})")


if __name__ == "__main__":
	main()
