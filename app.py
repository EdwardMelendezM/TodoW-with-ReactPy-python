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
global list_homework

@component
def App():
    todos,set_todos = use_state(list_todos)
    value_form, set_value_form = use_state("")
    
    list_homework = [TodoItem(item,set_todos) for item in todos ]
    

    def handleChangeInput(event):
       set_value_form(event["target"]["value"])
       
    def add_new(new):
       new_element = {
          "id":5,
          "name":new
       }
       
       new_list = todos
       new_list.append(new_element)
       set_todos(new_list)
       print(todos)

    def update_list():
       list_homework= [TodoItem(item,set_todos) for item in todos ]
    use_effect(update_list,dependencies=[todos])

    container = { "style" : { "display":"flex","alignt-items":"center","justify-content":"center","width":"100vw","hight":"100vh","flex-direction":"column" } }
    return html.div(
       container ,
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
  container_todo_item = { "style" : { "font-size":"15"} }
  return html.div(container_todo_item,
      html.p(item["name"]),
      html.button({"on_click":handle_remove},"Remove")
   )



app = FastAPI()
configure(app,App)