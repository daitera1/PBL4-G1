# Week 3 assigned tasks and deadlines

**Current schedule: [Gantt schedule](Gantt-Schedule.md).** The user’s latest request authorizes earlier deadlines for simpler tasks and time for leader review. This replaces the previous identical Wednesday deadline for every person. Final team handover remains 28 October 2026 at 23:59 JST.

## Development — Haruho

### Daisuke · UML & interfaces — PG1-4

Planned dates: 2026-10-22 to 2026-10-23. **Due: 23 October 2026, 23:59 JST**

Work: Create/review the initial Astah class diagram with Haruho. Show image loading, image split/overlap, alignment, blending and output responsibilities; mark planned components versus implemented ones. Agree interfaces before implementation proceeds.

Handoff/review: Send reviewed UML and agreed interfaces to Haruho, Sousuke and Monika by 23 October.

Evidence: Attach Astah source plus PNG/PDF diagram and a short review note naming agreed interfaces. Hand the diagram to Sousuke and Monika.

Status/evidence snapshot: To Do. No UML attachment or completion update is visible on this issue; repository is still empty.

### Marcus · Setup & blending experiment — PG1-5

Planned dates: 2026-10-23 to 2026-10-24. **Due: 24 October 2026, 23:59 JST**

Work: Write the projector arrangement, overlap and geometry notes first. With Haruho, implement one small overlap/blending experiment using the agreed input and interfaces. Record chosen overlap/settings and what still requires projector calibration; do not claim full alignment is complete.

Handoff/review: Send experiment, input/output examples and settings to Haruho by 24 October.

Evidence: Link demo/setup notes, the experiment commit or source files, and before/after output using the same input. Hand the working experiment and settings to Haruho and Hanz.

Status/evidence snapshot: To Do. No notes, code attachment or completion update is visible on this issue.

### Haruho · Prototype & technical review — PG1-6

Planned dates: 2026-10-23 to 2026-10-27. **Due: 27 October 2026, 18:00 JST**

Work: Agree the minimum design/interfaces with Daisuke. Publish a Python/OpenCV baseline that loads a known still image and produces the agreed two-projector outputs with configurable overlap. Integrate Marcus’s small blending experiment, document the alignment/calibration approach, and identify unfinished hardware work.

Handoff/review: Publish a runnable baseline by 25 October at 18:00 JST for Hanz and Pan. Reserve 26–27 October for fixes and technical leader review after Hanz’s report.

Evidence: Push/link runnable source, sample input, dependency list, exact run command and sample output. Give Hanz and Pan the same revision to test/document. This deadline is for a testable weekly prototype, not a claim that the final calibrated system is complete.

Status/evidence snapshot: To Do. No prototype attachment or completion update is visible on this issue; GitHub has no commits at the time of review.

### Hanz · Test prototype & report — PG1-7

Planned dates: 2026-10-25 to 2026-10-26. **Due: 26 October 2026, 18:00 JST**

Work: Prepare a short test checklist now, then run Haruho’s published revision using the documented steps. Check image loading, output dimensions/overlap, visible seams and failure handling. Test on the two projectors if available; otherwise clearly separate software results from untested hardware behavior.

Handoff/review: Prepare the checklist before the baseline handoff; test the published revision on 25–26 October. Send results to Haruho and Pan by 26 October at 18:00 JST.

Evidence: Link a report with source revision, input, environment/settings, expected and actual results, screenshots and reproducible bugs. Send findings to Haruho and results to Pan. Record any unavailable hardware as a blocker.

Status/evidence snapshot: To Do. No test report or completion update is visible on this issue; the shared results folder is empty.

## Documentation — Monika

### Bien · Doxywizard sample & config — PG1-12

Planned dates: 2026-10-22 to 2026-10-23. **Due: 23 October 2026, 23:59 JST**

Work: Complete the LINE-assigned Doxywizard work: run 13 - SampleWithMainPage, save the configuration and open the generated HTML. Record tool versions, input/output paths, exact generation steps and any errors. Give the repeatable generation instructions/configuration to Monika and Pan.

Handoff/review: Give saved sample configuration, working HTML and repeatable generation steps to Monika and Pan by 23 October.

Evidence: Link the saved Doxygen configuration, sample source reference, generated HTML folder/ZIP and a screenshot showing the Main Page opens. Include a short generation guide; label sample documentation separately from project documentation.

Status/evidence snapshot: To Do. No generated documentation/configuration is attached here; the shared Bien folder still contains only the original checklist.

### Sousuke · Overview & comment format — PG1-11

Planned dates: 2026-10-22 to 2026-10-24. **Due: 24 October 2026, 23:59 JST**

Work: Review the uploaded overview against Daisuke’s UML and Haruho’s actual approach. Correct assumptions, hand the reviewed text to Monika for the Main Page, and provide one documented function example using @brief, @param and @return where appropriate.

Handoff/review: Review against Daisuke’s UML after 23 October. Give the overview to Monika and comment example to Pan by 24 October; reconcile with the actual prototype when available.

Evidence: Attach/link the revised overview and comment example. Monika can reuse the prose, and Pan can apply the convention.

Status/evidence snapshot: In Progress. Project Overview and Design.docx is attached; its purpose/problem section was reviewed. Final technical review and comment-format output are not yet verified.

### Pan · Run guide & results section — PG1-9

Planned dates: 2026-10-25 to 2026-10-27. **Due: 27 October 2026, 12:00 JST**

Work: Own the Main Page setup/running/results section. Use Haruho’s actual prototype and Bien’s generation steps; test the written run instructions. Apply Sousuke’s agreed comment convention to the available public functions with developer review. Add Hanz’s test results and label anything not yet tested.

