from pydantic_ai.models.google import GoogleModel
from pydantic_ai import Agent
from pydantic_ai.providers.google import GoogleProvider
from dotenv import load_dotenv
import tools
import httpx

# 加载环境变量
load_dotenv()
# 初始化模型
model = GoogleModel("gemini-2.5-flash")
# 初始化agent
agent = Agent(model,
              system_prompt="You are an experienced programmer.",
              tools=[tools.read_file, tools.list_files, tools.rename_file])

def main() -> None:
  print("Hello from MyFirst-Ai-Agent")
  history = []
  while True:
    user_input = input("Your input: ")
    if user_input.lower() == "exit":
      break
    try:
      response = agent.run_sync(user_input)
      # 修复：避免使用message_history，简化实现
      print(response.output)
    except httpx.ConnectTimeout:
      print("Error: Connection timeout. Please check your network connection or try again later.")
    except Exception as e:
      print(f"Error: An unexpected error occurred: {e}")
  
if __name__ == "__main__":
  main()

