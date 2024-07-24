from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
from tradingbot.retrieval_generation import generation
from tradingbot.data_ingestion import ingestdata



