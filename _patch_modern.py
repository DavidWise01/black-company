#!/usr/bin/env python3
"""Bring Black Company roster to modern: add authored who/what/where/why/when/how
to every member (specialty kept — the page renders it). Idempotent.

Integrity: 'The Captain' keeps the standing note — the Annals record his death;
the exact circumstance is theirs to tell, not mine to invent. No detail asserted."""
import json
from pathlib import Path

P = Path(__file__).parent / "roster.json"
R = json.loads(P.read_text(encoding="utf-8"))

F = {
 "Croaker": {
  "who":"The Company's physician — and, in time, its Annalist and its Captain.",
  "what":"The cutter who keeps them breathing.",
  "where":"Wherever the Company marches — surgeon's kit in one hand, notebook in the other.",
  "why":"To mend his brothers, and to set down the truth of them.",
  "when":"From the Company's northern years onward.",
  "how":"With a blade for healing, a pen for remembering, and dry gallows wit."},
 "One-Eye": {
  "who":"An ancient little wizard in a battered black hat.",
  "what":"Half the Company's magic and most of its trouble; bearer of a poisoned spear.",
  "where":"The Company's column — usually mid-feud with Goblin.",
  "why":"Survival, mischief, and loyalty buried under centuries of cantankerousness.",
  "when":"Across the Company's whole recorded history.",
  "how":"Through battlefield sorcery, dirty tricks, and that spear."},
 "Goblin": {
  "who":"A toad-faced sorcerer — One-Eye's eternal rival.",
  "what":"Deadly, when he stops bickering long enough to cast.",
  "where":"The column, opposite One-Eye in every prank.",
  "why":"Loyalty to the Company, expressed almost entirely as a feud.",
  "when":"The Company's long road, to a grievous end.",
  "how":"Through quick magic and quicker insults."},
 "Silent": {
  "who":"The Company's mute sorcerer.",
  "what":"One who speaks only in spellwork — heals and harms without a word.",
  "where":"At the Company's side, and at Darling's.",
  "why":"Loyalty, and a love he never speaks aloud.",
  "when":"The early-to-middle Annals.",
  "how":"Through wordless magic alone."},
 "The Lady": {
  "who":"The sorceress-empress, heir to the Domination.",
  "what":"Beauty and near-absolute power; a maker of the Taken — and, later, Croaker's.",
  "where":"The empire of the north, then the long road south with the Company.",
  "why":"First dominion; then, stripped of power, something nearer to love.",
  "when":"From the Company's service to her, through her fall.",
  "how":"Through the Domination's stolen sorcery, statecraft, and an unbending will."},
 "Soulcatcher": {
  "who":"One of the Ten Who Were Taken — the Lady's sister.",
  "what":"Many voices in one cowl; brilliant, playful, mad.",
  "where":"The Company's first master, and a schemer ever after.",
  "why":"Her own tangled ends, never quite the Domination's.",
  "when":"The Company's northern years and beyond.",
  "how":"Through layered voices, raw sorcery, and deception."},
 "The Limper": {
  "who":"One of the Taken.",
  "what":"Cruel, relentless, and very hard to keep dead.",
  "where":"Wherever the Company least wants him.",
  "why":"Spite, and the will to survive.",
  "when":"A recurring scourge across the Annals.",
  "how":"Through brute sorcery and a sheer refusal to stay dead."},
 "The Lieutenant": {
  "who":"The Captain's second.",
  "what":"The steady hand that ran the Company between battles.",
  "where":"The command tent and the line.",
  "why":"Duty to the Captain and to the brotherhood.",
  "when":"The early Annals.",
  "how":"Through quiet competence and the chain of command."},
 "Darling": {
  "who":"A deaf girl the Company takes in, who becomes the White Rose reborn.",
  "what":"Null to all sorcery — the banner and the cause reborn.",
  "where":"From a ruined village to the heart of the rebellion.",
  "why":"To be the standard the free peoples rally to against the empire.",
  "when":"From childhood across the southern campaigns.",
  "how":"Through her null, her resolve, and the Company's shield around her."},
 "Croaker (Annalist)": {
  "who":"The Company's narrator and physician — later its Captain.",
  "what":"Keeper of the Annals; the Company's memory made ink.",
  "where":"Bent over the book by firelight after every march.",
  "why":"Because if it isn't in the Annals, it didn't happen.",
  "when":"Through all the years he carries the record.",
  "how":"With an honest pen and a surgeon's clear eye."},
 "Murgen": {
  "who":"The Company's standard-bearer turned Annalist.",
  "what":"One who carried the banner and the record both — even unstuck in time.",
  "where":"The southern years — Dejagore, and after.",
  "why":"To hold the Company's memory when Croaker no longer can.",
  "when":"The middle Annals.",
  "how":"Through the standard, the pen, and a mind that slips its moorings in time."},
 "Sleepy": {
  "who":"A later Annalist and Captain of the Company.",
  "what":"The one who carried the Company through the Glittering Stone years.",
  "where":"The far south, and the road toward Khatovar.",
  "why":"To keep faith with the Annals and the brotherhood.",
  "when":"The late Annals.",
  "how":"Through quiet endurance and the keeping of the book."},
 "One-Eye & Goblin": {
  "who":"The Company's two bickering wizards, taken together.",
  "what":"Centuries of pranks, curses, and insults — the Company's running joke.",
  "where":"Everywhere the column goes.",
  "why":"A feud that is, underneath, the deepest kind of loyalty.",
  "when":"The whole length of the Annals — to the grief when it finally ends.",
  "how":"Through escalating magical pranks that mask real devotion."},
 "Raven": {
  "who":"A cold, methodical, lethal man who joins the Company.",
  "what":"Darling's protector — the one who simply does what must be done.",
  "where":"At Darling's side, and in the shadows of the early rebellion.",
  "why":"To guard Darling — and to bury his own past.",
  "when":"The early-to-middle Annals.",
  "how":"Through lethal competence, and silence after."},
 "Elmo": {
  "who":"A Company sergeant.",
  "what":"The steady core of the line — the Company's spine made flesh.",
  "where":"The front rank, through the northern campaigns.",
  "why":"Loyalty to the Company, plain and total.",
  "when":"The early Annals.",
  "how":"Through steadiness, command of the line, and example."},
 "Otto & Hagop": {
  "who":"Two old-hand soldiers of the Company.",
  "what":"The two who always come back — together, grumbling, alive.",
  "where":"The line, march after march.",
  "why":"Gallows-loyalty to the brotherhood, to the last march.",
  "when":"From the early Annals to the late.",
  "how":"Through stubborn survival, and each other."},
 "The Captain": {
  "who":"The original commander of the Black Company, known by no other name.",
  "what":"The title that became a name — the man who held them together through the hardest years.",
  "where":"At the Company's head, in the north.",
  "why":"To keep the brotherhood whole and the contract honored.",
  "when":"The early Annals, until he fell.",
  "how":"Through command, endurance, and — when he fell — passing the title to Croaker. The Annals record his death; the exact circumstance is theirs to tell, not mine to invent."},
}

miss = []
for m in R["members"]:
    f = F.get(m["name"])
    if not f:
        miss.append(m["name"]); continue
    m.update(f)
if miss:
    raise SystemExit("UNMATCHED MEMBERS: " + ", ".join(miss))

R["note"] = R.get("note","") + " Every ACI now carries the full DLW tag with an authored six-W .spun (who/what/where/why/when/how)."
P.write_text(json.dumps(R, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("patched", len(R["members"]), "Black Company members with authored six-W fields")
