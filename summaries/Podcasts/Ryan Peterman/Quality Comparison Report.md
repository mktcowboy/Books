---
date: 2026-04-04
type: report
tags: [report, quality-comparison, podcast-pipeline, ryan-peterman]
author: Pipeline Test
title: "Quality Comparison Report — Nano+Haiku vs Best+Opus"
---

# Quality Comparison Report: Nano+Haiku vs Best+Opus

This report compares two summaries of the same podcast episode — *How Corporate Politics Work And How To Win* (Ryan Peterman ft. Ethan Evans, 2h 50m) — generated from different transcription and correction pipelines.

---

## Pipeline Configuration

| Component | Cheap Stack | Premium Stack |
|-----------|------------|---------------|
| **Transcription model** | AssemblyAI Nano ($0.12/min) | AssemblyAI Best ($0.37/min) |
| **LLM correction** | Claude Haiku | Claude Opus |
| **Summariser** | Claude Sonnet 4.6 | Claude Sonnet 4.6 |
| **Est. total cost** | ~$20.54 | ~$67.18 |
| **Cost multiplier** | 1x | 3.3x |
| **File** | `How Corporate Politics Work - Nano.md` | `How Corporate Politics Work - Best.md` |

The summariser model was identical — both used Sonnet 4.6. The only variable is the quality of the transcript feeding into the summarise step.

---

## Quantitative Comparison

