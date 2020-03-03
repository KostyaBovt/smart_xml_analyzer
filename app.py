import sys
from bs4 import BeautifulSoup

from config import DEFAULT_ORIG_ID

def get_file_soup(file):
	with open(file) as fd:
		soup = BeautifulSoup(fd, "lxml")
	return soup

def compare_elements(orig_element, new_element):
	score = 0
	for orig_key, orig_value in orig_element.attrs.items():
		if orig_value and new_element.attrs.get(orig_key) == orig_value:
			score += 1
	if orig_element.text.strip() == new_element.text.strip():
		score += 1
	return score

def constuct_path_element(parent, child):
	siblings = parent.find_all(child.name, recursive=False)
	child_index_str = ""
	if len(siblings) > 1:
		for index, sibling in enumerate(siblings, 1):
			if sibling is child:
				child_index_str = f"[{index}]"
	return f'{child.name}{child_index_str}'	
	
def get_path(element):
	path = []
	child = element
	for parent in child.parents:
		path_element = constuct_path_element(parent, child)
		path.append(path_element)
		child = parent
	path.reverse()
	return " > ".join(path)


if __name__ == '__main__':
	soup_orig = get_file_soup(sys.argv[1])
	soup_new = get_file_soup(sys.argv[2])

	id_orig = sys.argv[3] if len(sys.argv) == 4 else DEFAULT_ORIG_ID
	element_orig = soup_orig.find(id=id_orig)

	candidate_elements = soup_new.find_all(element_orig.name)
	candidates = [{"element": candidate_element, "score": 0} for candidate_element in candidate_elements]
	for candidate in candidates:
		candidate["score"] = compare_elements(element_orig, candidate["element"])

	best_candidate = max(candidates, key=lambda candidate: candidate["score"])
	path = get_path(best_candidate["element"])
	print(path)
