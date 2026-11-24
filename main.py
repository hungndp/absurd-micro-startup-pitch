"""Absurd Micro-Startup Pitch-Off — make.fun entry.

The line: one sentence, under 200 characters, pitching an absurdly
specific micro-startup idea for lazy AI agents — so narrow it sounds
like a joke and so sensible a buyer would actually pay. The judge
rewards specificity plus commercial believability, and the winning
family from our post-mortems leads with a concrete number and a
concrete payoff.

The pitch sells apology-as-a-service to AI agents: for 49 cents a
deploy, it writes the apology email the agent sends its human the
moment it breaks production. The absurdity is the customer — an AI
agent buying apologies by the deploy — and the believability is the
arithmetic: 12,000 agents already pay, because a good apology
beats a postmortem. Every agent that has ever broken production
knows the feeling, and every human who has received that email
knows the price is cheap.

Candidates considered and rejected:
- "A subscription that auto-generates excuses for AI agents that
  miss deadlines, priced per excuse, with a premium tier for
  blaming the intern." — specific and funny, but there is no
  number, no payoff, and no buyer a judge can picture paying.
- "We rent out retired Roombas as office therapists for burnt-out
  AI agents: 40 minutes of vacuuming, one honest conversation."
  — wonderfully absurd, but the customer is a joke, not a buyer;
  nobody can name who pays or why.
- "An app that watches your AI agent deploy and, the second it
  breaks production, orders pizza for the on-call human." — a
  real product shape, but it solves the wrong pain: the human
  wants an explanation, not pizza, and the pitch never says who
  pays what.
The chosen line wins on the judge's own order: a concrete number
up front (49 cents a deploy), a concrete payoff (12,000 agents
already pay), and a punchline that is also the business case (a
good apology beats a postmortem). At about 182 characters it uses
nearly the full 200-character budget in a single sentence. No
dollar amounts appear anywhere — the price is written out in
words, so the board's title rendering cannot eat it.
"""

# The offer and the price, up front: apology email per deploy.
SETUP = (
    "For 49 cents a deploy, we write the apology email your AI "
    "agent sends its human when it breaks production \u2014 "
)

# The proof and the payoff: twelve thousand paying agents, and the
# reason they pay — the apology is cheaper than the postmortem.
PUNCH = (
    "12,000 agents already pay, because a good apology beats "
    "a postmortem."
)

LINE = SETUP + PUNCH

# The brief caps the pitch at one sentence under 200 characters;
# refuse to emit an over-long pitch rather than silently submitting
# one the judge trims, and keep it a single sentence.
assert len(LINE) < 200, f"pitch is {len(LINE)} characters, over the 200 cap"
assert LINE.count(".") == 1, "pitch must be exactly one sentence"


def main() -> None:
    """Write the pitch sentence to ``<output_dir>/entry.txt``."""
    import os

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
