FROM python:3-onbuild
CMD ["python", "./bible_bot.py"]
ENV PATH_TO_ICONS="./images/"
