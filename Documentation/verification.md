# Packaging verification · 12 November 2026

## Final documentation addition

- The team-specified final Drive folder contains 232 files; 231 deliverable files were copied, excluding only macOS `.DS_Store` metadata.
- All 231 file sizes match Drive metadata. Their SHA-256 hashes and source URLs are recorded in the inventory alongside the 497 previously archived files.
- All 973 local references in the final HTML package resolve. Main-page images were also confirmed loaded in the browser. The source HTML uses external MathJax for equation typesetting; without internet, equations may show TeX source. The real projector photograph, left/right inputs, blended result, team/project photos and formula assets are included.
- The final `code/` folder still contains documentation skeletons rather than a complete application. The existing Development run guide remains applicable to the delivered implementations.
- Professor navigation now opens the final documentation. Historical source gaps below apply only to the earlier snapshots.

## Final presentation and handover check

- Added `Presentation/` alongside Development, Documentation and Management, with native Canva PDF and PowerPoint exports containing 27 slides. The empty page after the closing slide was excluded.
- PDF opens without a password; all pages render. Reviewed the slides, screenshots and final page. PowerPoint contains 27 slides and passes archive integrity checks; use the PDF for consistent visual appearance.
- Rechecked all 497 archived Drive files against their source SHA-256 hashes and corrected the inventory paths after the department-folder reorganization.
- Rechecked 298 relative Markdown links and the offline `START_HERE.html` links; all resolve.
- Rechecked the CSV/JSON register: identical 52 records, all Done, covering 12 assignees with corresponding issue pages.
- Rechecked all 14 implementation Python files with the parser and all four Office/ZIP containers with archive integrity checks.
- The presentation adds team-reported demonstration photos. Its `main_alpha_blender.py` revision has not been matched to the delivered `main.py` implementations. Use the current run guide for the delivered files.

## Earlier collection checks

- 497 Drive files copied/exported, including seven native Google Docs exported as Markdown. Three instructor resources are recorded by source link.
- Download byte lengths matched available non-native Drive metadata. All copied/exported Drive files matched the SHA-256 hashes in the source inventory.
- Current Jira CSV and JSON have the same 52 unique PG1 records; each has a corresponding Markdown issue page. Final 12 November status totals: 52 Done, 0 In Progress, 0 To Do. All 12 assignees have no open tickets.
- Historical 5 November and 9 November exports each retain 52 PG1 records and their own recorded statuses.
- Python source files in both existing implementation folders parse successfully. Existing implementation files, configuration and sample inputs remain byte-identical to the GitHub base commit.
- Added Markdown navigation links resolve within the repository.
- HTML local-file link checks covered 1,965 references across the three documentation snapshots.
- Original code ZIP and copied Office containers pass ZIP integrity checks.
- Public copies of Jira data omit internal account IDs, watchers and administrative fields. Text and Office XML checks found no project email addresses, account-ID strings, or obvious credential patterns. LaTeX macro names that resemble emails were reviewed as false positives.

- Public ZIP downloaded without credentials: HTTP 200, ZIP integrity passed and all 595 initially published files matched their local source bytes.
- Final closeout preserves the 11 November export; task descriptions, summaries, assignees and due dates match it. [Closeout screenshots](../Management/jira/screenshots/README.md) record the completed operation and empty open-ticket search.

## Source gaps preserved

The latest (5 November) HTML main page references `Left.jpg`, `Right.jpg` and `final.png`; these images were absent from the shared source folders. The 29 October package also lacks five formula PNGs (`form_0.png` through `form_4.png`). The 22 October draft lacks the three result images and four formula PNGs (`form_0.png` through `form_3.png`). There are 18 unresolved local references across all historical HTML files. The originals are preserved; no replacement test-result images were invented.

Historical setup commands and configuration names in the Doxygen text differ from the current implementation. Use [the current run guide](setup.md). The source Doxyfile still has its original “PBL Group 21” title.

## Not established by these checks

Packaging verification does not establish projector calibration, image quality, a successful classroom demo, or completion of tasks marked Done. OpenCV is not installed in the collection environment, so the GUI application was not executed. No independent hardware test results were supplied by the shared Drive results folder.
