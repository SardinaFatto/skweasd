import flet
import json
import requests
import datetime

class WorkDataClass():
    def __init__(self):
        self.user_token = ""
        self.blacklist = []
        self.witelist = []
        self.last_date = False
        self.last_clock_time = False
        self.datetime = None
        self.channel_id = 0
        self.channel_details = ""

SESSION_DATA = WorkDataClass()

COLLORS = {
    "discord-light-grey": "#424549",
    "discord-midle-grey": "#36393e",
    "discord-hard-grey" : "#282b30",
    "discord-black-grey": "#1e2124",
    "discord-blue"      : "#7289da",
    "discord-red"       : "#ED4245",
    "discord-white"     : "#FFFFFF"
}

async def princonsole(text, text_color=COLLORS["discord-white"]):
        SESSION_DATA.console.content.controls.append(flet.Text( f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}$~/  {text}", color=text_color ))
        SESSION_DATA.console.update()

async def validate_message(response_message_json):
    # str to compare posibility
    textify_response_message_json = str(response_message_json)
    
    # white list first
    for wl_item in SESSION_DATA.witelist:
        if wl_item in textify_response_message_json:
            await princonsole(f"[WHITELIST MATCH] {response_message_json['id']}", text_color=COLLORS['discord-blue'])
            # yes, skibidi
            for bl_item in SESSION_DATA.blacklist:
                if bl_item in textify_response_message_json:
                    await princonsole(f"[BLACKLIST MATCH] {response_message_json['id']}", text_color=COLLORS['discord-red'])
                    return False
            return True

#### TEST
async def EmbifyFields(FIELD):
    VALUES = flet.Column()
    for item in FIELD['value'].split('\n'):
        VALUES.controls.append(flet.Markdown(item))

    containa = flet.Container(
        flet.Column(
            [
                flet.Markdown(FIELD['name']),
                VALUES
            ]
        ),
        margin=10,
        padding=10,
        bgcolor="#1e2124",
        border_radius=10,
        alignment=flet.alignment.center_left,
    )
    return containa

async def prittyfy_my_embed(EMBED):
    EMBED = EMBED['embeds'][0]
    fields = flet.Column()
    #print(EMBED)
    for field in EMBED['fields']:
        if field['name'] in ['Links', 'Token Description']:
            continue
        fields.controls.append(await EmbifyFields(field))

    return flet.Container(
                content=flet.Column(
                    [
                        flet.Text(SESSION_DATA.channel_details, size=18),
                        flet.Markdown(EMBED['title']),
                        flet.Row(
                            [
                                flet.Markdown(EMBED['description']), 
                                flet.ElevatedButton(
                                    "Смотреть на сайте",
                                    bgcolor="#ffffff",
                                    color="#318acb",
                                    url=f"https://photon-sol.tinyastro.io/en/lp/{EMBED['description'].replace('`','')}"
                                    )
                            ]
                        ),
                        fields
                    ]
                ),
                margin=10,
                padding=10,
                alignment=flet.alignment.center,
                bgcolor="#282b30",
                border_radius=10
    )

async def WrapNPost(MESSAGES):
    print(SESSION_DATA.console.page.controls[0].controls[0].content)
    # fill out container
    WRAPPED_MESSAGES = []
    for message in MESSAGES:
        WRAPPED_MESSAGES.append(await prittyfy_my_embed(message))
    NEW_FIELDS = flet.ListView(WRAPPED_MESSAGES)
    SESSION_DATA.console.page.controls[0].controls[0].content = NEW_FIELDS
    SESSION_DATA.console.page.update()


async def scrappy_coco():
    # scraping da chat
    chat_id           = SESSION_DATA.channel_id
    user_sesion_token = SESSION_DATA.user_token
    URL               = f'https://discord.com/api/v9/channels/{chat_id}/messages?limit=1'
    HEADERS = {
        "Authorization": user_sesion_token
    }
    MESSAGES = []

    # we need to add filering in here now (date -> whitelist -> blacklist)
    responce = requests.get(URL, headers=HEADERS)
    if responce.status_code == 200:
        await princonsole("CONNECTION CREATED")
        json_message = json.loads(responce.text)[0]
        MESSAGES.append(json_message)
    else:
        print(f"FAILED TO RECIVE DATA: {responce.status_code}")
    
    for _ in range(20):
        responce = requests.get(f"{URL}&before={MESSAGES[-1]['id']}", headers=HEADERS)
        if responce.status_code == 200:
            json_message = json.loads(responce.text)[0]
            if await validate_message(json_message):
                MESSAGES.append(json_message)
            await princonsole(f"[GET 200] MESSAGE RESPOND: {json_message['id']} added main to pull")
        else:
            print(f"FAILED TO RECIVE DATA: {responce.status_code}")
    await princonsole(f"TOTAL MESSAGES FOUND {MESSAGES.__len__()}")
    await WrapNPost(MESSAGES)
    



async def StartSearching(page, console):
    # parse messages with whitelist and date filter
    await scrappy_coco()
    # drop black filtered messages
    # embeds to my embed
    # set main page fields
    return 0

async def validate_chat(chat_id):
    # scraping da chat
    URL     = f'https://discord.com/api/v9/channels/{chat_id}'
    HEADERS = {
        "Authorization": SESSION_DATA.user_token
    }
    response = requests.get(URL, headers=HEADERS)
    if response.status_code != 200:
        return False
    return json.loads(response.text)

async def OptionPage():
    async def apply_filtes(e):
        # validating chat
        chat_info = await validate_chat(CHAT_ID_FIELD.value)
        if chat_info:
            SESSION_DATA.channel_id = CHAT_ID_FIELD.value
            await princonsole("__________ ПРИМЕНЕНЫ ФИЛЬТРЫ ________")
            await princonsole(f"CHAT NAME: {chat_info['name']}")
            await princonsole(f"CHAT ID: {chat_info['id']}")

            # trying to get filter words
            actual_blacklist = BLACK_LIST_FIELD.value.split(',')
            actual_whitelist = WHITE_LIST_FIELD.value.split(',')

            if  actual_whitelist != ['']:
                SESSION_DATA.witelist = actual_whitelist
                await princonsole(f"WHITELIST: {actual_whitelist.__len__()} фильтров")

            if  actual_blacklist != ['']:
                SESSION_DATA.blacklist = actual_blacklist
                await princonsole(f"BLACKLIST: {actual_blacklist.__len__()} фильтров")
            await princonsole("______________________________________________")

        else:
            await princonsole(f"[ERROR]: Чат с таким айди не существует {CHAT_ID_FIELD.value}", text_color=COLLORS['discord-red'])
        e.page.update()
    
    async def reset_filters(e):
        BLACK_LIST_FIELD.value = ""
        WHITE_LIST_FIELD.value = ""
        SESSION_DATA.blacklist = []
        SESSION_DATA.witelist  = []
        await princonsole(f"Настройки фильтрования сброшены")
        e.page.update()

    
    async def search_with_filters(e):
        await princonsole("Поиск запущен")
        await StartSearching(e.page, CONSOLE)

    
    WHITE_LIST_FIELD = flet.TextField( label="WHITE LIST", border_color=COLLORS['discord-blue'] )
    BLACK_LIST_FIELD = flet.TextField( label="BLACK LIST", border_color=COLLORS['discord-blue'] )
    CHAT_ID_FIELD    = flet.TextField( label="CHAT ID", border_color=COLLORS['discord-blue'] )
    APPLY_BUTTON     = flet.Button( "Применить фильтры", on_click=apply_filtes, color=COLLORS["discord-white"], bgcolor=COLLORS['discord-blue'] )
    RESET_BUTTON     = flet.Button( "Сбросить фильтры", on_click=reset_filters, color=COLLORS["discord-white"], bgcolor=COLLORS['discord-red'] )
    SEARCH_BUTTON    = flet.Button( "Начать поиск", on_click=search_with_filters, color=COLLORS["discord-black-grey"], bgcolor=COLLORS['discord-white'] )
    BUTTONS_ROW      = flet.Row( [ SEARCH_BUTTON, APPLY_BUTTON, RESET_BUTTON ] )
    CONSOLE          = flet.Container(flet.ListView( auto_scroll=True, reverse=False ), expand=True, bgcolor=COLLORS['discord-black-grey'],margin=8, padding=8 )
    SESSION_DATA.console = CONSOLE

    OPTONPS_GROUP=flet.Column(
        [
            CHAT_ID_FIELD,
            WHITE_LIST_FIELD,
            BLACK_LIST_FIELD,
            BUTTONS_ROW,
            CONSOLE
        ]
    )
    return OPTONPS_GROUP

# programm entry point
async def openWorkspace(page):
    page.title = "Bitcord Trade Helper"
    page.bgcolor = COLLORS['discord-light-grey']

    GREETER = flet.Container(
        flet.Column(
            [
                flet.Image('https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/636e0b5061df29d55a92d945_full_logo_blurple_RGB.svg'),
                flet.Text("SKIBIDI DOBDOBDOBYESYES"),
            ]
        )
    )

    FIELDS = flet.Container(
        GREETER,
        expand=True,
        margin=5,
        padding=8,
        bgcolor=COLLORS['discord-light-grey']
    )

    OPTIONS_PAGE = flet.Container(
        await OptionPage(),
        expand=True
    )

    WORKSPACE = flet.Row(
    [  
        FIELDS,
        OPTIONS_PAGE
    ], 
    expand=True
    )

    page.controls = [WORKSPACE]
    page.update()
    return True

async def check_tokin(e):
    if e.data.__len__() > 30:
        SESSION_DATA.user_token = e.data
        await openWorkspace(e.page)
        
    else:
        dlg = flet.AlertDialog(
        title=flet.Text(f"Hello, {e.data}"))
        dlg.open = True
        e.control.page.overlay.append(dlg)
        e.control.value = ""
        e.page.update()


async def LoginPage():
    PAGE = flet.Column(
        [
            flet.Text(f"Say you'r name"),
            flet.TextField(on_submit=check_tokin)
        ]
    )
    return PAGE

async def main(page: flet.Page):
    page.title = "SAY HELLO HOMEWORK SITE"
    LOGIN_PAGE = await LoginPage()
    page.add(LOGIN_PAGE)

flet.app(main)
