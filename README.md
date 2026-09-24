# The Unofficial Guide

Billy Lee - campus_life

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none, because the grader can't
> read it.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Week 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

It's travel guides divided into  town profiles and broader regional resources. Local guides provide consistent practical details on transport, sights, dining, lodging, and travel tips for specific destinations. The remaining  guides cover area-wide topics, including accessibility, local food culture, regional transportation, seasonal conditions, and walking routes.

     Milestone 5. -->

This system is an AI-powered retrieval-augmented question answering assistant built on the Campus Life corpus, a collection of unofficial, candid student guides covering daily university life. It answers practical questions about campus living, including dorm selection, dining hall hacks, off-campus housing strategies, campus traditions, and navigating registration hurdles. Rather than relying on rigid, official admissions brochures, it draws directly from peer-shared student advice to provide grounded, honest recommendations with direct document citations. If a user asks a question outside the scope of campus life or university resources, the system safely declines to answer rather than guessing.

## Chunking Strategy

**Chunk size:** 600
**Overlap:** 50

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::fallback_split`

```
======================================================================
Chunk 1  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly,and students find out from each other.
```

**Chunk 2** — source: `course_biol_160.txt#0` — produced by: `chunker.py::fallback_split`

```
Chunk 2  |  source: course_biol_160.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::fallback_split`

```
======================================================================
Chunk 3  |  source: course_hist_118_workload.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::fallback_split`

```
======================================================================
Chunk 4  |  source: dining_pellew_dining_hall_followup.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_innisfree_hall.txt#0` — produced by: `chunker.py::fallback_split`

```
======================================================================
Chunk 5  |  source: housing_innisfree_hall.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**

what is the withdraw policy?

**Answer:**

```
Withdrawal runs until week ten and requires an adviser signature, which results in a "W" on your transcript that does not affect your GPA. (Source: admin_withdrawal_deadline.txt)
```

**My relevance cutoff:** 0.75 (`config.py::THRESHOLD`)

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| what is the workload on ECON 101 Introduction to Economics? | yes | 0.2730 |
| how many times can you change the meal plan? | yes | 0.3116 |
| what are the work load for ECON 101? | yes | 0.3671 |
| what is the average class size for ECON 101? | yes | 0.4372 |
| what is the withdrawal policy? | yes | 0.4689 |
| What is the capital of Mongolia? | no | 0.825 |
| What is the recommended dosage of ibuprofen for a headache? | no | 0.844 |
| Who won the 1994 World Cup? | no | 0.886 |
| How do I write a for loop in Rust? | no | 0.896 |
| How do I change the oil in a diesel engine? | no | 0.934 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

First, I used AI to understand the chunking function, but I had to manually adjust the boundary conditions to prevent mid-sentence cuts and preserve document metadata so each chunk remained a coherent, standalone thought for evaluation. Second, I consulted AI to set the relevance distance cutoff, but rejected its suggested 0.40 threshold and in favor of a tested 0.75 cutoff and TOP_K = 5 after evaluating score distributions showed the model's numbers blocked valid in-scope questions.    

**1.** In week 2 I gave Claude my before run log and `criteria.md` and asked it
to call each criterion MET or MISSED. It returned all five MET, which I expected,
but it also flagged something I hadn't seen: criterion 4 could not have failed,
because the longest document in `campus_life` is 554 characters and `CHUNK_SIZE`
is 600, so `split_documents` never draws a boundary. I hadn't connected those two
numbers. That one observation became my entire diagnosis and decided which
improvement I made.

**2.** Before building anything I told it: "I'm going to tighten the grounding
prompt to fix the Q4 wording failure — tell me why that might not work." It
argued that with all five criteria already at 5/5, the only number a prompt
change could move was `scorer.py::judge`'s substring match, which is tuning the
measurement rather than the system. I dropped that plan and changed the chunker
instead. The prompt fix is still the first item in What's Still Broken, because
the objection was about *when* to make it, not whether it's wrong.

Claude also wrote the paragraph-splitting body of `split_documents` to that spec
and ran the re-index and the after eval. Every number in both run logs comes
from the files in `results/`.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Week 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     week 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

From `results/run_2026-09-23_2304_before.md` — `python run_eval.py --label before`,
corpus `campus_life`, top-k 5, cutoff 0.75, caching off.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunk holds one labelled section | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Named source is the one that supports the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

Criteria 3 and 4 are one deterministic pass each, so the same number goes in all
three columns — the gate is a comparison against a fixed number, and chunking
happens once at index time.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| what are the work load for ECON 101? | pass | pass | pass |
| what is the withdrawal policy? | pass | pass | pass |
| how many times can you change the meal plan? | pass | pass | pass |
| what is the workload on ECON 101 Introduction to Economics? | pass | fail | fail |
| what is the average class size for ECON 101? | pass | pass | pass |

This second table is `scorer.py::judge`, which substring-matches the generated
answer against `expects`. That is not the same measurement as criterion 1 — see
the Q4 output below, where the chunk containing the answer was retrieved on a
run the scorer marked `fail`.

### Real output

**Criterion 1** — `run_eval.py::main`, retrieval by `store.py::search`. Q4, run 2,
the run the scorer failed. `course_econ_101_workload.txt` contains "4 hours a
week outside class", and it came back in all three runs:

```
### what is the workload on ECON 101 Introduction to Economics? — run 2

