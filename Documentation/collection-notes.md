# Collection notes

Collected on **12 November 2026** for the PBL4 Group 1 GitHub repository.

## Sources

| Source | What is preserved |
| --- | --- |
| Existing GitHub `main` at `03a2f33d9af5a84c4f6f8d18579cad6c205eb88b` | Both Python implementations, configuration and sample images; original paths retained |
| Shared project Google Drive | Dated Doxygen packages, documentation source, generated HTML/LaTeX, images, team guides, role checklists, initial code skeleton and Astah UML |
| PG1 Jira exports dated 11 and 12 November 2026 | Preserved pre-closeout snapshot plus final 52-Done CSV/JSON and current Markdown issue pages |
| Management collection dated 11 November 2026 | Planning Markdown, Confluence wiki exports, historical design attachment and unconfirmed workload workbook |

The [Drive source inventory](drive-source-inventory.csv) maps every collected file to its source URL and modification date. SHA-256 hashes identify downloaded originals. Google Docs were exported as Markdown for reading directly on GitHub; document comments and revision histories are not part of those exports. File-level copy dates do not mean the content was newly written or approved on that date.

## Public repository handling

The repository is public. The Jira copy keeps project content but omits internal account IDs, watchers, administrative fields and email addresses. The full Jira Cloud site backup, original all-fields export and unrelated sample project remain in the local archive. The full backup is not needed to read the PG1 records here.

Course slides, the original assignment form and the instructor's coding/Doxygen sample ZIP are indexed by source link rather than republished. Team-created materials are copied into this repository. Personal Moodle reports and local scratch/build files are outside this shared project collection.

## Evidence boundaries

- Jira counts are a dated tracker snapshot, not proof of software acceptance.
- The workload workbook is prefilled and remains unconfirmed.
- Earlier documentation packages and the original empty-code ZIP are historical artifacts; the implementation folders at the repository root are the software source.
- The Drive `Final Files` and `Screenshots and Test Results` folders returned no files on 12 November 2026. Documentation illustrations are included, but no independent verified experiment dataset was found there.
- Generated Doxygen pages describe a historical code snapshot. They are not automatically synchronized to the current implementations.
- The initial collection did not change Jira statuses. A subsequent user-authorized [project closeout](../Management/jira/closeout-2026-11-12.md) transitioned the remaining 34 tickets to Done and added a fresh export and screenshots. Google Drive sharing settings and source files were unchanged.

## Keeping the repository current

Update code in its existing implementation folder. Put new technical documents under `docs/`, dated Jira exports under `project-management/jira/`, and test evidence beside an explanation of inputs, configuration and outcomes. Keep old snapshots dated and update the relevant README and source inventory. This collection is a one-time snapshot, not an automatic Drive/Jira synchronization.
