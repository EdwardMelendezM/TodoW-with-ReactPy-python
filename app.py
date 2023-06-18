from reactpy import component,html,use_state,use_effect
from reactpy.backend.fastapi import configure

from fastapi import FastAPI

list_todos = [
   {
      "id":0,
      "name":"To do homework"
   },
   {
      "id":1,
      "name":"To do cook"
   },
   {
      "id":2,
      "name":"To do clean"
   }
]

@component
def App():
    todos,set_todos = use_state(list_todos)
    value_form, set_value_form = use_state("")

    list_homework = [TodoItem(item,set_todos) for item in todos ]
    
    
    def handleChangeInput(event):
       set_value_form(event["target"]["value"])
       
    def add_new(new):
       new_element = {
          "id":6,
          "name":new
       }
       new_list = todos.append(new_element)
       set_todos(new_list)

       

    return html.div(
        html.h1("Count"),
        html.div(
          html.input({"on_change":handleChangeInput}),
          html.button({"on_click":lambda event: add_new (value_form)},"add")  
        ),
        list_homework   
    )

@component
def TodoItem(item:list,set_todos):
  
  def handle_remove(event):
    print("Delete this element")
  
  return html.div(
      html.p(item["name"]),
      html.button({"on_click":handle_remove},"Remove")
   )



app = FastAPI()
configure(app,App)