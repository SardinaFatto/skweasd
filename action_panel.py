import flet
import datetime

def ActionPanel(page):
    # on change
    def set_selected_date(e):
        print(DickPicker.value)
        TIMEDELTA_INFO.value = f"Парсим дропы с {DickPicker.value}"
        page.update()
        return

    # on picking date
    def select_date(e):
        page.open(DickPicker)
        page.update()

    # date picker setup
    sixDaysBefore = datetime.datetime.now() - datetime.timedelta(days=7)
    DickPicker = flet.DatePicker(value=datetime.datetime.now(), first_date=sixDaysBefore, last_date=datetime.datetime.now(), on_change=set_selected_date)
    
    
    PANEL = flet.Row()
    START_SEARCH = flet.ElevatedButton(
            text="Начать поиск",
            bgcolor=flet.colors.WHITE,
            color=flet.colors.BLACK
        )
    
    SET_TIMEDELTA = flet.ElevatedButton(
            text="Установить временной промежуток поиска",
            bgcolor=flet.colors.BLUE_300,
            color=flet.colors.BLACK,
            icon=flet.Icons.CALENDAR_MONTH,
            on_click=select_date
        )
    
    TIMEDELTA_INFO = flet.Text("")

    PANEL.controls.append(START_SEARCH)
    PANEL.controls.append(SET_TIMEDELTA)
    PANEL.controls.append(TIMEDELTA_INFO)
    PANEL.controls.append(flet.Text("10202 совпадений"))

    return PANEL

if __name__ == "__main__":
    def main(page: flet.Page):

        # on change
        def set_selected_date(e):
            print(DickPicker.value)
            page.update()
            return

        # on picking date
        def select_date(e):
            page.open(DickPicker)
            page.update()

        # date picker setup
        sixDaysBefore = datetime.datetime.now() - datetime.timedelta(days=7)
        DickPicker = flet.DatePicker(first_date=sixDaysBefore, last_date=datetime.datetime.now(), on_change=set_selected_date)

        page.add(ActionPanel(page))
    flet.app(main)