
# --- injected by submission notebook ---

import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / "pj" / "mind-arc" / "src"))

from mind_arc.bridge import MindArcAgent

# --- end injection ---


from typing import Type, cast
from dotenv import load_dotenv
from .agent import Agent, Playback
from .swarm import Swarm
from .templates.random_agent import Random

load_dotenv()

AVAILABLE_AGENTS: dict[str, Type[Agent]] = {
    "random": Random,
    "mind_arc_agent": MindArcAgent,
}
