# AI-Driven Snarky Comments Plan

This document describes a possible approach to integrate the OpenAI API with WindowGotchi so the pet can make cute, slightly snarky comments based on what the user is doing on their screen.

## Overview
1. Periodically capture lightweight screenshots of the user's screen.
2. Send the image or extracted text to an OpenAI model to interpret the current activity.
3. Generate a short comment in the pet's voice that is playful and mildly sarcastic.
4. Display the comment in a notification balloon or in the UI next to the pet.

## Steps
- **Screenshot capture**: Use a cross‑platform library such as `pyautogui` or `Pillow` to take screenshots every few minutes. Images should be downscaled or otherwise processed to avoid privacy issues.
- **Context extraction**: Optionally run OCR (e.g. with `pytesseract`) to extract visible text. This text, or a low‑resolution version of the screenshot, can be provided as context to the OpenAI API.
- **Prompt design**: Craft prompts that instruct the model to respond as a cute pet that makes snarky but friendly remarks. The prompt might include example responses to ensure a consistent style.
- **Rate limiting**: Cache recent comments and avoid sending screenshots too often to respect API usage limits. A sample interval might be every 15 minutes or when significant screen changes are detected.
- **Displaying comments**: Use the existing notification manager or add a small speech‑bubble widget to surface the generated text to the user.

## Considerations
- **Privacy**: Offer the user clear opt‑in. Screenshots should be processed locally whenever possible and kept temporarily.
- **API costs**: Keep requests small by limiting screenshot size and prompt length. Batch requests when the user is idle.
- **Fallback behavior**: If the API is unreachable, the pet can fall back to prewritten generic comments.

This plan can evolve alongside the rest of the project to bring personality to WindowGotchi.
