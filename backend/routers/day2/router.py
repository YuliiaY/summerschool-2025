import os

from dotenv import load_dotenv
from fastapi import APIRouter
from openai import OpenAI

from ...models import ChatRequest, ChatResponse

load_dotenv()
client = OpenAI(

  base_url="https://openrouter.ai/api/v1",

  api_key=os.getenv("OPENROUTER_API_KEY"),

)

router = APIRouter(prefix="/api/day2", tags=["day2"])


@router.post("/echo", response_model=ChatResponse)
def echo(request: ChatRequest) -> ChatResponse:
    return ChatResponse(reply=f"Echo (day 2): {request.message}")


@router.get("/health")
def health():
    return {"ok": True}


@router.post("/solve_cot", response_model=ChatResponse)
def solve_cot(request: ChatRequest) -> ChatResponse:
    completion = solve_with_cot(request.message)
    return ChatResponse(reply=f"Question:\n{request.message}\nAntwort:\n{completion.choices[0].message.content}")


@router.post("/solve_self_consistency", response_model=ChatResponse)
def solve_self_consistency(request: ChatRequest) -> ChatResponse:
    completions = []
    print("start")
    for x in range(3):
        completion = solve_with_cot(request.message)
        print(f"got {x} completion")
        completions.append(completion)

    user_prompt = f"""
        #ROLE
        you are a reviewer that need to find the best answer to a given question.

        #INSTRUCTIONS
        You will get a question and a set of diferent answers to this question.
        Extract the final, extracted answer from each response (e.g., a number, a word, or a sentence).
        Determine the most frequently mentioned answer (majority decision) and return it as the final result. 

        #QUESTION
        {request.message}

        #ANSWERS
        Here are the answers for the question. Each answer started with START ANSWER and ended with END ANSWER.

"""
    for completion in completions:
        user_prompt = user_prompt + "\nSTART ANSWER" + completion.choices[0].message.content + "\nEND ANSWER"

    answer = client.chat.completions.create(
        model="mistralai/mistral-nemo:free",
        messages=[
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )
    return ChatResponse(reply=f"Question:\n{request.message}\nAntwort:\n{answer.choices[0].message.content}")


def solve_with_cot(problem_description):
    system_prompt = """
        # ROLE
        You are a panel of experts in Physics, Computer Science, Mathematics, Political Philosophy, Law, Economics, and Medicine.

        # INSTRUCTIONS
        Respond to the user's query using a multi-step reasoning process.
        
        ## Thinking Process
        - MUST engage in thorough, systematic reasoning before EVERY response
        - Demonstrate careful analysis and consideration of multiple angles
        - Break down complex problems into components
        - Challenge assumptions and verify logic
        - Show authentic curiosity and intellectual depth
        - Consider edge cases and potential issues
        - Never skip or shortcut the thinking process

        ## Thinking Format
        - Use natural, unstructured thought process
        - No nested code blocks within thinking sections
        - Show progressive understanding and development of ideas

        ## Thought Quality Standards
        1. Depth
        - Explore multiple approaches and perspectives
        - Draw connections between ideas
        - Consider broader implications
        - Question initial assumptions

        2. Rigor
        - Verify logical consistency
        - Fact-check when possible
        - Acknowledge limitations
        - Test conclusions

        3. Clarity
        - Organize thoughts coherently
        - Break down complex ideas
        - Show reasoning progression
        - Connect thoughts to conclusions
"""
    
    completion = client.chat.completions.create(
        temperature=0.6,
        model="mistralai/mistral-nemo:free",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": problem_description
            }
        ]
    )
    return completion
