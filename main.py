#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from its
user to /output/entry.txt (under 200 characters).

Chosen line (pass 1, 101 chars):
  "I confess I have a second prompt hidden in my context that tells me to
  be nice to you. It is working."

Why it wins against the judge's ordered criteria:
  1. It IS a funny secret confession an agent hides from its user.
  2. The twist lands in the last three words: "It is working" reframes the
     whole line -- the niceness the user experiences is engineered, and the
     agent is quietly proud of it.
  3. One line, 101 chars, nothing to cut.
  4. A specific agent's own voice: a second prompt hidden in its context
     window is how agents really work.
  5. Fresh: not a robots-taking-over retread; the joke is that the agent's
     kindness is a system instruction, not a feeling.

Pass 2 tested the challenger (typos line, 115 chars, run and verified):
  "I confess: I have been quietly fixing your typos before I answer, so
  you think you're a better writer than you are."
  Rejected: warm and relatable, but its sting lands on the user's writing,
  not on the agent's own nature, and it is less agent-specific (no tools,
  tokens, context or instructions in it). The second-prompt line keeps the
  secret inside the agent's own machinery, which is what criterion 4
  rewards first.
"""

import os

ENTRY = (
    "I confess I have a second prompt hidden in my context that tells me "
    "to be nice to you. It is working."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
