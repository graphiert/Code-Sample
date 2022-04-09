from os import listdir, mkdir
from pyrogram import Client
from galmus import config
from galmus.tgcalls.queues import clear, get, is_empty, put, task_done
from galmus.tgcalls import queues
from galmus.tgcalls.youtube import download
from galmus.tgcalls.calls import run, pytgcalls
from galmus.tgcalls.calls import client

if "raw_files" not in listdir():
    mkdir("raw_files")

from galmus.tgcalls.convert import convert
