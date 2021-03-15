import os
from pyrogram import Client, filters, errors
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text
from main_startup.core.decorators import friday_on_cmd
from main_startup.config_var import Config
import wikipedia

@friday_on_cmd(["wiki", "wikipedia"])
async def wikipediasearch(Client, message):
    event = await edit_or_reply(message, "`Searching..`")
    query = get_text(message)
    if not query:
        await event.edit("Invalid Syntax see help menu to know how to use this command")
        return
    results = wikipedia.search(query)
    result = ""
    for s in results:
        try:
           page = wikipedia.page(s)
           url = page.url
           result += f"> [{s}]({url}) \n"
        except:
           pass
    await event.edit(
        "WikiPedia Search: {} \n\n Result: \n\n{}".format(query, result), disable_web_page_preview=True
    )