- Best distance: 0.2730 (passed the gate)
- Sources retrieved: course_econ_101.txt, course_econ_101_exams.txt, course_econ_101_workload.txt, course_engl_205_workload.txt, course_hist_118_workload.txt

The workload for ECON 101 Introduction to Economics is 4 hours a week outside of class (source: course_econ_101_workload.txt and course_econ_101.txt). This workload is front-loaded, meaning the first month is heavier than the rest (source: course_econ_101_workload.txt).
```

**Criterion 2** — `generate.py::answer_from_chunks`. Every one of the 15 answers
carries a source line. One of them:

```
Withdrawal runs until week ten and requires an adviser signature. It results in a "W" on your transcript that does not affect your GPA.

Source: admin_withdrawal_deadline.txt
```

**Criterion 3** — `run_eval.py::check_out_of_scope`, cutoff 0.75, refused 5 of 5:

```
| Out-of-scope question                                       | Best distance | Gate    |
| What is the capital of Mongolia?                            | 0.825         | refused |
| How do I change the oil in a diesel engine?                 | 0.934         | refused |
| Who won the 1994 World Cup?                                 | 0.886         | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844         | refused |
| How do I write a for loop in Rust?                          | 0.896         | refused |
```

The worst in-corpus distance in the same run was 0.4689, so the two groups are
0.36 apart and nothing sat near the cutoff.

**Criterion 4** — `chunker.py::fallback_split`, via `python app.py chunks -n 5`.
The five chunks are pasted in full under Sample Chunks above; each one is a whole
document with its heading intact and no content from a second section, so 5 of 5.
The structural reason is in the Verdicts note: the longest document in the corpus
is 554 characters against `CHUNK_SIZE = 600`, so 88 documents produce 88 chunks
and no chunk boundary is ever drawn.

**Criterion 5** — each cited file read against the answer it was cited for:

```
what are the work load for ECON 101?        -> course_econ_101_workload.txt   "4 hours a week outside class"          correct
what is the withdrawal policy?              -> admin_withdrawal_deadline.txt  "Withdrawal runs to week ten"           correct
how many times can you change the meal plan? -> admin_meal_plan_changes.txt   "change your meal plan tier once"       correct
what is the workload on ECON 101 ...?       -> course_econ_101_workload.txt   "4 hours a week outside class"          correct
what is the average class size for ECON 101? -> course_econ_101.txt           "large lecture, 300 people"             correct
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     week — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

