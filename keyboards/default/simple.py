from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppData, WebAppInfo

home = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="Button 1"
            )
        ]
    ],
    resize_keyboard=True
)

admin_panel_keys = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(
                text="📩 Xabar yuborish"
            )
        ]
    ]
)

uzbekistan_regions_uz = [
    "Toshkent",
    "Andijon",
    "Buxoro",
    "Farg'ona",
    "Jizzax",
    "Namangan",
    "Navoiy",
    "Qashqadaryo",
    "Samarqand",
    "Sirdaryo",
    "Surxondaryo",
    "Xorazm",
    "Qoraqalpog'iston Respublikasi"
]


regions = [[ KeyboardButton(i) ] for i in uzbekistan_regions_uz]

select_region = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard= regions
)