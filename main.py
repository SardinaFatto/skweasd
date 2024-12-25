import flet
from blacklist_integrator import BlacklistAppender
from chat_selector import ParseChatSelector
from action_panel import ActionPanel
from fields_container import GetFIelds

def main(page: flet.Page):
    page.title = "voyeur coin"
    rail_vl = flet.ListView(spacing=10, expand=True)
    rail_vl.controls.append(ActionPanel(page))
    rail_vl.controls.append(BlacklistAppender(page))
    rail_vl.controls.append(ParseChatSelector(page))
    page.bgcolor='#36393e'
    page.add(flet.Row(
        [  
            flet.Container(
                rail_vl,
                expand=True,
                margin=5,
                padding=8,
                bgcolor='#36393e'
            ),
            flet.Container(
                GetFIelds(page),
                expand=True,
                margin=5,
                padding=8,
                bgcolor='#36393e'
            ),
            
        ], 
        expand=True
    ))

flet.app(target=main, assets_dir="assets")