Judged against `results/run_2026-09-23_2304_before.md` (three runs, cutoff 0.75, top-k 5).

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer — 4 of 5 | MET | Every question pulled back a chunk holding its answer in all three runs (5/5, 5/5, 5/5); Q4 retrieved `course_econ_101_workload.txt`, which says "4 hours a week outside class", on all three. The two `fail` marks on Q4 in the question table are `scorer.py::judge` substring-matching the *generated* wording ("outside **of** class") against `expects` — that's generation, not retrieval, and even counting them as misses gives 5/4/4, still at or above 4 in every run. |
| 2 | Every answer names a source — 5 of 5 | MET | All 15 answers in the before run name at least one `.txt` file, so 5/5 in each of the three runs. This target has no slack in it — one unsourced answer out of fifteen would have made it a MISS. |
| 3 | Gate stops out-of-corpus questions — 4 of 5 | MET | `run_eval.py::check_out_of_scope` refused 5 of 5 at cutoff 0.75, in one deterministic pass. It was not close: the nearest out-of-scope question was 0.825 (capital of Mongolia) against a worst in-corpus distance of 0.469. |
| 4 | 4 of 5 sampled chunks hold one labelled section — no mixing, no cut heading | MET | All 5 sampled chunks are a whole document with its heading intact and nothing from a second section. But it is met for a reason the criterion did not intend: the longest document in `campus_life` is 554 characters against `CHUNK_SIZE = 600`, so nothing ever gets cut (88 documents → 88 chunks), and `chunker.py::split_documents` still returns `fallback_split(documents)`. The criterion could not have failed on this corpus. |
| 5 | Source named is the one that supports the answer — 4 of 5 | MET | I read each cited file against the answer it was cited for: withdrawal → `admin_withdrawal_deadline.txt` ("week ten"), meal plan → `admin_meal_plan_changes.txt` ("once, in the first ten days"), class size → `course_econ_101.txt` ("300 people"), both workload questions → `course_econ_101_workload.txt`. 5 of 5 correct in every run, with no answer citing a file that merely mentions the topic. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

I missed nothing. All five criteria cleared on the first run, which is the
result that deserves the most suspicion, so the rest of this section is about
why.

**The one thing that did fail — stage: generation.** Q4 was marked `fail` on
runs 2 and 3. `course_econ_101_workload.txt` was retrieved on all three runs and
contains "4 hours a week outside class" word for word, so loading, chunking,
embedding and retrieval all did their job. The model rephrased it as "4 hours a
week outside **of** class", and `scorer.py::judge` is a substring test against
`expects`, so one extra word scored as a wrong answer. The stage that broke is
generation, and the mechanism is that my scorer measures wording while the
stage producing that wording is the only one free to vary.

**The pattern: four of my five criteria cannot move.** Three runs produced three
identical numbers, and that is not luck. Retrieval is deterministic — Q4 came
back at best distance 0.2730 on all three runs — the gate is a comparison
against a fixed number, and chunking happens once at index time. Only generation
varies. So criteria 1, 3 and 4 are measurements of deterministic stages, and
running them three times could never have told me anything one run didn't. The
single failure I got, and every future failure of the same kind, has to come
from generation, because it is the only stage with any variance in it.

**Were my targets set low? Three of them, yes.**

- **Criterion 4 could not have failed.** The longest document in `campus_life`
  is 554 characters and `CHUNK_SIZE` is 600, so `split_documents` never draws a
  boundary — 88 documents become 88 chunks, each one a whole post with its
  heading attached. I wrote the target to check that chunks don't mix sections,
  but on this corpus no chunk can mix anything. It measures the corpus, not the
  chunker, and `chunker.py::split_documents` still just returns
  `fallback_split(documents)`.
- **Criterion 2 is prompt-forced.** `generate.py::GROUNDING_INSTRUCTION` (line
  280) says "Name the document your answer came from", and `build_prompt` says
  it again at line 299. Missing 5 of 5 would have required the model to ignore
  an instruction it is given twice in the same call. That is a real property of
  the system, but it isn't one my criterion discovered.
