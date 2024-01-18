import json
import os
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import List
from uuid import uuid4

import openai
import streamlit as st

from utils.helpers import date_id
from utils.messages import (
    REINFORCEMENT_SYSTEM_MSG,
    INITIAL_SYSTEM_MSG,
    INTROS,
    CARDS_REINFORCEMENT_SYSTEM_MSG,
)
from utils.tarot import TAROT_DECK