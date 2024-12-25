import flet

def BlacklistAppender(page: flet.Page):
    def amenity_selected(e):
        amenity_chips.update()

    title = flet.Row([flet.Icon(flet.Icons.ADD_TASK_OUTLINED), flet.Text("BlackListed")])
    amenities = [] # here is pre-load array from skibidi database
    amenity_chips = flet.Row(wrap=True)
    for amenity in amenities:
        amenity_chips.controls.append(
            flet.Chip(
                label=flet.Text(amenity),
                on_select=amenity_selected,
                selected=True
            )
        )
    
    

    chipi = flet.Column(controls=[title, amenity_chips])
    ######################
    def get_from_input(e):
        if input_field.value == '':
            return
        
        chipi.controls[1].controls.append(
            flet.Chip(
                label=flet.Text(input_field.value),
                on_select=amenity_selected,
                selected=True
            )

        )
        input_field.value = ''
        page.update()
        input_field.focus()
    input_field = flet.TextField(border_color="#7289da", hint_text="мы это будем игнорировать", on_submit=get_from_input)
    
    

    def delete_selected(e):
        newBorn = []
        for item in chipi.controls[1].controls:
            if item.selected != False:
                newBorn.append(item)
                #chipi.controls[1].controls.remove(item)
        chipi.controls[1].controls = newBorn
        page.update()
        
    
    def clear_all_inputs(e):
        chipi.controls[1].controls = []
        page.update()

    return flet.Container(flet.Column([
        chipi, input_field,
        flet.Row([
            flet.ElevatedButton(text="Очистить все", on_click=clear_all_inputs, bgcolor=flet.colors.RED, color=flet.colors.WHITE),
            flet.ElevatedButton(text="Очистить неиспользуемые", on_click=delete_selected, bgcolor="#7289da", color=flet.colors.WHITE)
        ])
        
        ]))

def main(page: flet.Page):
    page.add(BlacklistAppender(page))

if __name__ == "__main__":
    flet.app(main)