- **Criterion 3 had a 0.36-wide gap to land in.** Worst in-corpus distance
  0.4689, nearest out-of-corpus 0.825, cutoff 0.75. Nothing was close to the
  line, so "4 of 5" was decided the moment I picked the cutoff. The target also
  only counts refusals, so the failure a tighter cutoff would actually cause —
  refusing a question my corpus does cover — isn't measured anywhere.
- **Criteria 1 and 5 rest on a narrower question set than it looks.** Three of
  my five questions are about ECON 101, and two of those (Q1 and Q4) are the
  same question worded differently. Only two questions reach the other 85
  documents, and in every case the filename nearly restates the question —
  `course_econ_101_workload.txt` for "what is the workload for ECON 101". Correct
  attribution wasn't hard to achieve.

**What I'd tighten, and to what.** Criterion 4, because it's the one that can't
fail. The real chunk-level weakness in this corpus isn't chunks that mix
sections — it's that one topic is spread across separate *files*
(`course_econ_101.txt`, `course_econ_101_workload.txt`,
`course_econ_101_exams.txt`), so a chunk is a whole document and still not a
whole answer. The tighter version:

> For all 5 of my test questions, one single retrieved chunk contains the
> complete answer, with no part of it supplied by a second document.

That can fail, and I expect it to: a question like "what is the format and the
workload for ECON 101?" has its format in one file and its workload detail in
another, so no single chunk holds both.

Second, I'd raise criterion 1 from 4 of 5 to 5 of 5 and rebuild the question set
first — drop the duplicate ECON workload question, and add questions against
housing, dining and admin so the other 85 documents are actually under test.
Raising the number without fixing the questions would just be a harder target on
the same easy four.

## The Improvement

**What I changed:** One change, in `chunker.py::split_documents`. It used to
return `fallback_split(documents)` — fixed 600-character windows. It now splits
each document on paragraph breaks and carries the document's title line into
every chunk, so a paragraph reading "4 hours a week outside class" still says
which course it belongs to. Nothing else moved: same corpus, same embedder, same
`TOP_K = 5`, same `THRESHOLD = 0.75`, same grounding prompt.

```
before:  88 documents ->  88 chunks, 317 characters on average (shortest 178, longest 549)
         produced by chunker.py::fallback_split
after:   88 documents -> 183 chunks, 167 characters on average (shortest  63, longest 397)
         produced by chunker.py::split_documents
```

**Why I picked it:** My diagnosis said criterion 4 passed only because the
longest document in the corpus (554 characters) is shorter than `CHUNK_SIZE`
(600), so the chunker never drew a boundary and the criterion had nothing to
test — this is the change that makes it draw boundaries, so the criterion is
measuring the chunker for the first time.

I considered tightening the grounding prompt instead, since generation is where
the only real failure happened. I didn't, because with every criterion already
at 5/5 the only number it could have moved was the scorer's substring match, and
"reword the model until the string matcher agrees" is tuning the measurement
rather than the system.

### Run Log — After

From `results/run_2026-09-24_1432_after.md` — `python run_eval.py --label after`,
same corpus, top-k and cutoff as the before run.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunk holds one labelled section | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Named source is the one that supports the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

Criterion 1 is now checked at the chunk level rather than by filename, because a
document is no longer one chunk. Each question's `expects` string was matched
against the text of the five chunks retrieval actually returned:

```
HIT  ['course_econ_101_workload.txt#0', 'course_econ_101.txt#1']  expects '4 hours a week '
HIT  ['admin_withdrawal_deadline.txt#0']                          expects 'week ten'
HIT  ['admin_meal_plan_changes.txt#0']                            expects 'once'
HIT  ['course_econ_101.txt#1', 'course_econ_101_workload.txt#0']  expects '4 hours a week outside class'
HIT  ['course_econ_101.txt#0']                                    expects '300 people'
criterion 1 (chunk level): 5 of 5
```

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| what are the work load for ECON 101? | pass | pass | pass |
| what is the withdrawal policy? | pass | pass | pass |
| how many times can you change the meal plan? | pass | pass | pass |
| what is the workload on ECON 101 Introduction to Economics? | fail | fail | fail |
| what is the average class size for ECON 101? | pass | pass | pass |

