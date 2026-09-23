# not_for_you.md

A personal working log. Nothing here is needed to use the repository; the
[README](./README.md) and [NOTICE](./NOTICE) cover that.

There is no DEVDOC. A shelf of PDFs and one checker script has no architecture
to describe.

---

## The overhaul pass, 2026-09-23

### Nothing in here is mine

That is the whole finding, and it reframed everything else. Seven PDFs, one
two-line README, and not a page of it written by me. The README said

> It will contain all the pdf resources and notes of some of the languages and
> concepts to learn Frontend, Backend, Devops

with no hint that the contents belong to other people.

Establishing who wrote what was most of the work:

- **Five are from the Notes for Professionals series by GoalKicker.com**, built
  from Stack Overflow Documentation and released under CC BY-SA. Four announced
  themselves in their PDF metadata (`Author: GoalKicker.com`). The Git one had
  no metadata at all.
- **One is institutional lecture notes**: "Lecture Note On Internet and Web
  Technology", prepared by Rajashree Sukla, Lecturer, Department of Computer
  Science and Engineering, NM Institute of Engineering and Technology. Named
  author, named institution, no licence stated anywhere in the document.

The filenames had erased all of this. `01-frontend-html.pdf` is a fine name for
sorting a shelf and tells you nothing about who wrote the book or on what terms.

### Decoding the Git book

`00-git.pdf` had empty metadata and `pdftotext` returned nonsense:

```
,1"0#,//,#"00&,+)0
```

Not encrypted, just a font with a non-standard encoding, and the substitution is
uniform. Comparing the shape of the garbled text against the phrase every book
in that series carries gave the offset: each character is shifted by 67.
Decoding confirmed "Notes for Professionals", "goalkicker.com" and "Free
Programming Books".

Worth remembering that a PDF whose text extracts as noise is usually a font
encoding, not a corrupt file, and that a uniform substitution is trivially
recoverable if you have a crib.

### Why there is no LICENSE file

The house rule is that every repository gets MIT. Here that would be wrong
rather than merely unnecessary: an MIT licence is a grant, and granting rights
over other people's books is not something this repository is in a position to
do. It would read as a claim to have relicensed CC BY-SA material and a
lecturer's copyrighted notes.

So there is a NOTICE instead, naming each item and the terms it came with, and
the README says plainly why there is no LICENSE. This follows the same rule the
job already applies to ChatWrap, DigitalLibrary, FaceClone and MyWeather: do not
relicense someone else's work.

The lecture notes entry includes an offer to remove the document if the author
or the institution would rather it were not hosted here, with a route to ask.
That is the least that can be done while continuing to host something whose
licence is unstated.

### Binary repositories fail quietly

There is nothing to lint and nothing to build here, so the obvious answer is
that there is nothing to check. That is wrong: a truncated commit, an
interrupted download or a mishandled Git LFS migration leaves a file that is
still present, still roughly the right size in a directory listing, and no
longer openable. Nothing complains until someone clicks it, which might be
months later.

`scripts/check.py` reads each file's header, looks for `%%EOF` near the end and
counts page objects, using no third-party packages. Its page counts agree with
`pdfinfo` exactly on all seven files, which is how I know the parsing is right
rather than merely not crashing.

Proven by truncating the JavaScript book to its first 400 KB in a copy of the
tree: `no %%EOF near the end, so it looks truncated`, exit 1.

It also resolves the attribution links, because an attribution pointing nowhere
is not an attribution, and it refuses to pass if it finds no PDFs at all.

### The badge that could not pass until it existed

The first local run failed on the CI badge URL, which returns 404 until the
workflow exists on the default branch. Pushing the workflow made it 200. Not a
bug, but worth knowing before chasing it: a status badge is a chicken-and-egg
on the very first commit that introduces it.

### Left alone

- **The filenames stay as they are.** The numbering sorts the shelf into a
  sensible reading order, which is more useful day to day than titles, and the
  titles now live in NOTICE where the terms are too.
- **The default branch stays `master`.** Renaming it would break any existing
  clone or link for no benefit to a repository that is read, not developed.
- **No DEVDOC**, as above.
