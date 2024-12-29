import os
from telegram import Update, ChatPermissions, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
import logging

# Atur level logging global
logging.basicConfig(level=logging.WARNING)

# Matikan logger bawaan HTTP
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("telegram.ext._application").setLevel(logging.WARNING)
logging.getLogger("telegram._vendor.ptb_urllib3.urllib3.connectionpool").setLevel(logging.CRITICAL)

# Muat environment dari file token.env
load_dotenv("/token.env")

# Ambil token dari environment
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("TOKEN tidak ditemukan. Pastikan Anda telah mengatur environment variable TOKEN.")

# Logging untuk debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Dictionary untuk mencatat peringatan
warnings = {}

# Fungsi /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Owner", url="https://t.me/edikurbot"),
            InlineKeyboardButton("Support", url="https://t.me/s905x4"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Selamat datang di Bot Anti Mute dan Peringatan Username!\n\n"
        "Bot ini memiliki beberapa fitur:\n"
        "- Memantau anggota yang tidak memiliki username.\n"
        "- Memberikan hingga 3 peringatan sebelum mengeluarkan anggota tanpa username.\n"
        "Gunakan perintah /help untuk melihat daftar perintah.\n\n"
        "Klik tombol di bawah untuk informasi lebih lanjut.",
        reply_markup=reply_markup
    )

# Fungsi /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Menampilkan informasi tentang bot\n"
        "/help - Menampilkan pesan bantuan\n"
        "/check_members - Memeriksa anggota tanpa username\n"
        "Bot juga secara otomatis memantau anggota tanpa username."
    )

# Fungsi untuk memantau anggota tanpa username
async def monitor_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    username = update.effective_user.username
    first_name = update.effective_user.first_name

    if not username:  # Jika username belum diset
        if user_id not in warnings:
            warnings[user_id] = 1

            # Kirim peringatan dengan tombol
            button = InlineKeyboardButton("Atur Username", url="https://t.me/settings/username")
            reply_markup = InlineKeyboardMarkup([[button]])

            await update.message.reply_text(
                f"Hai {first_name}, Anda belum memiliki username. "
                "Harap atur username Anda segera! Ini adalah peringatan pertama atau anda akan dikick.",
                reply_markup=reply_markup
            )
        elif warnings[user_id] < 3:
            warnings[user_id] += 1
            await update.message.reply_text(
                f"{first_name}, Anda belum memiliki username. "
                f"Ini adalah peringatan ke-{warnings[user_id]}."
            )
        else:  # Kick jika peringatan sudah 3 kali
            try:
                await context.bot.ban_chat_member(chat_id, user_id)
                await update.message.reply_text(
                    f"{first_name} telah dikeluarkan dari grup karena tidak memiliki username."
                )
                del warnings[user_id]
            except Exception as e:
                logger.error(f"Gagal mengeluarkan {first_name}: {e}")
                await update.message.reply_text(
                    f"Gagal mengeluarkan {first_name}: {e}"
                )
    else:  # Jika username sudah diset
        if user_id in warnings:
            del warnings[user_id]
            await update.message.reply_text(
                f"Terima kasih {first_name}, Anda telah mengatur username!"
            )

# Fungsi untuk memeriksa anggota tanpa username (hanya member yang aktif)
async def check_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Fitur ini hanya memantau anggota yang aktif berinteraksi di grup. "
        "Anggota yang belum memiliki username akan diberi peringatan."
    )

# Fungsi menambahkan perintah di bot
async def set_commands(application):
    commands = [
        BotCommand("start", "Menampilkan informasi tentang bot"),
        BotCommand("help", "Menampilkan pesan bantuan"),
        BotCommand("check_members", "Memeriksa anggota tanpa username"),
    ]
    await application.bot.set_my_commands(commands)
    
# Fungsi utama untuk menjalankan bot
def main():
    # Membuat aplikasi bot
    application = Application.builder().token(TOKEN).build()

    # Menambahkan handler untuk perintah dan pemantauan pesan
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("check_members", check_members))
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, monitor_members))

    # Menjalankan bot
    application.run_polling()

if __name__ == "__main__":
    main()
