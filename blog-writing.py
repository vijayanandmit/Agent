llm_config = {"model": "gpt-3.5-turbo")

task = '''
	write a concise but engaging blogpost about Deeplearning.ai
	make sure that blogpost is within 200 words.
	'''

import autogen

writer = autogen.AssistantAgent(
	name="Writer",
	system_message="You are a writer. You write engaging and concise"
		"blogpost with title on given topics. You mush polish your"
		"wriiting base"
		""
