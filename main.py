from reactpy import component,html,use_state
from reactpy.backend.fastapi import configure

from fastapi import FastAPI

@component
def Item(text,initial_done=False):
    
    done, set_done = use_state(initial_done)

    def handle_click(event):
        set_done(not done)
    

    attrs = { "style" : { "color":"#ccc" } } if initial_done else {}
    if(done):
        return html.li(attrs,text),
    else:
      return html.li(
          html.span(text),
          html.button({"on_click":handle_click},"Hecho")
      )
@component
def Counter(state,set_state):
    def handleCounter(event):
      set_state(state+1)
    return html.div(
        html.p(state),
        html.button({"on_click":handleCounter},'Add')
    )

@component
def App():
    count,set_count = use_state(1)
    return html.div(
        html.h1("Count"),
        Counter(count,set_count)
        
    ) 

app = FastAPI()
configure(app,App)