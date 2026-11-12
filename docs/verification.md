# Packaging verification · 12 November 2026

## Passed

- 497 Drive files copied/exported, including seven native Google Docs exported as Markdown. Three instructor resources are recorded by source link.
- Download byte lengths matched available non-native Drive metadata. All copied/exported Drive files matched the SHA-256 hashes in the source inventory.
- Current Jira CSV and JSON have the same 52 unique PG1 records; each has a corresponding Markdown issue page. Status totals: 18 Done, 1 In Progress, 33 To Do.
- Historical 5 November and 9 November exports each retain 52 PG1 records and their own recorded statuses.
- Python source files in both existing implementation folders parse successfully. Existing implementation files, configuration and sample inputs remain byte-identical to the GitHub base commit.
- Added Markdown navigation links resolve within the repository.
- HTML local-file link checks covered 1,965 references across the three documentation snapshots.
- Original code ZIP and copied Office containers pass ZIP integrity checks.
- Public copies of Jira data omit internal account IDs, watchers and administrative fields. Text and Office XML checks found no project email addresses, account-ID strings, or obvious credential patterns. LaTeX macro names that resemble emails were reviewed as false positives.

## Source gaps preserved

The latest (5 November) HTML main page references `Left.jpg`, `Right.jpg` and `final.png`; these images were absent from the shared source folders. The 29 October package also lacks five formula PNGs (`form_0.png` through `form_4.png`). The 22 October draft lacks the three result images and four formula PNGs (`form_0.png` through `form_3.png`). There are 18 unresolved local references across all historical HTML files. The originals are preserved; no replacement test-result images were invented.

Historical setup commands and configuration names in the Doxygen text differ from the current implementation. Use [the current run guide](setup.md). The source Doxyfile still has its original “PBL Group 21” title.

## Not established by these checks

Packaging verification does not establish projector calibration, image quality, a successful classroom demo, or completion of tasks marked Done. OpenCV is not installed in the collection environment, so the GUI application was not executed. No independent hardware test results were supplied by the shared Drive results folder.