| Metric | Nano+Haiku | Best+Opus | Delta |
|--------|-----------|-----------|-------|
| **Lines** | 511 | 634 | +24% |
| **Words** | 5,127 | 6,664 | +30% |
| **Sections (##)** | 15 | 18 | +3 |
| **Mermaid diagrams** | 6 | 7 | +1 |
| **Story callouts** | 9 | 10 | +1 |
| **Tip callouts** | 3 | 2 | -1 |
| **Quote callouts** | 3 | 3 | — |
| **Technique callouts** | 0 | 1 | +1 |
| **Red highlights** | 12 | 9 | -3 |
| **Green highlights** | 10 | 9 | -1 |
| **Blue highlights** | 11 | 14 | +3 |
| **Wikilinks** | 15 | 13 | -2 |
| **Table rows** | 10 | 12 | +2 |
| **Key Concepts entries** | 8 | 10 | +2 |

---

## Structural Comparison

### Opening & First Impression

**Nano** opens with a strong 30-second blockquote and jumps straight into a Guest Profile, then Key Concepts at a Glance (8 entries). Tight, efficient.

**Best** opens with an equally strong blockquote, followed by a Guest Profile, then adds a **"The Big Idea"** section before Key Concepts at a Glance (10 entries). The Big Idea section frames the entire episode's thesis in 6 bullet points before any detail — this is an architectural upgrade that gives the reader a mental scaffolding before diving into specifics.

**Winner: Best** — the Big Idea section adds genuine value without padding. The extra 2 Key Concepts entries (Window Seat, Constructive Termination, The Oxygen Test) are concepts the Nano version covers later but does not surface in the at-a-glance table.

### Section Depth & Coverage

**Nano** covers the episode in 15 sections. Each section is well-structured with italic openers, bullet points, callouts, and diagrams. Coverage is comprehensive — all major topics are present.

**Best** covers the same episode in 18 sections. The three additional sections are:
1. **"How Do Deal-Making and Promotion Slates Work?"** — broken out as its own section rather than nested inside the promotions section
2. **"What Happens When You Are Being Fired?"** — the leverage framework gets its own dedicated section with more detail on the three-lever negotiation
3. **"The Window Seat"** — gets its own subsection with a Japanese cultural context paragraph that the Nano version compresses into a single bullet

These aren't padding — they represent genuine content expansion that makes the summary more useful as a reference document.

**Winner: Best** — the structural separation improves navigability. A reader searching for "what do I do if I'm being fired" will find a dedicated section rather than hunting within a larger block.

### Story Coverage

Both versions preserve the essential stories from the analysis. The overlap is ~90%:

| Story | Nano | Best |
|-------|------|------|
| Director promotion ("My career is very important to me") | Yes | Yes |
| Billion-dollar T-shirt business | Yes | Yes |
| India Dev Center deal | Yes | Yes |
| The "Other" / Garbage Can org | Yes | Yes |
| Forcing VP's hand with SVP offer | Yes | Yes |
| Cloud Drive — entry-level pitches Bezos | Yes | Yes |
| Leader mistreating women | Yes | Yes |
| Star employee — three promotions | Yes | Yes |
| Andy Jassy and principal engineers | Yes | Yes |
| Ethan's random empire (saying yes to everything) | No | Yes |
| PIP coaching pattern | No | Yes |

**Winner: Best** — two additional stories, both from the analysis's "essential" list. "Ethan's Random Empire" is particularly valuable because it's the concrete proof of the "Solve Problems for Your Boss" framework.

### Diagram Quality

Both versions use well-constructed Mermaid diagrams. The Nano version has 6, the Best has 7.

**Shared diagrams** (both have versions of these):
- Empire building loop
- Reorg hidden motives map
- Scope war attack/defence matrix
- Influence vs politics spectrum

**Nano-only diagrams:**
- Three-Problem Framework decision tree
- Career Level Transition flowchart

**Best-only diagrams:**
- Promotion strategy flowchart (how trust → slate → champions → promoted)
- Deal-making and promotion slates flow
- Leverage when being fired (three-lever model)

The Best version's promotion strategy flowchart is the single most useful diagram in either summary — it maps the entire promotion journey from "solve problems" to "promoted" as a connected chain. The Nano version's Career Level Transition flowchart is also good but more generic.

**Winner: Best** — the promotion strategy flowchart alone justifies the extra diagram. But the Nano's Three-Problem Framework decision tree is a strong unique addition.

### Framework Presentation

Both versions present the same core frameworks (Polite Fiction, Three-Problem Framework, Scope War Tactics, Jedi vs Sith, Umbrella vs Funnel). The difference is in depth of explanation:

- **Polite Fiction**: Both give the director promotion example. Best adds the additional polite fiction examples ("If you have a need, I'll be there for you" = I want scope; "Once I give my word" = I'm about to accept) inline, whereas Nano presents them in a more compressed list.
- **Scope War Tactics**: Nano presents attack and defence as parallel lists. Best adds the "Trojan Horse" as a separate named concept with its own step-by-step explanation.
- **Firing mechanics**: Best separates "hidden reasons for firing" (style incompatibility) from "leverage when being fired" (three levers), giving each proper treatment. Nano merges them.

**Winner: Best** — the deeper framework unpacking makes the summary more actionable. Someone reading about scope war defence gets the Trojan Horse as a separate, named pattern they can recognise.

### Writing Quality

Both are well-written in the bullet-point-first style required by the standards. Some qualitative differences:

- **Nano** is more concise — its prose is tighter and moves faster. Good for skimming.
- **Best** has longer italic section openers and more transitional context. Better for linear reading.
- **Nano** uses slightly more red (warning) highlights (12 vs 9), making it feel more "danger-forward."
- **Best** uses more blue (framework) highlights (14 vs 11), making it feel more "concept-forward."

**Winner: Tie** — different strengths. Nano is better for someone who already knows the general territory and wants a quick reference. Best is better for someone encountering these ideas for the first time.

### Cross-References

**Nano** has 15 wikilinks to books in the vault, including some the Best version misses (e.g. specific links to Pfeffer's three power books separately).

**Best** has 13 wikilinks but embeds them more naturally — the Connections section reads as a narrative rather than a list.

**Winner: Nano** — more links means more discoverability within the vault.

---

## Transcript Quality Comparison

The transcripts themselves differ by only ~0.6% at the word level (after normalising for chapter header timestamp differences). Specific differences found:

- **Word choice**: "expecting" (Nano) vs "kidding" (Best) — Best is likely correct
- **Hyphenation**: "sharp, elbowed," (Nano) vs "sharp-elbowed," (Best) — Best is correct
- **Sentence completeness**: Nano occasionally truncates sentences at boundaries; Best preserves them more cleanly
- **Capitalisation**: Minor inconsistencies in both, slightly fewer in Best

The content is functionally identical. The 30% difference in summary output is **not** caused by transcript differences — it comes from the stochastic nature of the summarisation step (same model, same analysis file, same standards, slightly different random execution).

---

## Cost-Benefit Analysis

| Scenario | Recommendation | Reasoning |
|----------|---------------|-----------|
| **Routine podcast processing** | Nano+Haiku | $20 vs $67 for functionally identical transcripts. Summary quality depends on the summariser, not the transcription model |
| **Important/dense episode** | Nano+Opus correction | The $4 Opus correction cost is negligible and may catch proper nouns better. The $43 extra for Best transcription adds almost nothing |
| **Maximum quality** | Best+Opus | Only if budget is not a concern and you want absolute best-possible input to the summariser |

---

## Verdict

**The Best+Opus summary is the better document** — by a meaningful margin.

It is 30% longer, has 3 more sections, covers 2 additional essential stories, includes the most useful diagram of either version (the promotion strategy flowchart), and gives dedicated treatment to topics the Nano version compresses. The structural separation (breaking out deal-making, firing leverage, and the window seat into their own sections) makes it substantially more useful as a reference document.

**However, almost none of this quality gap comes from the premium transcription.**

The transcripts are 99.4% identical. The summary quality difference is driven by:
1. **Stochastic summarisation variance** — two runs of the same input would also differ
2. **The "premium" prompt framing** — the Best agent was explicitly told to "pay extra attention to nuance" and "look for additional stories," which made it write more, not because the transcript was better, but because the instruction was different

**The honest conclusion**: you could get Best-quality summaries from the Nano transcript by simply running the summariser twice and picking the better output, or by tweaking the summarise skill to be more thorough by default.

### Recommended Default Pipeline

| Step | Model | Cost/episode (2hr) | Reasoning |
|------|-------|-------------------|-----------|
| Transcription | AssemblyAI Nano | ~$14 | 99.4% identical to Best |
| Correction | Claude Haiku | ~$0.05 | Catches obvious errors; Opus adds marginal value |
| Analysis | Claude Sonnet 4.6 | (conversation cost) | Standard analysis |
| Summary | Claude Sonnet 4.6 | (conversation cost) | Standard summary with podcast-summary-standards enforced |

**Total: ~$14 per 2-hour episode** — roughly $7/hour of podcast content.

If a summary feels thin after the first pass, re-run `/podcast-summarize` — that costs nothing extra and is more likely to improve quality than upgrading the transcription model.
