# ---------------------------------------------------
# File Name: start.py
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

from pyrogram import filters
from devgagan import app
from config import OWNER_ID
from devgagan.core.func import subscribe
import asyncio
from devgagan.core.func import *
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.raw.functions.bots import SetBotInfo
from pyrogram.raw.types import InputUserSelf

from pyrogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
 
@app.on_message(filters.command("set"))
async def set(_, message):
    if message.from_user.id not in OWNER_ID:
        await message.reply("Tu n'es pas autorisé à utilisé cette commande.")
        return
     
    await app.set_bot_commands([
        BotCommand("start", "🚀 Start the bot"),
        BotCommand("batch", "🫠 Extract in bulk"),
        BotCommand("login", "🔑 Get into the bot"),
        BotCommand("logout", "🚪 Get out of the bot"),
        BotCommand("token", "🎲 Get 3 hours free access"),
        BotCommand("adl", "👻 Download audio from 30+ sites"),
        BotCommand("dl", "💀 Download videos from 30+ sites"),
        BotCommand("freez", "🧊 Remove all expired user"),
        BotCommand("pay", "₹ Pay now to get subscription"),
        BotCommand("status", "⟳ Refresh Payment status"),
        BotCommand("transfer", "💘 Gift premium to others"),
        BotCommand("myplan", "⌛ Get your plan details"),
        BotCommand("add", "➕ Add user to premium"),
        BotCommand("rem", "➖ Remove from premium"),
        BotCommand("session", "🧵 Generate Pyrogramv2 session"),
        BotCommand("settings", "⚙️ Personalize things"),
        BotCommand("stats", "📊 Get stats of the bot"),
        BotCommand("plan", "🗓️ Check our premium plans"),
        BotCommand("terms", "🥺 Terms and conditions"),
        BotCommand("speedtest", "🚅 Speed of server"),
        BotCommand("lock", "🔒 Protect channel from extraction"),
        BotCommand("gcast", "⚡ Broadcast message to bot users"),
        BotCommand("help", "❓ If you're a noob, still!"),
        BotCommand("cancel", "🚫 Cancel batch process")
    ])
 
    await message.reply("✅ Commande configuré avec succès!")
 
 
 
 
help_pages = [
    (
        "📝 **Aperçu des commandes du bot (1/2)**:\n\n"
        "1. **/add userID**\n"
        "> Ajouter un utilisateur au premium (Propriétaire uniquement)\n\n"
        "2. **/rem userID**\n"
        "> Retirer un utilisateur du premium (Propriétaire uniquement)\n\n"
        "3. **/transfer userID**\n"
        "> Transférer le premium à votre bien-aimé, principal objectif pour les revendeurs (Membres premium uniquement)\n\n"
        "4. **/get**\n"
        "> Obtenir tous les identifiants d'utilisateur (Propriétaire uniquement)\n\n"
        "5. **/lock**\n"
        "> Verrouiller un canal contre l'extraction (Propriétaire uniquement)\n\n"
        "6. **/dl link**\n"
        "> Télécharger des vidéos (Non disponible dans v3 si vous l'utilisez)\n\n"
        "7. **/adl link**\n"
        "> Télécharger de l'audio (Non disponible dans v3 si vous l'utilisez)\n\n"
        "8. **/login**\n"
        "> Se connecter au bot pour accéder au canal privé\n\n"
        "9. **/batch**\n"
        "> Extraction en masse pour les publications (Après connexion)\n\n"
    ),
    (
        "📝 **Aperçu des commandes du bot (2/2)**:\n\n"
        "10. **/logout**\n"
        "> Se déconnecter du bot\n\n"
        "11. **/stats**\n"
        "> Obtenir des statistiques sur le bot\n\n"
        "12. **/plan**\n"
        "> Vérifier les plans premium\n\n"
        "13. **/speedtest**\n"
        "> Tester la vitesse du serveur (non disponible dans v3)\n\n"
        "14. **/terms**\n"
        "> Termes et conditions\n\n"
        "15. **/cancel**\n"
        "> Annuler le processus de lot en cours\n\n"
        "16. **/myplan**\n"
        "> Obtenir des détails sur vos plans\n\n"
        "17. **/session**\n"
        "> Générer une session Pyrogram V2\n\n"
        "18. **/settings**\n"
        "> 1. SETCHATID : Pour télécharger directement dans le canal ou le groupe ou le DM de l'utilisateur, utilisez-le avec -100[chatID]\n"
        "> 2. SETRENAME : Pour ajouter une étiquette de renommage personnalisée ou un nom d'utilisateur de vos canaux\n"
        "> 3. CAPTION : Pour ajouter une légende personnalisée\n"
        "> 4. REPLACEWORDS : Peut être utilisé pour les mots dans l'ensemble supprimé via REMOVE WORDS\n"
        "> 5. RESET : Pour rétablir les paramètres par défaut  \n\n"
        "> Vous pouvez définir des THUMBNAILS PERSONNALISÉS, un FILIGRANE PDF, un FILIGRANE VIDÉO, une connexion basée sur la SESSION, etc., depuis les paramètres.\n\n"
        "**__💝‣ Propulsé Par: [@BotZFlix]__**"
    )
]
 
 
async def send_or_edit_help_page(_, message, page_number):
    if page_number < 0 or page_number >= len(help_pages):
        return
 
     
    prev_button = InlineKeyboardButton("◀️ Précédent", callback_data=f"help_prev_{page_number}")
    next_button = InlineKeyboardButton("Suivant ▶️", callback_data=f"help_next_{page_number}")
 
     
    buttons = []
    if page_number > 0:
        buttons.append(prev_button)
    if page_number < len(help_pages) - 1:
        buttons.append(next_button)
 
     
    keyboard = InlineKeyboardMarkup([buttons])
 
     
    await message.delete()
 
     
    await message.reply(
        help_pages[page_number],
        reply_markup=keyboard
    )
 
 