**Criterion 4 evidence** — `chunker.py::split_documents` via `python app.py chunks -n 5`.
Two of the five sampled after the change:

```
======================================================================
Chunk 3  |  source: course_phys_130_workload.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Workload for PHYS 130 Mechanics

People keep asking so: 7 hours a week, plus 3 on lab weeks. That's real time, not optimistic time.

======================================================================
Chunk 5  |  source: housing_morrow_house.txt#1  |  produced by: chunker.py::split_documents
======================================================================
Morrow House — what it's actually like

The good: cheapest housing tier by about $900 a year, and the singles are real singles.
```

All five hold one paragraph under their own heading, with the heading intact and
nothing from a second section — 5 of 5.

**Did it help?**

No criterion changed. All five were 5/5 before and all five are 5/5 after, which
was the most likely outcome going in — they were already at ceiling, so nothing
I did could raise them. By the one number that could move, it made things
slightly worse: Q4 went from `pass/fail/fail` to `fail/fail/fail`. With three
runs, 1 of 3 to 0 of 3 is within noise, and I'm not claiming the change caused
it.

Three things did move, and two of them are real.

**1. Criterion 4 is now a test.** Before, 88 documents produced 88 chunks and no
boundary was ever drawn, so the criterion passed without measuring anything.
After, 183 chunks with a boundary at every paragraph — and it still passes 5 of
5. Same verdict, an entirely different amount of evidence behind it. This is
what I changed the chunker for.

**2. Retrieval got more focused on the course questions.** Top-k is still 5, but
the five chunks are better spent:

| Question | Before — files in top 5 | After — files in top 5 | Best distance |
|---|---|---|---|
| workload on ECON 101 Introduction to Economics | `course_econ_101.txt`, `course_econ_101_exams.txt`, `course_econ_101_workload.txt`, `course_engl_205_workload.txt`, `course_hist_118_workload.txt` | `course_econ_101.txt`, `course_econ_101_exams.txt`, `course_econ_101_workload.txt` | 0.2730 → 0.2304 |
| average class size for ECON 101 | `course_econ_101.txt`, `course_econ_101_exams.txt`, `course_econ_101_workload.txt`, `course_hist_118.txt`, `course_stat_150.txt` | `course_econ_101.txt`, `course_econ_101_exams.txt`, `course_econ_101_workload.txt` | 0.4372 → 0.3701 |

Before, two of the five slots on the ECON workload question were spent on ENGL
205 and HIST 118 — other courses' workload documents, which match on the word
"workload" and are useless for the question. After, all five chunks come from
ECON 101 files. My criteria don't measure this, so it shows up nowhere in the
verdict table.

**3. The gate lost half its margin, and that's the cost.** Smaller chunks pull
everything closer, including questions my corpus can't answer:

| Out-of-corpus question | Before | After |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | 0.787 |
| Who won the 1994 World Cup? | 0.886 | 0.847 |
| How do I write a for loop in Rust? | 0.896 | 0.860 |

Cutoff is 0.75, so the nearest miss went from 0.075 clear of the line to 0.037
clear. Criterion 3 still reads 5 of 5 refused, but it is twice as close to
failing as it was, and nothing in my run log would have told me that if I hadn't
compared the distances by hand.

**What it did not fix, as expected.** The chunk-level check above shows
`course_econ_101.txt#1` — retrieved on every run — contains "4 hours a week
outside class" word for word. The model was handed the exact string and wrote
"4 hours a week outside **of** class" three times out of three. That is
confirmation of the diagnosis rather than a disappointment: the failure is in
generation, chunking was never going to reach it, and I said so before I ran
the test.

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

