from datetime import datetime
import time
import pyperclip
from dotenv import load_dotenv
import os
from openai import OpenAI


# Load variables from .env file
load_dotenv()

PROG_DIR = os.environ.get('PROG_DIR')
API_KEY = os.environ.get('API_KEY')
DB = f"{PROG_DIR}/db.csv"
def set_clipboard(text):
    pyperclip.copy(text)

def get_clipboard():
    return pyperclip.paste()

def get_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def set_file_content(file_path,content):
    with open(file_path, 'w') as f:
        f.write(content)
    return True

def append_file_content(file_path,content):
    with open(file_path, 'a') as f:
        f.write(content)
    return True


# =>What is a process?
# =>4:What is a process?
def get_chatgpt_answer(question,model="gpt-3.5-turbo"):
    set_clipboard("&>Loading...")
    # time.sleep(5)
    client = OpenAI(
        # This is the default and can be omitted
        api_key=API_KEY,
    )
    messages = [
        {"role":"system","content":"You are an expert in major of computer science and field of operating systems. Answer the following questions:"},
        {"role":"user","content":question}
    ]
    print("Model: ",model)
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
        )
        print(response)
        answer =  response.choices[0].message.content
        # answer = response["choices"][0]["message"]["content"]
        fetched =  f"&> {answer}"
        set_clipboard(fetched)
        return fetched
    except Exception as e:
        print(e)
        error =  "&>Error: Network error - {e}"
        set_clipboard(error)
        return error

def handle_clipboard_content(content,changeDef):

    if content.startswith("->"):
        # get a file content : ->2
        filename = content[2:]
        file_path = f"{PROG_DIR}/documents/slides/txt/{filename}.txt"
        try:
            content = get_file_content(file_path)
            set_clipboard(content)
            return content
        except Exception as e:
            error =  f"&>Error: Getting File Content - {e} | {content}"
            # content = f"{content} - {error}"
            set_clipboard(error)
            return error
    
    elif content.startswith("=>"):
        model="gpt-3.5-turbo"
        # get a chatgpt answer : =>What is a process?
        question = content[2:]
        if question.startswith("4:"):
            question = question[2:]
            model="gpt-4"
        answer = get_chatgpt_answer(question,model)
        set_clipboard(answer)
        return answer
    
    elif content.startswith("&>"):
        # just return the value : &>hello
        return content
    else:
        if changeDef:
            error =  "&>Error: Wrong formatting - eg[->{i/0}, =>{network}|4:, &>{mgbo}]"
            content = f"&>{content} - {error}"
            set_clipboard(content)
        return content

if __name__ == "__main__":
    counter = 0
    while(True):
        try:
            progress = get_file_content(f"{PROG_DIR}/progress.txt").strip()
            # set_file_content(f"{PROG_DIR}/progress.txt","working1")
            # print("Progress: ",progress)
            if progress != "working":
                timestamp = datetime.timestamp(datetime.now())
                set_file_content(f"{PROG_DIR}/progress.txt",f"working,{timestamp}")

                clipboard_content = get_clipboard().strip()
                changeDef = False
                if counter > 40:
                    changeDef = True
                # if changeDef:
                #     print("Manipulate",datetime.now())
                # else:
                #     print("Do not manipulate",datetime.now())
                handle_clipboard_content(clipboard_content,changeDef)

                set_file_content(f"{PROG_DIR}/progress.txt",f"free,{timestamp}")
        except Exception as e:
            print(e)
        counter += 5
        # Run every minute by cronjob then relooping every 5 seconds for 55 seconds then break to avoid overlapping
        if(counter > 50):
            break

        time.sleep(5)
    
