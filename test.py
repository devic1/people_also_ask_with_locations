import people_also_ask

k = people_also_ask.get_related_questions(text="reinforcement learning", location="in")
assert len(k) > 0
assert isinstance(k, list)