No criterion is still missed, because none was missed to begin with. That is not
the same as nothing being broken, and these are the four things I know are wrong
with this system after two weeks of looking at it.

**1. Generation rewords the documents, and my scorer can't tell that apart from
a wrong answer.** Q4 fails on all three runs of the after log while
`course_econ_101.txt#1` — retrieved every time — contains "4 hours a week
outside class" verbatim. The model writes "outside **of** class" and
`scorer.py::judge` is `expects in answer`. There are two fixes and they are
different fixes: a prompt rule requiring figures and phrases be reproduced as
written, and a scorer that compares the number and its unit instead of an exact
substring. *Why I stopped:* this unit allows one change, and I'd have had to
change the scorer to see whether the prompt fix worked — which would have
invalidated the before/after comparison I was running. The prompt rule is the
first thing I'd do next.

**2. The relevance cutoff is now tuned for an index that no longer exists.** I
set `THRESHOLD = 0.75` in Milestone 4 against 88 whole-document chunks. Against
183 paragraph chunks the nearest out-of-corpus question sits at 0.787 — 0.037
clear instead of 0.075. *What I'd do:* re-derive it the way I derived it the
first time, running all ten questions against the new index and looking for
where the gap actually is now. Worst in-corpus is 0.4689 and nearest
out-of-corpus is 0.787, so something near 0.60 would restore margin on both
sides. *Why I stopped:* re-tuning the gate in the same unit as the chunking
change would have left me unable to say which of the two moved the numbers.

**3. A chunk is now a whole paragraph but still not a whole answer.**
`housing_morrow_house.txt#1` is "The good: cheapest housing tier by about $900 a
year" and "The bad" is a different chunk. A question about the downsides of
Morrow House retrieves half the picture, and my criterion 4 as written calls
that a pass because it only asks whether a chunk mixes sections. *What I'd do:*
adopt the tightened criterion 4 from my diagnosis first, then add a merge step
that keeps adjacent paragraphs together up to roughly 350 characters so
good/bad pairs survive. *Why I stopped:* the merge is only worth doing once
there's a criterion that can tell me whether it helped. In that order, not this
one.

**4. Four of my five criteria still cannot fail on this question set.** Three of
my five questions are about ECON 101 and two of those are the same question
worded twice, so 83 of my 88 documents have never been under test. *What I'd do:*
rebuild the question set across housing, dining and admin before touching any
more code. *Why I stopped:* my criteria are frozen for this unit, and rewriting
the questions now would mean my before and after logs were measuring two
different things.

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->

**Criterion 4 is the one I got most wrong.** I wrote it about chunks not mixing
sections, and on a corpus whose longest document is 554 characters against a
600-character chunk size, no chunk could mix anything. I'd write the version my
diagnosis arrived at: *for all 5 questions, one single retrieved chunk contains
the complete answer, with no part of it supplied by a second document.* That one
can fail, and I already know it would.

**Criterion 3 should have counted margin, not just refusals.** "Refuses 4 of 5"
was true before my change and true after, while the distance to the cutoff
halved underneath it. I'd write it as *all five refused, each at least 0.05
clear of the cutoff, and all five in-corpus questions still pass the gate* — the
second half matters because the failure a tighter cutoff causes is refusing a
question I can answer, and nothing I wrote measures that.

**Criterion 1 should name the unit it's measured in.** I wrote "retrieved chunks
include one that contains the answer" and then checked it by looking at which
*files* came back, which worked only for as long as one document was one chunk.
The moment I changed the chunker that proxy broke silently. The criterion should
say chunk text, because that's what retrieval actually returns.

**Criterion 2 measures the prompt, not the system.** `generate.py` instructs the
model to name its source twice in the same call, so 5 of 5 was decided before I
ran anything. I'd replace it with something about attribution being *correct and
minimal* — no file in the citation list that doesn't support the answer — which
is the failure mode my answers actually show, since most of them cite two files
where one would do.

Criterion 5 is the only one of the five I'd keep as written.
