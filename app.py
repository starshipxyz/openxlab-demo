import gradio as gr

def greet(name):
    envVar = os.environ.get('token')
    return "Hello " + name + '-' + envVar  + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    
if __name__ == "__main__":
    demo.launch()   
