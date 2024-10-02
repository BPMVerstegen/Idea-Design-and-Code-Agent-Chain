!pip install groq
from groq import Groq

client = Groq(
    api_key="API_KEY",
)

def IdeaAgent(prompt):
  """
  Generates an idea for an app, script or game based on user input.
  """
  print("IdeaAgent: Generating Idea...")
  chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": prompt,
          }
      ],
      model="llama-3.2-3B-preview",
  )
  idea = chat_completion.choices[0].message.content
  print("IdeaAgent: Generated Idea: ", idea)
  return idea

def DesignAgent(idea):
    """
    Generates an design for an app, script or game based on the idea.
    """
    print("IdeaAgent: Generating Design...")
    chat_completion = client.chat.completions.create(
       messages=[
           {
               "role": "user",
               "content": "You are an expert designer. Design an app, script or game based on the following idea: " + idea,
           }
       ],
        model="llama-3.2-3B-preview",
    )
    design = chat_completion.choices[0].message.content
    print("DesignAgent: Generated Design: ", design)
    return design

def CodeAgent(design):
    """
    Generates a code for an app, script or game based on the design.
    """
    print("CodeAgent: Generating Code...")
    chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": "You are an expert programmer. Write the python code for the following app, script or game design: " + design,
          }
       ],
      model="llama-3.2-3B-preview",
    )
    code = chat_completion.choices[0].message.content
    print("CodeAgent: Generated Code: ", code)
    #Save the code to a Python file
    with open("generated_code.py", "w") as f:
      f.write(code)
    print("CodeAgent: Code saved to generated_code.py")

# Test the agents
prompt = "Create an app that helps users manage and keep track of their daily tasks"
idea = IdeaAgent(prompt)
design = DesignAgent(idea)
CodeAgent(design)
