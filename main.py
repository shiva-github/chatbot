from processInput.agent1_action import Action
from processInput.agent2_store import store
from processOutput.agent1_validate import Validate

while True:
	userInput = input("You: ")
	if(userInput == ''):
		break
	tempararyOutput = Action(userInput).takeAction()

	finalOutput = Validate(tempararyOutput).validateResponse()

	print('JARVIS: '+ finalOutput)
