import flet as ft
def main(Page):
    Page.title = "Counter App"
    Page.window_width = 300
    Page.window_height = 300
    Page.window_resizable = False
    Page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    Page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    def add(e):
        Tfield.value = int(Tfield.value)+1
        Page.update()

    def minus(e):
        Tfield.value = int(Tfield.value)-1
        Page.update()
        
    Tfield = ft.Text(value="0")
    columns = [ft.IconButton(ft.icons.ADD,on_click=add),Tfield,ft.IconButton(ft.icons.REMOVE,on_click=minus)]
    Page.add(ft.Row(columns))


ft.app(target=main)
