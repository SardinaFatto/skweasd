import flet
import json
import requests

def ParseDiscordChannels(channels_ids: list,  amount: int):
    return [{
    "type": "rich",
    "url": "https://t.me/nestor_trojanbot?start=d-ag_botello-DGmWTEG4ra4343y3waSuwgiUUoXHUsPzamZTQCPXZ4qX",
    "title": "Fresh Wallet 👶 swapped **0.34 SOL** for **8,020,651.75 XmasBoy**",
    "description": "```DGmWTEG4ra4343y3waSuwgiUUoXHUsPzamZTQCPXZ4qX```",
    "color": 7928396,
    "timestamp": "2024-12-24T22:27:26.810000+00:00",
    "fields": [
        {
            "name": "Stats XmasBoy",
            "value": "💰 **MC**: `$8,353`\n💧 **Liq**: `$7,323` (`86.87%`⚠️)\n📓 **Type**: SPL Token\n🪙 **Token Age**: <t:1735079214:R>\n👪 **Top 20**: `8.23%`\n🏦 **Recent Swaps**:\n┗**F**: `4` **KYC**: `3` **Unq**: `4` **SM**: `0`\n🔗 **Links**: [X](https://x.com/Ab_magma)",
            "inline": True
        },
        {
            "name": "Stats Creator",
            "value": "🚦 **AG Score**: `6/10`\n🔌 **Mint**: No 🟢 **Freeze**: No 🟢\n🎨 **Mut.**: No 🟢 **Chg.**: No 🟢\n📦 **Bundled**: `6.23%`\n🦅 **DS paid**: `n/a`\n👨‍💻 **Creator**: [DWbiWx](https://solscan.io/account/DWbiWxnLPrXHGYM4cfDgv2HPToagUcpQWmQu5rCBzGnp) (`0%` | `0.3 ◎`)\n┣ **Funding**: XT Exchange @ 13h\n┗ Drained 0 of 0\n🪂 **Airdropped**: `0%`",
            "inline": True
        },
        {
            "name": "First 10 Insider Positions",
            "value": "-",
            "inline": False
        },
        {
            "name": "Recent Swaps",
            "value": "🟢 <t:1735079242:R> [Freshy (`AFRKcu`) __ 2h__](https://solscan.io/tx/2nXTU9saq36k4LKJVe67kRfo7HD7JQxAyp58WjQjY1Vgr1Wnv2hydXCfYBXhAMHv3Csb8ryJayFdCQj4yz7Dvfxk) `0.34 SOL`・`8.4K`\n🟢 <t:1735079234:R> [**HTX Freshy** __ 1d__](https://solscan.io/tx/53UVxRyr2Jsd7Xt5VTWfFNduWoNZ6QUESCiHkBE4trrH9rJjtCzPtKrKnkUk9WjDJEU1rGG8NVmJt122TfxmPm4a) `0.94 SOL`・`7.1K`\n🟢 <t:1735079234:R> [**Kucoin Freshy** __ 1d__](https://solscan.io/tx/4QDBUazhPvRdsNBuGeqjikffSM2NYtTwHkiDYqQAEdoU88kkuK9tNa5USNjXoJ5vkSEYEYs3AzyTuH2WaJgQJviP) `0.63 SOL`・`6.8K`\n🟢 <t:1735079214:R> **XT Exchange Freshy** __13h__ `1.85 SOL`・`5.9K`",
            "inline": False
        },
        {
            "name": "First Alerted",
            "value": "🟢 <t:1735079214:R> [**XT Exchange Freshy** __13h__](https://solscan.io/tx/3mPKHzCnrpcEU4tv5hSVwr7XDdEYTumVzbhXiWRMRMC1pGEho37vq41bv2T6r3vYnJUmRzjS92uRBqwnMD5fQ1Gm) `1.85 SOL`・`5.9K`",
            "inline": False
        },
        {
            "name": "Token Description",
            "value": "Am Not Who Or What U Think I Am, I Am A PRISONER OF CONSCIENCE, In The SPIRIT OF LOVE, A RAINMAKER",
            "inline": False
        },
        {
            "name": "Links",
            "value": "[RC](https://rugcheck.xyz/tokens/DGmWTEG4ra4343y3waSuwgiUUoXHUsPzamZTQCPXZ4qX) | [DS](https://dexscreener.com/solana/DGmWTEG4ra4343y3waSuwgiUUoXHUsPzamZTQCPXZ4qX) | [DT](https://www.dextools.io/app/en/solana/pair-explorer/DGmWTEG4ra4343y3waSuwgiUUoXHUsPzamZTQCPXZ4qX) | [SC](https://solscan.io/token/DGmWTEG4ra4343y3waSuwgiUUoXHUsPzamZTQCPXZ4qX) | [Banana](https://t.me/BananaGunSolana_bot?start=snp_agbot_DGmWTEG4ra4343y3waSuwgiUUoXHUsPzamZTQCPXZ4qX) | [gmweb](https://gmgn.ai/sol/token/GV31ZAPw_DGmWTEG4ra4343y3waSuwgiUUoXHUsPzamZTQCPXZ4qX) | [Bloom](https://t.me/BloomSolana_bot?start=ref_DQKMSUUJVL_ca_DGmWTEG4ra4343y3waSuwgiUUoXHUsPzamZTQCPXZ4qX) | [Search X](https://twitter.com/search?q=DGmWTEG4ra4343y3waSuwgiUUoXHUsPzamZTQCPXZ4qX%20OR%20$XmasBoy&src=typed_query&f=live) | [PF](https://www.pump.fun/DGmWTEG4ra4343y3waSuwgiUUoXHUsPzamZTQCPXZ4qX)",
            "inline": False
        }
    ],
    "thumbnail": {
        "url": "https://ipfs.io/ipfs/QmZyPh2ikHNq3t9kEBheKUezn1sp5KNfh3GWRwinfuenVc",
        "proxy_url": "https://images-ext-1.discordapp.net/external/Hqa9pUepDkJR0PHRAxjhBRjiuV49iaXCvs3dfUZaPiU/https/ipfs.io/ipfs/QmZyPh2ikHNq3t9kEBheKUezn1sp5KNfh3GWRwinfuenVc",
        "width": 0,
        "height": 0,
        "flags": 0
    },
    "footer": {
        "text": "Built by Alpha Gardeners • 👀 0",
        "icon_url": "https://alphagardeners.xyz/wp-content/uploads/2021/07/100x100.jpg",
        "proxy_icon_url": "https://images-ext-1.discordapp.net/external/mF-C299-P2cAgCJHXizqCtczsa6B_xM5eP-2MeM0M2U/https/alphagardeners.xyz/wp-content/uploads/2021/07/100x100.jpg"
    },
    "content_scan_version": 1
}]

def EmbifyFields(FIELD):
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

def prittyfy_my_embed(EMBED):
    fields = flet.Column()
    for field in EMBED['fields']:
        fields.controls.append(EmbifyFields(field))

    return flet.Container(
                content=flet.Column(
                    [
                        flet.Markdown(EMBED['title']),
                        flet.Row(
                            [
                                flet.Markdown(EMBED['description']), 
                                flet.ElevatedButton(
                                    "Смотреть на сайте",
                                    bgcolor=flet.colors.WHITE,
                                    color=flet.colors.BLUE_700,
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

def GetFIelds(page: flet.Page):
    b = flet.ListView(spacing=10, expand=True)
    EMBEDS = ParseDiscordChannels(channels_ids=[1241009019494072370], amount=50)
    for embed in EMBEDS:
        b.controls.append(prittyfy_my_embed(embed))
    return b


if __name__ == "__main__":
    def main(page: flet.Page):
        page.add(GetFIelds(page))
    flet.app(main)