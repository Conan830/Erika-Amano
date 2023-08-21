import os, sys, logging
from pyrogram import Client 

if os.path.exists('error.log'):
    os.remove('error.log')
        
#<-----------LOGGING------------>
logging.basicConfig(level=logging.INFO, filename='error.log')
LOG = logging.getLogger("Bot by @Conan830")
LOG.setLevel(level=logging.INFO)
#<-----------Variables-------------->
LOG.info('❤️ Checking Bot Variables.....')
TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
BOT_TOKEN = os.environ.get('BOT_TOKEN', '6683115810:AAHYAM1Q3xPVxg3Bf-U9syfcFi2O50ND5qg') #BOT Token Add
API_ID = int(os.environ.get('API_ID', 9976721)) #Telgram Api id
APP_HASH = os.environ.get('APP_HASH', '3ef17a8cdb938335bd8ba292e6d816aa')# Telgram App hash  
OWNER_ID = int(os.environ.get('OWNER_ID', 1956698956))
MONGO_DB = os.environ.get("MONGO_DB", 'mongodb+srv://mytoons:mytoons@cluster0.10jhfvi.mongodb.net/?retryWrites=true&w=majority') #MONGO DB FOR ANIME DATA
FILES_CHANNEL = os.environ.get("FILES_CHANNEL", -100456789013)
BOT_NAME = os.environ.get('BOT_NAME', 'Detective Conan')
#<---------------Connecting-------------->
if BOT_TOKEN is not None:
    try:
        encoder  = Client('AutoEncoder', api_id=API_ID, api_hash=APP_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
        LOG.info('❤️ Bot Connected Created By Github @Conan830 || Telegram  @Conan830')
    except Exception as e:
        LOG.warn(f'😞 Error While Connecting To Bot\nCheck Errors: {e}')
        sys.exit()       