Handoff/review: Draft setup instructions from Haruho’s baseline; add Hanz’s results after 26 October. Give the tested setup/results section to Monika by 27 October at 12:00 JST.

Evidence: Link the setup/results source, exact run command and tested source revision, comments commit/file, and captions/evidence links for real test results. Hand the section to Monika as soon as it is ready, allowing generation before the shared Wednesday deadline.

Status/evidence snapshot: To Do. No code-comment or Main Page output is attached here; the shared Pan folder still contains only the original checklist.

### Monika · Main Page & docs review — PG1-8

Planned dates: 2026-10-24 to 2026-10-28. **Due: 28 October 2026, 18:00 JST**

Work: Own the Main Page purpose/design section: integrate Sousuke’s reviewed overview and Daisuke’s UML instead of duplicating the draft. Combine it with Pan’s setup/results section, use Bien’s Doxygen configuration, and generate/review the project HTML. Keep unimplemented features and untested results clearly marked.

Handoff/review: Integrate the overview/configuration from 24 October. Combine Pan’s section on 27 October; reserve 28 October for documentation leader review, fixes and generation. Give final HTML/source to Watts by 18:00 JST.

Evidence: Link Main Page source, the configuration used, generated project HTML folder/ZIP and a brief review checklist. Verify navigation, images/diagram and links open. Coordinate early handovers with Pan and Watts so the combined documentation is ready by the shared Wednesday deadline.

Status/evidence snapshot: In Progress on the latest Jira timeline check on 22 October. No new completion evidence was reviewed during scheduling; Sousuke’s earlier overview draft remains available.

## Management — Jake

### Tarun · Workload & access check — PG1-10

Planned dates: 2026-10-22 to 2026-10-23. **Due: 23 October 2026, 18:00 JST**

Work: Confirm availability and workload for the 12 named members: Jake, Haruho, Daisuke, Marcus, Hanz, Monika, Pan, Sousuke, Bien, Tarun, Sariga and Watts. Jake has confirmed Yuki is not part of this work. Check each owner understands the output/deadline, has required tool/access, and can meet the handover. Escalate clashes to Jake before deadlines slip.

Handoff/review: Give Jake the 12-person workload/access table and urgent blockers by 23 October at 18:00 JST.

Evidence: Link a 12-person table containing Jira key, accepted task, deadline, availability and blockers. Flag overloaded or unavailable owners and propose a specific redistribution for Jake to decide. Report access blockers as soon as they are found.

Status/evidence snapshot: To Do. No availability chart or workload report is visible on this issue.

### Sariga · Meeting notes & decisions — PG1-14

Planned dates: 2026-10-22 to 2026-10-26. **Due: 26 October 2026, 23:59 JST**

Work: Publish this week’s meeting record: attendance, actual instructor feedback, agreed technical approach, weekly role handovers, decisions, blockers and action owners/dates. Use the 12-member roster; Yuki is excluded. Ask owners to confirm factual contributions rather than treating planned tasks as completed.

Handoff/review: Publish dated notes and owner/action decisions by 26 October; append any final review decisions on 28 October for Jake.

Evidence: Link dated meeting notes and an action table. Each decision/action has an owner, date and related Jira/file link; unconfirmed points remain marked pending. Append actual weekly outcomes in time for Jake’s review by the shared Wednesday deadline.

Status/evidence snapshot: To Do. No meeting notes, decisions or completion update is visible on this issue.

### Watts · Jira & evidence handover — PG1-15

Planned dates: 2026-10-26 to 2026-10-28. **Due: 28 October 2026, 20:00 JST**

Work: Check owners/deadlines with the team and reconcile PG1-17; coordinate Main Page tracking with Monika/Pan. Check everyone can reach the shared resources and escalate editing/upload problems to Jake. Collect the tested code revision, UML, generated docs and test report into one linked weekly evidence index.

Handoff/review: Assemble an initial evidence index on 26–27 October. Check final documentation after Monika’s 28 October 18:00 handoff; give Jake the complete linked index by 20:00 JST, leaving time for final PM review.

Evidence: Link a weekly handover index listing each owner, task, actual status, evidence and unresolved blocker. Check links work for the team. This Wednesday deadline is the weekly handover checkpoint; retain 29 October as the later delivery milestone rather than implying final project completion.

Status/evidence snapshot: In Progress. The task board exists and PG1-16 is Done. PG1-17 remains To Do even though Jake and Sousuke now have assigned tasks. No weekly delivery bundle is visible here.

### Jake · Coordination & final review — PG1-13

Planned dates: 2026-10-22 to 2026-10-28. **Due: 28 October 2026, 23:59 JST**

Work: Confirm the weekly baseline with Haruho, obtain the 12 owners’ acknowledgments and resolve access/ownership blockers. Review progress as outputs become available and coordinate handovers before the shared Wednesday deadline. Use Tarun’s workload check to adjust any infeasible assignment and record the decision.

Handoff/review: Coordinate blockers throughout the week. Reserve 28 October for checking Haruho’s technical review, Monika’s documentation review and Watts’s evidence index. Final team handover: 28 October at 23:59 JST.

Evidence: Update the coordination record with actual decisions, per-person evidence, remaining blockers and next actions. Review Watts’s evidence index before the shared Wednesday deadline. Keep the individual Assignment 3 deadline (27 October, 13:00 JST) separate from internal team checkpoints.

Status/evidence snapshot: In Progress. Coordination plan is saved and this week’s individual tasks/deadlines have been added. Actual team check-in outcomes and completed outputs still need confirmation.

