from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import requests
from my_tools.calculator import add, sub, multiplication, division
from my_tools.greet import say_hello
from my_tools.fun import tell_joke
from my_tools.dictionary import word_meaning

# langchain is a kind of high level frame work that allows us to build AI application
# langgraph is a little bit more of a complex framework that allows us to built AI Agents
# langchain OpenAI obviously allows us to use OpenAI within kind of langchain and langgraph which are kind of coupled together
# dotenv module allows us to load these environmnet variable files from within our python script.

# An AI agent has access to tools.
# so what we are going to learn how to make a simple python tool that the agent can use so that it can go out and do something beyond just simply responding to your message

# we are going to make a really simple tool , which is a calculator but we could make any kind of tool that we want. a tool that saves a file to a node, a tool that calls an API , a tool that on or off your lights.

load_dotenv()

@tool
def motivate():
    """Useful for motivation"""
    return "You don’t need to be the best today — just better than yesterday."




# it just looks in the current directory for this .env file and loads in the variables so we can use them later on our program.

def main():
    # intialize our chatBot and our AI Agent
    # before AI agent we are going to have an LLM that acts like the brain

    model = ChatOpenAI(temperature=0)

    # The higher temperature you go here, the more random the module is going to be.
    # if temperature = 0 it means you don't really want randomness at all

    tools=[add,sub,multiplication,division,say_hello,tell_joke,word_meaning]
    # create an agent

    agent_executer = create_react_agent(model,tools)

    # here we are using a pre-built agent that just takes some kind of model and some kind of tools and automatically handles kind of how to use these tools and how to utilize models

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    # The idea here is, we want to keep looping and allow the user to kind of interact with us like a chatbot.

    while True:
        user_input = input("\nYou: ").strip()
        # strip() removes the extra spaces
        if user_input == "quit":
            break
        print("\nAssistant: ",end="")
        # we are able to stream the response from our LLM using this agent_executer(which is our agent).
        for chunk in agent_executer.stream(
            {"messages":[HumanMessage(content=user_input)]}):

            # chunks are essentially parts of response coming from our agent
            if "agent" in chunk and "messages" in chunk["agent"]:
                # checking if there are messages in that particular response(current chunk) and making sure that chunks come from the agent.
                for message in chunk["agent"]["messages"]:
                    print(message.content,end="")
                # this is going to do is allow us to stream these longer responses from the agent.So it look's like the agent's kind of typing word by word rather than just printing the message at once.
                print()
if __name__=="__main__":
    main()






    







