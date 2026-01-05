import csv
import logging
import time
import hashlib
import json
import os
from typing import Dict

from app.llm.llm_inference import infer
from app.prompts.system_prompt import system_prompt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

INPUT_FILE = "app/data/evals_conversations.csv"
OUTPUT_FILE = "app/data/evaluation_results.csv"
CACHE_FILE = "app/data/eval_cache.json"

START_FROM = 938
END_AT = 1000

REQUESTS_PER_MINUTE = 20
SLEEP_SECONDS = 60 / REQUESTS_PER_MINUTE
MAX_RETRIES = 3


def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_cache() -> Dict[str, dict]:
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_cache(cache: Dict[str, dict]):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


def evaluate_conversations():
    logger.info("Starting evaluation job")

    cache = load_cache()
    logger.info(f"Loaded cache with {len(cache)} entries")

    with open(INPUT_FILE, "r") as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)

    file_exists = os.path.exists(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", newline="") as outfile:
        fieldnames = [
            "conversation_id",
            "conversation_hash",
            "predicted_primary",
            "predicted_secondary",
            "predicted_tertiary",
            "confidence",
            "latency_ms",
            "input_tokens",
            "output_tokens",
        ]

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        for i, row in enumerate(rows[START_FROM - 1 : END_AT], start=START_FROM):
            conversation = row["conversation"]
            conv_id = row["conversation_id"]
            conv_hash = hash_text(conversation)

            if conv_hash in cache:
                logger.info(f"[SKIP] Conversation {conv_id} already labeled")
                cached = cache[conv_hash]

                writer.writerow({
                    "conversation_id": conv_id,
                    "conversation_hash": conv_hash,
                    **cached
                })
                continue

            logger.info(f"[PROCESS] Conversation {conv_id}")

            retries = 0
            while retries < MAX_RETRIES:
                try:
                    start_time = time.time()
                    result, usage = infer(system_prompt, conversation)
                    latency = int((time.time() - start_time) * 1000)

                    record = {
                        "conversation_id": conv_id,
                        "predicted_primary": result.primary_topic,
                        "predicted_secondary": result.secondary_topic,
                        "predicted_tertiary": result.tertiary_topic,
                        "confidence": result.confidence,
                        "latency_ms": latency,
                        "input_tokens": usage.get("prompt_tokens", 0),
                        "output_tokens": usage.get("completion_tokens", 0),
                    }

                    cache[conv_hash] = record
                    save_cache(cache)

                    writer.writerow({
                        "conversation_id": conv_id,
                        "conversation_hash": conv_hash,
                        **record
                    })

                    logger.info(
                        f"✓ {result.primary_topic} → {result.secondary_topic} → "
                        f"{result.tertiary_topic} ({latency}ms)"
                    )

                    time.sleep(SLEEP_SECONDS)
                    break

                except Exception as e:
                    retries += 1
                    logger.warning(
                        f"[RETRY {retries}/{MAX_RETRIES}] Conversation {conv_id} failed: {e}"
                    )
                    time.sleep(30)

            else:
                logger.error(f"[FAILED] Conversation {conv_id} permanently failed")

                writer.writerow({
                    "conversation_id": conv_id,
                    "conversation_hash": conv_hash,
                    "predicted_primary": "ERROR",
                    "predicted_secondary": "ERROR",
                    "predicted_tertiary": "ERROR",
                    "confidence": 0.0,
                    "latency_ms": 0,
                    "input_tokens": 0,
                    "output_tokens": 0,
                })


if __name__ == "__main__":
    evaluate_conversations()
