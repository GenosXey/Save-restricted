 
# ---------------------------------------------------
# File Name: shrink.py
# Description: A Pyrogram bot for downloading files from Telegram channels or groups 
#              and uploading them back to Telegram.
# Author: Gagan
# GitHub: https://github.com/devgaganin/
# Telegram: https://t.me/team_spy_pro
# YouTube: https://youtube.com/@dev_gagan
# Created: 2025-01-11
# Last Modified: 2025-01-11
# Version: 2.0.5
# License: MIT License
# ---------------------------------------------------

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
import requests
import string
import aiohttp
from devgagan import app
from devgagan.core.func import *
from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB, WEBSITE_URL, AD_API, LOG_GROUP  
 
 
tclient = AsyncIOMotorClient(MONGO_DB)
tdb = tclient["telegram_bot"]
token = tdb["tokens"]
 
 
async def create_ttl_index():
    await token.create_index("expires_at", expireAfterSeconds=0)
 
 
 
Param = {}
 
 
async def generate_random_param(length=8):
    """Generate a random parameter."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
 
 
async def get_shortened_url(deep_link):
    api_url = f"https://{WEBSITE_URL}/api?api={AD_API}&url={deep_link}"
 
     
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                data = await response.json()   
                if data.get("status") == "success":
                    return data.get("shortenedUrl")
    return None
 
 
async def is_user_verified(user_id):
    """Check if a user has an active session."""
    session = await token.find_one({"user_id": user_id})
    return session is not None
 
 
@app.on_message(filters.command("start"))
async def token_handler(client, message):
    """Handle the /token command."""
    join = await subscribe(client, message)
    if join == 1:
        return
    chat_id = "save_restricted_content_bots"
    msg = await app.get_messages(chat_id, 796)
    user_id = message.chat.id
    if len(message.command) <= 1:
        image_url = "https://iili.io/3Gu0PIa.md.jpg"
        join_button = InlineKeyboardButton("Rejoins Mon Canal", url="https://t.me/BotZFlix")
        premium = InlineKeyboardButton("Obtenir Premium", url="https://t.me/Kingcey")   
        keyboard = InlineKeyboardMarkup([
            [join_button],   
            [premium]    
        ])
         
        await message.reply_photo(
            msg.photo.file_id,
            caption=(
                "Salut 👋 dārin. je suis Nayuta...?\n\n"
                "✳️ Je peux enregistrer des publications de chaînes ou de groupes dont le transfert est désactivé. Je peux télécharger des vidéos et des fichiers audio depuis YouTube, Instagram, etc..\n"
                "✳️ mais pour les anaux privée, il faudra que je sois admin au canal ou que je sois connecté à votre compte.."
            ),
            reply_markup=keyboard
        )
        return  
 
    param = message.command[1] if len(message.command) > 1 else None
    freecheck = await chk_user(message, user_id)
    if freecheck != 1:
        await message.reply("Vous êtes un pseudo-KINGCEY pas de token requis 😉")
        return
 
     
    if param:
        if user_id in Param and Param[user_id] == param:
             
            await token.insert_one({
                "user_id": user_id,
                "param": param,
                "created_at": datetime.utcnow(),
                "expires_at": datetime.utcnow() + timedelta(hours=3),
            })
            del Param[user_id]   
            await message.reply("✅ Vous avez été vérifié avec succès ! Profitez de votre session pendant les 3 prochaines heures..")
            return
        else:
            await message.reply("❌ lien de vérification invalide ou expiré. Veuillez générer un nouveau jeton.")
            return
 
@app.on_message(filters.command("token"))
async def smart_handler(client, message):
    user_id = message.chat.id
     
    freecheck = await chk_user(message, user_id)
    if freecheck != 1:
        await message.reply("Vous êtes un pseudo-KINGCEY pas de token requis 😉")
        return
    if await is_user_verified(user_id):
        await message.reply("✅ Votre session gratuite est déjà active. Profitez-en !")
    else:
         
        param = await generate_random_param()
        Param[user_id] = param   
 
         
        deep_link = f"https://t.me/{client.me.username}?start={param}"
 
         
        shortened_url = await get_shortened_url(deep_link)
        if not shortened_url:
            await message.reply("❌ Échec de la génération du lien de jeton. Veuillez réessayer")
            return
 
         
        button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Verification du token...", url=shortened_url)]]
        )
        await message.reply("Cliquez sur le bouton ci-dessous pour vérifier votre jeton d'accès gratuit: \n\n> Qu'est-ce que vous obtiendrez ? \n1. Pas de limite de temps jusqu'à 3 heures  \n2. La limite de commande par lot sera FreeLimit + 20 \n3. Toutes les fonctions débloquées", reply_markup=button)
 
