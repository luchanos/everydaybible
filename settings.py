from envparse import env

TOKEN = env.str('TOKEN', default='X-TOKEN')
PATH_TO_ICONS = env.str('PATH_TO_ICONS', default='./images/')
STRING_LIMIT = env.str('STRING_LIMIT', default=100)
USE_PROXY = env.bool('USE_PROXY', default=False)
PROXY = env.str('PROXY', default='')