@app.on_message(filters.command("help"))
async def help(client, message):
    join = await subscribe(client, message)
    if join == 1:
        return
 
     
    await send_or_edit_help_page(client, message, 0)
 
 
@app.on_callback_query(filters.regex(r"help_(prev|next)_(\d+)"))
async def on_help_navigation(client, callback_query):
    action, page_number = callback_query.data.split("_")[1], int(callback_query.data.split("_")[2])
 
    if action == "prev":
        page_number -= 1
    elif action == "next":
        page_number += 1
 
     
    await send_or_edit_help_page(client, callback_query.message, page_number)
 
     
    await callback_query.answer()
 
 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 
@app.on_message(filters.command("terms") & filters.private)
async def terms(client, message):
    terms_text = (
        "> 📜 **Termes et Conditions** 📜\n\n"
        "✨  Nous ne sommes pas responsables des actes des utilisateurs et nous ne promouvons pas de contenu protégé par des droits d'auteur. Si un utilisateur s'engage dans de telles activités, il en assume l'entière responsabilité.\n"
        "✨  Lors d'un achat, nous ne garantissons pas la disponibilité, les temps d'arrêt ou la validité du plan. __L'autorisation et l'interdiction des utilisateurs relèvent de notre discrétion ; nous nous réservons le droit d'autoriser ou d'interdire des utilisateurs à tout moment.__\n"
        "✨  Le paiement effectué ne __**garantit pas** l'autorisation pour la commande /batch. Toutes les décisions concernant l'autorisation sont prises à notre discrétion et selon notre humeur__.\n"
    )
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📋 Voir le plan", callback_data="see_plan")],
            [InlineKeyboardButton("💬 Contactez moi", url="https://t.me/Kingcey")],
        ]
    )
    await message.reply_text(terms_text, reply_markup=buttons)
 
 
@app.on_message(filters.command("plan") & filters.private)
async def plan(client, message):
    plan_text = (
        "> 💰 **Prix Premium**:\n\n À partir de **2$** ou **1200**, acceptés via **N'importe quel mode de paiement** (des termes et conditions s'appliquent).\n"
        "📥 **Limite de téléchargement :** Les utilisateurs peuvent télécharger jusqu'à **100 000 fichiers** dans une seule commande batch.\n"
        "🛑 **Modes Batch :** Vous aurez accès à deux modes : **/bulk** et **/batch**.\n"
        "    - Il est conseillé aux utilisateurs d'attendre que le processus se termine automatiquement avant de procéder à tout téléchargement ou upload.\n\n"
        "📜 **Termes et Conditions :** Pour plus de détails et les termes et conditions complets, veuillez envoyer la commande **/terms**.\n"
    )
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📜 Voir les Terms", callback_data="see_terms")],
            [InlineKeyboardButton("💬 Contact moi", url="https://t.me/Kingcey")],
        ]
    )
    await message.reply_text(plan_text, reply_markup=buttons)
 
 
@app.on_callback_query(filters.regex("see_plan"))
async def see_plan(client, callback_query):
    plan_text = (
        "> 💰 **Prix Premium**:\n\n À partir de **2$** ou **1200**, acceptés via **N'importe quel mode de paiement** (des termes et conditions s'appliquent).\n"
        "📥 **Limite de téléchargement :** Les utilisateurs peuvent télécharger jusqu'à **100 000 fichiers** dans une seule commande batch.\n"
        "🛑 **Modes Batch :** Vous aurez accès à deux modes : **/bulk** et **/batch**.\n"
        "    - Il est conseillé aux utilisateurs d'attendre que le processus se termine automatiquement avant de procéder à tout téléchargement ou upload.\n\n"
        "📜 **Termes et Conditions :** Pour plus de détails et les termes et conditions complets, veuillez envoyer la commande **/terms**.👇\n"
    )
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📜 Voir les Terms", callback_data="see_terms")],
            [InlineKeyboardButton("💬 Contact", url="https://t.me/Kingcey")],
        ]
    )
    await callback_query.message.edit_text(plan_text, reply_markup=buttons)
 
 
@app.on_callback_query(filters.regex("see_terms"))
async def see_terms(client, callback_query):
    terms_text = (
        "> 📜 **Conditions Générales** 📜\n\n"
        "✨ Nous ne sommes pas responsables des actions des utilisateurs et nous ne promouvons pas de contenu protégé par des droits d'auteur. Si un utilisateur s'engage dans de telles activités, cela relève uniquement de sa responsabilité.\n"
        "✨ Lors de l'achat, nous ne garantissons pas le temps de disponibilité, __le temps d'arrêt ou la validité du plan. L'autorisation et l'interdiction des utilisateurs sont à notre discrétion ; nous nous réservons le droit d'interdire ou d'autoriser des utilisateurs à tout moment.__\n"
        "✨ Le paiement que vous effectuez **__ne garantit pas__** l'autorisation pour la commande /batch. Toutes les décisions concernant l'autorisation sont prises à notre discrétion et selon notre humeur.\n"
    )
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📋 Voir les Plans", callback_data="see_plan")],
            [InlineKeyboardButton("💬 Contact", url="https://t.me/kingcey")],
        ]
    )
    await callback_query.message.edit_text(terms_text, reply_markup=buttons)
 
 
